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

# Proteomics d values
raw_proteomics_url = os.path.abspath("./data/sce_mct1_omics/_source/proteomics_values.txt")
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

# CYC1
cohen_d(
    proteomics_mct1.loc['CYC1'].values,
    proteomics_wt.loc['CYC1'].values)

# CYC7
cohen_d(
    proteomics_mct1.loc['CYC7'].values,
    proteomics_wt.loc['CYC7'].values)

# CTP1
cohen_d(
    proteomics_mct1.loc['CTP1'].values,
    proteomics_wt.loc['CTP1'].values)

# DIC1
cohen_d(
    proteomics_mct1.loc['DIC1'].values,
    proteomics_wt.loc['DIC1'].values)

# FUM1
cohen_d(
    proteomics_mct1.loc['FUM1'].values,
    proteomics_wt.loc['FUM1'].values)


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

# Citrate
cohen_d(
    metabolomics_mct1_15min.loc[' Citric acid '].values,
    metabolomics_wt_15min.loc[' Citric acid '].values)

# Malate
cohen_d(
    metabolomics_mct1_15min.loc[' D-Malic acid '].values,
    metabolomics_wt_15min.loc[' D-Malic acid '].values)

# Fumarate
cohen_d(
    metabolomics_mct1_15min.loc[' Fumaric acid '].values,
    metabolomics_wt_15min.loc[' Fumaric acid '].values)
