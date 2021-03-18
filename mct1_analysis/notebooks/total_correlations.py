import os
import gzip
import json
import scipy
import numpy as np
import pandas as pd
import xpressplot as xp

__path__ = os.getcwd()

# Read metadata
refine_path = os.path.join(
    __path__,
    "mct1_analysis",
    "data",
    "refine.bio.yeast.all")
with open(
        os.path.join(refine_path, 'aggregated_metadata.json'), 'r') as jsonfile:
    metadata = json.load(jsonfile)

# Read tables
tables = []
for k in metadata['experiments'].keys():
    file = os.path.join(refine_path, k, k + ".tsv")
    data = pd.read_csv(
        file,
        sep='\t',
        index_col=0
    )
    data.index.name = None
    tables.append(data)
agg_data = pd.concat(tables, axis=1)

# Perform correlation analysis
counter = 0
total = len(agg_data.index.tolist())

results = pd.DataFrame(index=agg_data.index, columns=agg_data.index)

for x in agg_data.index.tolist():
    for y in agg_data.index.tolist():
        r, p = scipy.stats.pearsonr(
            x=agg_data.loc[x].values,
            y=agg_data.loc[y].values)

        results.at[x, y] = [r, p]

    counter += 1
    if counter % 10 == 0:
        print(counter, "/", total)

# Output results table
results.to_csv(
    os.path.join(
        __path__,
        "mct1_analysis",
        "data",
        "yeast_correlations_all.tsv"),
    sep='\t')
