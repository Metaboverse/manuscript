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

# Metabolomics d values
raw_metabolomics_url = os.path.abspath("./data/lung_tumor_pr000305_st000390/measurements_values.txt")
metabolomics = pd.read_csv(
    raw_metabolomics_url,
    sep='\t',
    index_col=0)
tumor_cols = row[row == 'tumor'].index.tolist()
normal_cols = row[row == 'normal'].index.tolist()
metabolomics_tumor = metabolomics[tumor_cols]
metabolomics_normal = metabolomics[normal_cols]

# malate
cohen_d(
    metabolomics_tumor.loc['malic acid'].astype(float).values,
    metabolomics_normal.loc['malic acid'].astype(float).values)

# xanthine
cohen_d(
    metabolomics_tumor.loc['xanthine'].astype(float).values,
    metabolomics_normal.loc['xanthine'].astype(float).values)

# glutamine (fc: -0.198369384, p: 0.320542108)
cohen_d(
    metabolomics_tumor.loc['glutamine'].astype(float).values,
    metabolomics_normal.loc['glutamine'].astype(float).values)

# glyceric acid
cohen_d(
    metabolomics_tumor.loc['glyceric acid'].astype(float).values,
    metabolomics_normal.loc['glyceric acid'].astype(float).values)

# 3-Phosphoglyceric acid
cohen_d(
    metabolomics_tumor.loc['3-phosphoglycerate'].astype(float).values,
    metabolomics_normal.loc['3-phosphoglycerate'].astype(float).values)

# citrate
cohen_d(
    metabolomics_tumor.loc['citric acid'].astype(float).values,
    metabolomics_normal.loc['citric acid'].astype(float).values)

# glutamate
cohen_d(
    metabolomics_tumor.loc['glutamic acid'].astype(float).values,
    metabolomics_normal.loc['glutamic acid'].astype(float).values)

# Alpha-Ketoglutarate (fc: -0.016819815, p: 0.9380325)
cohen_d(
    metabolomics_tumor.loc['alpha ketoglutaric acid'].astype(float).values,
    metabolomics_normal.loc['alpha ketoglutaric acid'].astype(float).values)

# succinate (0.43302502	0.102575479)
cohen_d(
    metabolomics_tumor.loc['succinic acid'].astype(float).values,
    metabolomics_normal.loc['succinic acid'].astype(float).values)

# fumurate (0.09684086	0.50166131)
cohen_d(
    metabolomics_tumor.loc['fumaric acid'].astype(float).values,
    metabolomics_normal.loc['fumaric acid'].astype(float).values)
