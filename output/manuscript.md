---
author-meta:
- Jordan A. Berg
- Youjia Zhou
- T. Cameron Waller
- Ian George
- James Cox
- Bei Wang
- Jared Rutter
bibliography:
- content/manual-references.json
date-meta: '2020-02-10'
header-includes: '<!--

  Manubot generated metadata rendered from header-includes-template.html.

  Suggest improvements at https://github.com/manubot/manubot/blob/master/manubot/process/header-includes-template.html

  -->

  <meta name="dc.format" content="text/html" />

  <meta name="dc.title" content="Gazing into the Metaboverse: Automated contextualization of metabolic data" />

  <meta name="citation_title" content="Gazing into the Metaboverse: Automated contextualization of metabolic data" />

  <meta property="og:title" content="Gazing into the Metaboverse: Automated contextualization of metabolic data" />

  <meta property="twitter:title" content="Gazing into the Metaboverse: Automated contextualization of metabolic data" />

  <meta name="dc.date" content="2020-02-10" />

  <meta name="citation_publication_date" content="2020-02-10" />

  <meta name="dc.language" content="en-US" />

  <meta name="citation_language" content="en-US" />

  <meta name="dc.relation.ispartof" content="Manubot" />

  <meta name="dc.publisher" content="Manubot" />

  <meta name="citation_journal_title" content="Manubot" />

  <meta name="citation_technical_report_institution" content="Manubot" />

  <meta name="citation_author" content="Jordan A. Berg" />

  <meta name="citation_author_institution" content="Department of Biochemistry, University of Utah" />

  <meta name="citation_author_orcid" content="0000-0002-5096-0558" />

  <meta name="twitter:creator" content="@jordanberg0" />

  <meta name="citation_author" content="Youjia Zhou" />

  <meta name="citation_author_institution" content="School of Computing, University of Utah" />

  <meta name="citation_author_orcid" content="XXXX-XXXX-XXXX-XXXX" />

  <meta name="citation_author" content="T. Cameron Waller" />

  <meta name="citation_author_institution" content="Department of Biochemistry, University of Utah" />

  <meta name="citation_author_institution" content="Division of Medical Genetics, Department of Medicine, School of Medicine, University of California San Diego" />

  <meta name="citation_author_orcid" content="XXXX-XXXX-XXXX-XXXX" />

  <meta name="citation_author" content="Ian George" />

  <meta name="citation_author_institution" content="Department of Biochemistry, University of Utah" />

  <meta name="citation_author_orcid" content="XXXX-XXXX-XXXX-XXXX" />

  <meta name="citation_author" content="James Cox" />

  <meta name="citation_author_institution" content="Department of Biochemistry, University of Utah" />

  <meta name="citation_author_orcid" content="XXXX-XXXX-XXXX-XXXX" />

  <meta name="citation_author" content="Bei Wang" />

  <meta name="citation_author_institution" content="School of Computing, University of Utah" />

  <meta name="citation_author_orcid" content="XXXX-XXXX-XXXX-XXXX" />

  <meta name="citation_author" content="Jared Rutter" />

  <meta name="citation_author_institution" content="Department of Biochemistry, University of Utah" />

  <meta name="citation_author_institution" content="Howard Hughes Medical Institute, University of Utah" />

  <meta name="citation_author_orcid" content="XXXX-XXXX-XXXX-XXXX" />

  <meta property="og:type" content="article" />

  <meta property="twitter:card" content="summary_large_image" />

  <link rel="icon" type="image/png" sizes="192x192" href="https://manubot.org/favicon-192x192.png" />

  <link rel="mask-icon" href="https://manubot.org/safari-pinned-tab.svg" color="#ad1457" />

  <meta name="theme-color" content="#ad1457" />

  <!-- end Manubot generated metadata -->'
keywords:
- metabolomics
- metabolism
- network
- omics
- rna-seq
- proteomics
- gene
- protein
- metabolite
- context
lang: en-US
manubot-clear-requests-cache: false
manubot-output-bibliography: output/references.json
manubot-output-citekeys: output/citations.tsv
manubot-requests-cache-path: ci/cache/requests-cache
title: 'Gazing into the Metaboverse: Automated contextualization of metabolic data'
...






<small><em>
This manuscript
was automatically generated
on February 10, 2020.
</em></small>

## Authors


[![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0002-5096-0558)
Jordan A. Berg<sup>1</sup>,
[![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/XXXX-XXXX-XXXX-XXXX)
Youjia Zhou<sup>2</sup>,
[![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/XXXX-XXXX-XXXX-XXXX)
T. Cameron Waller<sup>1,3</sup>,
[![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/XXXX-XXXX-XXXX-XXXX)
Ian George<sup>1</sup>,
[![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/XXXX-XXXX-XXXX-XXXX)
James Cox<sup>1</sup>,
[![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/XXXX-XXXX-XXXX-XXXX)
Bei Wang<sup>2</sup>,
[![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/XXXX-XXXX-XXXX-XXXX)
Jared Rutter<sup>1,4</sup>

<sup>†</sup> --- To whom correspondence should be addressed: 

<small>


1. Department of Biochemistry, University of Utah
2. School of Computing, University of Utah
3. Division of Medical Genetics, Department of Medicine, School of Medicine, University of California San Diego
4. Howard Hughes Medical Institute, University of Utah

</small>


## Abstract {.page_break_before}

Metabolism is a complex network of perturbations to essential chemical and enzymatic reactions; however, the past century has seen a largely reductionist approach to understanding this system. While previously this approach was necessary due to technological limitations, current computer age technological advances allow us to survey, model, and explore the biological details of individual cells and populations of cells. Yet, our ability to contextualize and extract the full extent of these enormous datasets continues to lag and often results in focusing on only a handful of entities from a dataset. We therefore created Metaboverse, a multi-omic computational analysis framework  and application for the automated extraction of regulatory events from user multi-omic data within the metabolic network and interactive visualization of the data. This framework will revolutionize our ability to more holistically understand temporal metabolic shifts and gene-metabolite intra-cooperativity, as well as ensure we obtain the maximum amount of information from our data. Metaboverse if freely available under a GPL-3.0 license at [https://github.com/Metaboverse/](https://github.com/Metaboverse/).


## Introduction {.page_break_before}


## Results {.page_break_before}


## Discussion {.page_break_before}


## Methods {.page_break_before}


## Supplementary Material {.page_break_before}


## Results {.page_break_before}


## References {.page_break_before}

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>
