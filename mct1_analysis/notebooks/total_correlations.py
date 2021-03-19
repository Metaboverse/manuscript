import os
import gzip
import json
import scipy
import numpy as np
import pandas as pd
import xpressplot as xp
import matplotlib.pyplot as plt

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

results.head()

"""
count    4.558950e+07
mean     6.583752e-03
std      2.263918e-01
min     -8.725383e-01
25%     -1.422423e-01
50%     -1.673049e-03
75%      1.471100e-01
max      1.000000e+00
dtype: float64
"""
results.stack().map(lambda x: x[0]).describe()

"""
0.05   -0.357512
0.95    0.398079
dtype: float64

represents 2.27 million connections


0.025   -0.427949
0.975    0.483644
dtype: float64

represents 1.14 million connections

"""
results.stack().map(lambda x: x[0]).quantile([.025, .975])

g = results.stack().map(lambda x: x[0]).plot.hist(bins=50)
fig = g.get_figure()
fig.savefig(
    os.path.join(
        __path__,
        "mct1_analysis",
        "plots",
        "yeast_correlations_all.png"
    )
)




def g_decompress(
        path,
        file,
        output):

    g_open = open(os.path.join(path, output), "wb")
    with gzip.open(os.path.join(path, file), "rb") as f:
        g_data = f.read()
    g_open.write(g_data)
    g_open.close()

g_decompress(
    path=os.path.join(
        __path__,
        "mct1_analysis",
        "data",
        "analysis_lists"),
    file="Saccharomyces_cerevisiae.R64-1-1.103.gtf.gz",
    output="Saccharomyces_cerevisiae.R64-1-1.103.gtf"
)

gtf = pd.read_csv(
    str(os.path.join(
        __path__,
        "mct1_analysis",
        "data",
        "analysis_lists",
        "Saccharomyces_cerevisiae.R64-1-1.103.gtf")),
    sep='\t',
    comment='#',
    low_memory=False,
    header=None)

# Parse out old and new names from GTF
gtf_genes = gtf.loc[gtf[2] == 'gene']
gtf_genes['original'] = gtf[8].str.split("gene_id \"").str[1].str.split("\"; ").str[0]
gtf_genes['new'] = gtf[8].str.split("gene_name \"").str[1].str.split("\"; ").str[0]
gene_dict = pd.Series(gtf_genes['new'].values,index=gtf_genes['original']).to_dict()
for k in gene_dict.keys():
    try:
        if gene_dict[k] is np.nan:
            gene_dict[k] = k
    except:
        gene_dict[k] = k

os.remove(os.path.join(
    __path__,
    "mct1_analysis",
    "data",
    "analysis_lists",
    "Saccharomyces_cerevisiae.R64-1-1.103.gtf")
)


import networkx as nx
g = nx.Graph()

results = pd.read_csv(
    os.path.join(
        __path__,
        "mct1_analysis",
        "data",
        "yeast_correlations_all.tsv"),
    sep='\t',
    index_col=0,
    low_memory=False
)

import ast
for c in results.columns.tolist():
    results[c] = results[c].apply(lambda x: ast.literal_eval(x))


for x in results.index.tolist():
    g.add_node(x)
    g.nodes()[x]['id'] = x
    g.nodes()[x]['name'] = gene_dict[x]


"""
0.025   -0.427949
0.975    0.483644
"""
for x in results.index.tolist():
    for y in results.index.tolist():
        if results.at[x, y][0] >= 0.483644 or results.at[x, y][0] <= -0.427949 and results.at[x, y][1] < 0.05:
            g.add_edge(x, y)
            g.edges()[(x, y)]['r'] = results.at[x, y][0]
            g.edges()[(x, y)]['p'] = results.at[x, y][1]

import json
from networkx.readwrite import json_graph

data = json_graph.node_link_data(g)
with open(os.path.join(
        __path__,
        "mct1_analysis",
        "data",
        "yeast_correlations_graph.json"),
    'w') as f:
    json.dump(data, f, indent=4)  # Parse out as array for javascript



# Plot clustered heatmap of r values
# generate graph, maybe more strict, make sure it was selective in the code above.
