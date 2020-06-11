import os
import pandas as pd
import scipy
from scipy.optimize import curve_fit
from scipy.stats import linregress
import matplotlib.pyplot as plt

__path__ = os.path.abspath("./data/flux_sandbox/") + '/'
__data__ = 'flux_test.txt'

def agg_data(
        file):

    # Input must have all #!DIV/0 errors forced to '0'
    data = pd.read_csv(
        file,
        sep='\t',
        index_col=0
    )

    group_index = []
    for idx in data.index.tolist():
        try:
            int(idx.rpartition('-')[-1])
            group_index.append(idx.rpartition('-')[0:1][0])
        except:
            try:
                int(idx.rpartition(' ')[-1])
                group_index.append(idx.rpartition(' ')[0:1][0])
            except:
                print(idx + ' is not splittable')
                group_index.append(idx)
            pass
    data['group'] = group_index

    data_agg = data.groupby('group').agg(lambda x: list(x))
    data_agg.index.name = None

    return data_agg

data_sub = agg_data(
    file=__path__ + 'flux_test_sub.txt')

sub_cols = data_sub.columns.tolist()
data_sub_c = data_sub.copy()
for index, row in data_sub.iterrows():

    for x in range(len(row)):
        lens = [y for y in range(len(row[x]))]
        vals = row[x]

        slope, intercept, r_value, p_value, std_err = linregress(lens, vals)
        data_sub.at[index, sub_cols[x]] = r_value


data_sub.loc[data_sub['15v6_2'] > data_sub['15v6_0']].T.plot(figsize=(15,5))

data_sub.loc[data_sub['15v6_2'] < data_sub['15v6_0']].T.plot(figsize=(15,5))


data_div = agg_data(
    file=__path__ + 'flux_test_div.txt')
div_cols = data_div.columns.tolist()
data_div_c = data_div.copy()
for index, row in data_div.iterrows():

    for x in range(len(row)):
        lens = [y for y in range(len(row[x]))]
        vals = row[x]

        slope, intercept, r_value, p_value, std_err = linregress(lens, vals)
        data_div.at[index, sub_cols[x]] = r_value

data_div.loc[data_div['15v6_2'] > data_div['15v6_0']].T.plot(figsize=(15,5))
data_div.loc[data_div['15v6_2'] < data_div['15v6_0']].T.plot(figsize=(15,5))
