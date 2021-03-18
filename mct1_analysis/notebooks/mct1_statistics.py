from __future__ import division
import os
import sys
import pandas as pd
from numpy import mean, std
from math import sqrt

def cohen_d(x,y):
    return (
        mean(x) - mean(y)) / sqrt((std(x, ddof=1) ** 2 + std(y, ddof=1) ** 2) / 2.0
    )


os.path.abspath(".")

# Proteomics d values
raw_proteomics_url = os.path.abspath(os.path.join("..", "data", "mct1_proteomics_data", "proteomics_values.txt"))
proteomics = pd.read_csv(
    raw_proteomics_url,
    sep='\t',
    index_col=0)
proteomics_mct1 = proteomics[[
    'mct1_1',
    'mct1_2',
    'mct1_3']]
proteomics_wt = proteomics[[
    'WT_1',
    'WT_2',
    'WT_3']]

protein_list = [
    'BI4',
    'COR1',
    'CTP1',
    'CYC1',
    'CYC7',
    'CYT1',
    'DIC1',
    'FUM1',
    'GDH1',
    'GDH2',
    'MAE1',
    'MAS1',
    'MAS2',
    'PYC1',
    'PYC2',
    'QCR6',
    'QCR7',
    'QCR8',
    'RIP1',
    'ACO1',
    'ACO2',
    'CIT2',
    'ICL1',
    'MDH2',
    'MDH3',
    'MLS1'
]

for x in protein_list:
    print(x)
    print('Cohen\'s d: '+ str(
        cohen_d(
            proteomics_mct1.loc[x].values,
            proteomics_wt.loc[x].values)
        )
    )




# Metabolomics d values
raw_metabolomics_url_15min = os.path.abspath("./data/sce_mct1_omics/_source/metabolomics_values_15min.txt")
metabolomics = pd.read_csv(
    raw_metabolomics_url_15min,
    sep='\t',
    index_col=0)
metabolomics_mct1_15min = metabolomics[[
    'mct1_15min_1',
    'mct1_15min_2',
    'mct1_15min_3',
    'mct1_15min_4',
    'mct1_15min_5',
    'mct1_15min_6']]
metabolomics_wt_15min = metabolomics[[
    'WT_15min_1',
    'WT_15min_2',
    'WT_15min_3',
    'WT_15min_4',
    'WT_15min_5',
    'WT_15min_6']]

raw_metabolomics_url_60min = os.path.abspath("./data/sce_mct1_omics/_source/metabolomics_values_60min.txt")
metabolomics_60min = pd.read_csv(
    raw_metabolomics_url_60min,
    sep='\t',
    index_col=0)
metabolomics_mct1_60min = metabolomics_60min[[
    'mct1KO at 1hr minR+Leu 0',
    'mct1KO at 1hr minR+Leu 1',
    'mct1KO at 1hr minR+Leu 2',
    'mct1KO at 1hr minR+Leu 3',
    'mct1KO at 1hr minR+Leu 4',
    'mct1KO at 1hr minR+Leu 5'
]]
metabolomics_wt_60min = metabolomics_60min[[
    'WT at 1hr minR+Leu 0',
    'WT at 1hr minR+Leu 1',
    'WT at 1hr minR+Leu 2',
    'WT at 1hr minR+Leu 3',
    'WT at 1hr minR+Leu 4',
    'WT at 1hr minR+Leu 5'
]]

# Citrate
cohen_d(
    metabolomics_mct1_15min.loc[' Citric acid '].values,
    metabolomics_wt_15min.loc[' Citric acid '].values)

# Malate
cohen_d(
    metabolomics_mct1_15min.loc[' D-Malic acid '].values,
    metabolomics_wt_15min.loc[' D-Malic acid '].values)

# Succinate
cohen_d(
    metabolomics_mct1_15min.loc[' Succinic acid '].values,
    metabolomics_wt_15min.loc[' Succinic acid '].values)

# Fumarate
cohen_d(
    metabolomics_mct1_15min.loc[' Fumaric acid '].values,
    metabolomics_wt_15min.loc[' Fumaric acid '].values)

# GSH
cohen_d(
    metabolomics_mct1_60min.loc['Glutathione'].values,
    metabolomics_wt_60min.loc['Glutathione'].values)

# LACT
cohen_d(
    metabolomics_mct1_60min.loc['L-Lactic acid'].values,
    metabolomics_wt_60min.loc['L-Lactic acid'].values)
