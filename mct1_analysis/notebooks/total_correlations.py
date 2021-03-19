import os
import sys
import gzip
import json
import scipy
import ast
import json
import numpy as np
import pandas as pd
import xpressplot as xp
import matplotlib.pyplot as plt
import networkx as nx
from networkx.readwrite import json_graph
import seaborn as sns
sns.set(font='arial')
sns.set(font_scale=float(.1))
jakes_cmap = sns.diverging_palette(212, 61, s=99, l=77, sep=1, n=16, center='dark') #Custom aesthetics

__path__ = os.getcwd()

# Read metadata
def read_agg_data():

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

    return agg_data


def corr_agg_data(agg_data):
    # Perform correlation analysis
    counter = 0
    total = len(agg_data.index.tolist())
    results_r = pd.DataFrame(index=agg_data.index, columns=agg_data.index)
    results_p = pd.DataFrame(index=agg_data.index, columns=agg_data.index)

    for x in agg_data.index.tolist():
        for y in agg_data.index.tolist():
            r, p = scipy.stats.pearsonr(
                x=agg_data.loc[x].values,
                y=agg_data.loc[y].values)

            results_r.at[x, y] = r
            results_p.at[x, y] = p

        counter += 1
        if counter % 10 == 0:
            print(counter, "/", total)
            sys.stdout.flush()

    # Output results table
    results_r.to_csv(
        os.path.join(
            __path__,
            "mct1_analysis",
            "data",
            "yeast_correlations_all_r.tsv"),
        sep='\t')

    # Output results table
    results_p.to_csv(
        os.path.join(
            __path__,
            "mct1_analysis",
            "data",
            "yeast_correlations_all_p.tsv"),
        sep='\t')

    return results_r, results_p


def plot_historgrams(results_r, results_p):

    f = results_r.stack().plot.hist(bins=50)
    fig = f.get_figure()
    fig.savefig(
        os.path.join(
            __path__,
            "mct1_analysis",
            "plots",
            "yeast_correlations_all_r_hist.png"
        )
    )

    g = results_p.stack().plot.hist(bins=50)
    fig = g.get_figure()
    fig.savefig(
        os.path.join(
            __path__,
            "mct1_analysis",
            "plots",
            "yeast_correlations_all_p_hist.png"
        )
    )


def get_quantiles(results, _range):

    r = results.stack().quantile(_range)
    return r.iloc[0], r.iloc[1]

def make_gene_dict():


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

    return gene_dict


def read_corr_data():

    results_r = pd.read_csv(
        os.path.join(
            __path__,
            "mct1_analysis",
            "data",
            "yeast_correlations_all_r.tsv"),
        sep='\t',
        index_col=0,
        low_memory=False
    )

    results_p = pd.read_csv(
        os.path.join(
            __path__,
            "mct1_analysis",
            "data",
            "yeast_correlations_all_p.tsv"),
        sep='\t',
        index_col=0,
        low_memory=False
    )

    return results_r, results_p


def get_graph(results_r, results_p, min, max, thresh=0.01):

    g = nx.Graph()

    for x in results.index.tolist():
        g.add_node(x)
        g.nodes()[x]['id'] = x
        g.nodes()[x]['name'] = gene_dict[x]
    print("Nodes:", str(len(g.nodes())))
    sys.stdout.flush()

    for x in results_r.index.tolist():
        for y in results_r.index.tolist():
            if results_r.at[x, y] >= max or results_r.at[x, y] <= min and results_p.at[x, y] < thresh:
                g.add_edge(x, y)
                g.edges()[(x, y)]['r'] = results_r.at[x, y]
                g.edges()[(x, y)]['p'] = results_p.at[x, y]
    print("Edges:", str(len(g.edges())))
    sys.stdout.flush()

    return g


def output_graph(g):

    data = json_graph.node_link_data(g)
    with open(os.path.join(
            __path__,
            "mct1_analysis",
            "data",
            "yeast_correlations_graph.json"),
        'w') as f:
        json.dump(data, f, indent=4)  # Parse out as array for javascript


def read_graph():


    with open(os.path.join(
            __path__,
            "mct1_analysis",
            "data",
            "yeast_correlations_graph.json")) as f:
        js_graph = json.load(f)
    g = json_graph.node_link_graph(js_graph)

    return g


def make_subgraph(g, gene_dict, s, t):

    gg = nx.Graph()
    for x in nx.all_shortest_paths(g, source=s, target=t):
        for y in range(len(x)):
            try:
                gg.add_node(gene_dict[x[y]])
                gg.add_edge(gene_dict[x[y]], gene_dict[x[y+1]])
            except:
                pass

    data = json_graph.node_link_data(gg)
    with open(os.path.join(
            __path__,
            "mct1_analysis",
            "data",
            "yeast_correlations_graph" + str(gene_dict[s]) + "_" + str(gene_dict[t]) + ".json"),
        'w') as f:
        json.dump(data, f, indent=4)


def make_hist_gene(results_r, results_p, gene=''):

    f = results_r[gene].plot.hist(bins=50)
    fig = f.get_figure()
    fig.savefig(
        os.path.join(
            __path__,
            "mct1_analysis",
            "plots",
            "yeast_correlations_" + str(gene) + "_r_hist.png"
        )
    )

    g = results_p[gene].plot.hist(bins=50)
    fig = g.get_figure()
    fig.savefig(
        os.path.join(
            __path__,
            "mct1_analysis",
            "plots",
            "yeast_correlations_" + str(gene) + "_p_hist.png"
        )
    )


def make_clustermap(results_r):
    # Plot clustered heatmap of r values
    # generate graph, maybe more strict, make sure it was selective in the code above.

    ax = sns.clustermap(results_r,
        center=0,
        metric='euclidean',
        method='centroid',
        xticklabels=True,
        yticklabels=True,
        linewidths=0,
        linecolor='#DCDCDC',
        cmap=jakes_cmap,
        col_cluster=True,
        row_cluster=True,
        figsize=(100,100))
    plt.savefig(os.path.join(
            __path__,
            "mct1_analysis",
            "data",
            "yeast_correlations_clustered.pdf"), bbox_inches='tight')


"""MAIN"""
print('Reading agg data')
sys.stdout.flush()
agg_data = read_agg_data()
print('Performing correlation analysis')
sys.stdout.flush()
results_r, results_p = corr_agg_data(agg_data)
print('Plotting total dataset histograms')
sys.stdout.flush()
plot_histograms(results_r, results_p)
print('Getting quantiles')
sys.stdout.flush()
min, max = get_quantiles(results_r, [.01, .99])

print('Making gene dict')
sys.stdout.flush()
gene_dict = make_gene_dict()
print('Reading correlations')
sys.stdout.flush()
results_r, results_p = read_corr_data()
print('Constructing graph')
sys.stdout.flush()
g = get_graph(results_r, results_p, min, max)
print('Outputting graph')
sys.stdout.flush()
output_graph(g)

print('Reading graph')
sys.stdout.flush()
g = read_graph()

print('Making subgraph:', 'YOR221C', 'YBR291C')
sys.stdout.flush()
make_subgraph(g, gene_dict, s='YOR221C', t='YBR291C') # MCT1 vs CTP1
print('Making subgraph:', 'YOR221C', 'YKL192C')
sys.stdout.flush()
make_subgraph(g, gene_dict, s='YOR221C', t='YKL192C') # MCT1 vs ACP1
print('Making subgraph:', 'YJR066W', 'YKL203C')
sys.stdout.flush()
make_subgraph(g, gene_dict, s='YJR066W', t='YKL203C') # TOR1 vs TOR2
print('Making subgraph:', 'YJR066W', 'YJL052W')
sys.stdout.flush()
make_subgraph(g, gene_dict, s='YJR066W', t='YJL052W') # Random -- TOR1 vs TDH1

print('Making gene histogram:', 'YOR221C')
sys.stdout.flush()
make_hist_gene(results_r, results_p, gene='YOR221C')
print('Making gene histogram:', 'YBR291C')
sys.stdout.flush()
make_hist_gene(results_r, results_p, gene='YBR291C')

print('Making clustermap')
sys.stdout.flush()
make_clustermap(results_r)
