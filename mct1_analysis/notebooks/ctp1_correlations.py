"""CTP1 correlation analysis
Purpose: determine correlative effects between CTP1 and glyoxylate pathway genes
"""
import os
import gzip
import json
import scipy
import numpy as np
import pandas as pd
import xpressplot as xp

__path__ = os.getcwd()


"""Functions
"""
def read_table(
        url,
        sep='\t',
        index_col=0,
        header='infer',
        low_memory=False,
        compression='infer',
        comment='#'):
    """Read tab-delimited table
    """

    data = pd.read_csv(
        url,
        sep=sep,
        index_col=index_col,
        header=header,
        low_memory=low_memory,
        compression=compression,
        comment=comment)

    return data


def parse_genelist(
        url,
        gene_name,
        gene_id,
        sep='\t',
        comment='#'):
    """Parse gene list from file
    """

    data = pd.read_csv(
        url,
        sep=sep,
        comment=comment)

    gene_names = list(set(data[gene_name].tolist()))
    gene_ids = list(set(data[gene_id].tolist()))

    gene_dict = {}
    for index, row in data.iterrows():
        gene_dict[row[gene_id]] = row[gene_name]

    return gene_names, gene_ids, gene_dict


def g_decompress(
        path,
        file,
        output):

    g_open = open(os.path.join(path, output), "wb")
    with gzip.open(os.path.join(path, file), "rb") as f:
        g_data = f.read()
    g_open.write(g_data)
    g_open.close()


"""Part 0: Read in gene lists for analysis
"""
query_name = 'CTP1'
query_id = 'YBR291C'

query_name2 = 'MCT1'
query_id2 = 'YOR221C'

glyoxylate_names, glyoxylate_ids, glyoxylate_dict = parse_genelist(
    url=os.path.join(
        __path__,
        "mct1_analysis",
        "data",
        "analysis_lists",
        "glyoxylate-cycle-pathway-genes-sgd.txt"),
    gene_name="Gene name",
    gene_id="Gene ID"
)

"""Part 1: Correlation analysis for mct1 datasets
"""
mct1_rnaseq = read_table(
    url=os.path.join(
        __path__,
        "mct1_analysis",
        "data",
        "mct1_rnaseq_data",
        "sce_mct1_deduped_count_table.tsv")
)
yeast_gtf = read_table(
    url=os.path.join(
        __path__,
        "mct1_analysis",
        "data",
        "analysis_lists",
        "Saccharomyces_cerevisiae.R64-1-1.103.gtf.gz"),
    index_col=None,
    header=None,
    comment='#'
)

g_decompress(
    path=os.path.join(
        __path__,
        "mct1_analysis",
        "data",
        "analysis_lists"),
    file="Saccharomyces_cerevisiae.R64-1-1.103.gtf.gz",
    output="Saccharomyces_cerevisiae.R64-1-1.103.gtf"
)
mct1_rnaseq_norm = xp.tpm(
    data=mct1_rnaseq,
    gtf=os.path.join(
        __path__,
        "mct1_analysis",
        "data",
        "analysis_lists",
        "Saccharomyces_cerevisiae.R64-1-1.103.gtf"),
    identifier='gene_id'
)
os.remove(os.path.join(
    __path__,
    "mct1_analysis",
    "data",
    "analysis_lists",
    "Saccharomyces_cerevisiae.R64-1-1.103.gtf")
)

mct1_proteomics = read_table(
    url=os.path.join(
        __path__,
        "mct1_analysis",
        "data",
        "mct1_proteomics_data",
        "proteomics_values.txt")
)


mct1_proteomics.loc['ACO1']

mct1_proteomics.loc['ACO2']

mct1_proteomics.loc['CTP1']

for x in glyoxylate_ids:
    r, p = scipy.stats.pearsonr(
        x=mct1_rnaseq_norm.loc[query_id].values,
        y=mct1_rnaseq_norm.loc[x].values)

    print("pearson", glyoxylate_dict[x], ":", str(r), str(p))

    #rho, p = scipy.stats.spearmanr(
    #    a=mct1_rnaseq_norm.loc[query_id].values,
    #    b=mct1_rnaseq_norm.loc[x].values)

    #print("spearman", x, ":", str(rho), str(p))

mct1_rnaseq_norm_c = mct1_rnaseq_norm.copy()
for x in mct1_rnaseq_norm.index.tolist():
    r, p = scipy.stats.pearsonr(
        x=mct1_rnaseq_norm.loc[query_id].values,
        y=mct1_rnaseq_norm.loc[x].values)

    mct1_rnaseq_norm_c.at[x, 'pearson_r'] = r

mct1_rnaseq_norm_c['pearson_r'].hist(bins=50)


for x in glyoxylate_names:

    if x in mct1_proteomics.index.tolist():
        r, p = scipy.stats.pearsonr(
            x=mct1_proteomics.loc[query_name].values,
            y=mct1_proteomics.loc[x].values)

        print("pearson", x, ":", str(r), str(p))

mct1_proteomics_c = mct1_proteomics.copy()
for x in mct1_proteomics.index.tolist():
    if x in mct1_proteomics.index.tolist():
        r, p = scipy.stats.pearsonr(
            x=mct1_proteomics.loc[query_name].values,
            y=mct1_proteomics.loc[x].values)
        mct1_proteomics_c.at[x, 'pearson_r'] = r


mct1_proteomics_c['pearson_r'].hist(bins=50)







mct1_rnaseq_norm.head()
agg_data = mct1_rnaseq_norm.copy()

counter = 0
total = len(agg_data.index.tolist())
results_r = pd.DataFrame(index=agg_data.index, columns=agg_data.index)
results_p = pd.DataFrame(index=agg_data.index, columns=agg_data.index)


for x in agg_data.index.tolist():
    for y in agg_data.index.tolist():

        if sum(agg_data.loc[x].values) != 0 and sum(agg_data.loc[y].values != 0):
            r, p = scipy.stats.pearsonr(
                x=agg_data.loc[x].values,
                y=agg_data.loc[y].values)

            results_r.at[x, y] = r
            results_p.at[x, y] = p
        else:
            results_r.at[x, y] = 0.0
            results_p.at[x, y] = 1.0

    counter += 1
    if counter % 10 == 0:
        print(counter, "/", total)


# Output results table
results_r.to_csv(
    os.path.join(
        __path__,
        "mct1_analysis",
        "data",
        "yeast_correlations_rnaseq_r.tsv"),
    sep='\t')

# Output results table
results_p.to_csv(
    os.path.join(
        __path__,
        "mct1_analysis",
        "data",
        "yeast_correlations_rnaseq_p.tsv"),
    sep='\t')










"""Part 2: Correlation analysis for refine.bio dataset
"""
refine_path = os.path.join(
    __path__,
    "mct1_analysis",
    "data",
    "refine.bio.yeast.all")
with open(
        os.path.join(refine_path, 'aggregated_metadata.json'), 'r') as jsonfile:
    metadata = json.load(jsonfile)

metadata['samples']['ERR1095152']['refinebio_treatment']


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


agg_data_c = agg_data.copy()
for x in agg_data.index.tolist():
    r, p = scipy.stats.pearsonr(
        x=agg_data.loc[query_id].values,
        y=agg_data.loc[x].values)
    agg_data_c.at[x, 'pearson_r_ctp1'] = r
for x in agg_data.index.tolist():
    r, p = scipy.stats.pearsonr(
        x=agg_data.loc[query_id2].values,
        y=agg_data.loc[x].values)
    agg_data_c.at[x, 'pearson_r_mct1'] = r

agg_data_c['pearson_r_ctp1'].hist(bins=50)

agg_data_c['pearson_r_mct1'].hist(bins=50)

for x in glyoxylate_ids:
    r, p = scipy.stats.pearsonr(
        x=agg_data.loc[query_id].values,
        y=agg_data.loc[x].values)

    print("pearson", glyoxylate_dict[x], ":", str(r), str(p))


for x in glyoxylate_ids:
    r, p = scipy.stats.pearsonr(
        x=agg_data.loc[query_id2].values,
        y=agg_data.loc[x].values)

    print("pearson", glyoxylate_dict[x], ":", str(r), str(p))




# top 1% correlated genes with CTP1
ctp1_corr = agg_data_c.sort_values(by='pearson_r_ctp1').tail(int(len(agg_data_c.index.tolist()) * 0.01)).index.tolist()
for a in reversed(ctp1_corr):
    print(a)

# top 1% anti-correlated genes with CTP1
for a in agg_data_c.sort_values(by='pearson_r_ctp1').head(int(len(agg_data_c.index.tolist()) * 0.01)).index.tolist():
    print(a)


# top 1% correlated genes with MCT1
mct1_corr = agg_data_c.sort_values(by='pearson_r_mct1').tail(int(len(agg_data_c.index.tolist()) * 0.01)).index.tolist()
for a in reversed(mct1_corr):
    print(a)

# top 1% anti-correlated genes with MCT1
for a in agg_data_c.sort_values(by='pearson_r_mct1').head(int(len(agg_data_c.index.tolist()) * 0.01)).index.tolist():
    print(a)


for z in []:
    np.log2(agg_data).T.plot.scatter(z, 'YOR221C', alpha=0.1)




np.log2(agg_data).T.plot.scatter('YNR050C', 'YBR291C', alpha=0.1)
np.log2(agg_data).T.plot.scatter('YJL200C', 'YBR291C', alpha=0.1)
np.log2(agg_data).T.plot.scatter('YDL131W', 'YBR291C', alpha=0.1)
np.log2(agg_data).T.plot.scatter('YIR034C', 'YBR291C', alpha=0.1)







#ACO2
np.log10(agg_data).T.plot.scatter(query_id, 'YJL200C', alpha=0.1)


np.log10(agg_data).T.plot.scatter(query_id, 'YML117W', alpha=0.1)








np.log10(agg_data).T.plot.scatter(query_id2, 'YIL016W', alpha=0.1)




np.log10(agg_data).T.plot.scatter(query_id, 'YLR304C', alpha=0.1)

12





"""Part 3: CTP1 vs all genes & correlation coefficient distribution
"""


yeast_gtf[8].loc[1]



agg_data_named = agg_data.copy()
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


ctp1_id = "YBR291C"
mct1_id = "YOR221C"
rtg = [
    'YNR001C',
    'YNL037C',
    'YOR136W',
    'YLR304C',
    'YCR005C',
    'YGL062W',
    'YEL071W',
    'YPL265W',
    'YMR083W'
]

aneu = [
    'YKL029C',
    'YGL062W',
    'YBR218C',
    'YOR375C',
    'YDL215C'
]

import matplotlib.pyplot as plt
for x in rtg:
    r, p = scipy.stats.pearsonr(
        x=agg_data.loc[ctp1_id].values,
        y=agg_data.loc[x].values)

    print(gene_dict[x], ":", r, p)
    np.log10(agg_data).T.plot.scatter(ctp1_id, x, alpha=0.1)
    plt.show()


for x in rtg:
    r, p = scipy.stats.pearsonr(
        x=agg_data.loc[mct1_id].values,
        y=agg_data.loc[x].values)

    print(gene_dict[x], ":", r, p)
    np.log10(agg_data).T.plot.scatter(mct1_id, x, alpha=0.1)
    plt.show()



for x in aneu:
    r, p = scipy.stats.pearsonr(
        x=agg_data.loc[ctp1_id].values,
        y=agg_data.loc[x].values)

    print(gene_dict[x], ":", r, p)
    np.log10(agg_data).T.plot.scatter(ctp1_id, x, alpha=0.1)
    plt.show()


for x in aneu:
    r, p = scipy.stats.pearsonr(
        x=agg_data.loc[mct1_id].values,
        y=agg_data.loc[x].values)

    print(gene_dict[x], ":", r, p)
    np.log10(agg_data).T.plot.scatter(mct1_id, x, alpha=0.1)
    plt.show()


agg_data_c['pearson_r_ctp1'].hist(bins=50)




query_id
query_id2
r, p = scipy.stats.pearsonr(
    x=agg_data.loc[query_id].values,
    y=agg_data.loc[query_id2].values)

print(gene_dict[query_id], gene_dict[query_id2], ":", r, p)
np.log10(agg_data).T.plot.scatter(query_id, query_id2, alpha=0.1)
plt.show()



agg_data_c['pearson_r_mct1'].hist(bins=50)











# top 1% correlated genes with query
query_corr = agg_data_c.sort_values(by='pearson_r_query').tail(int(len(agg_data_c.index.tolist()) * 0.01)).index.tolist()
for a in reversed(query_corr):
    print(gene_dict[a])

# top 1% anti-correlated genes with query
for a in agg_data_c.sort_values(by='pearson_r_query').head(int(len(agg_data_c.index.tolist()) * 0.01)).index.tolist():
    print(gene_dict[a])








"""
"""
