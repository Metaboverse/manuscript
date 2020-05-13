---
author-meta:
- Jordan A. Berg
- Youjia Zhou
- T. Cameron Waller
- Yeyun Ouyang
- Sara M. Nowinski
- Tyler Van Ry
- James Cox
- Bei Wang
- Jared Rutter
bibliography:
- content/manual-references.json
date-meta: '2020-05-13'
header-includes: '<!--

  Manubot generated metadata rendered from header-includes-template.html.

  Suggest improvements at https://github.com/manubot/manubot/blob/master/manubot/process/header-includes-template.html

  -->

  <meta name="dc.format" content="text/html" />

  <meta name="dc.title" content="Gazing into the Metaboverse: Automated exploration and contextualization of metabolic data" />

  <meta name="citation_title" content="Gazing into the Metaboverse: Automated exploration and contextualization of metabolic data" />

  <meta property="og:title" content="Gazing into the Metaboverse: Automated exploration and contextualization of metabolic data" />

  <meta property="twitter:title" content="Gazing into the Metaboverse: Automated exploration and contextualization of metabolic data" />

  <meta name="dc.date" content="2020-05-13" />

  <meta name="citation_publication_date" content="2020-05-13" />

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

  <meta name="citation_author_institution" content="Scientific Computing &amp; Imaging Institute, University of Utah" />

  <meta name="citation_author_orcid" content="XXXX-XXXX-XXXX-XXXX" />

  <meta name="citation_author" content="T. Cameron Waller" />

  <meta name="citation_author_institution" content="Division of Medical Genetics, Department of Medicine, School of Medicine, University of California San Diego" />

  <meta name="citation_author_orcid" content="0000-0002-0313-6646" />

  <meta name="citation_author" content="Yeyun Ouyang" />

  <meta name="citation_author_institution" content="Department of Biochemistry, University of Utah" />

  <meta name="citation_author_orcid" content="0000-0001-9523-1044" />

  <meta name="citation_author" content="Sara M. Nowinski" />

  <meta name="citation_author_institution" content="Department of Biochemistry, University of Utah" />

  <meta name="citation_author_orcid" content="0000-0002-4744-6101" />

  <meta name="citation_author" content="Tyler Van Ry" />

  <meta name="citation_author_institution" content="Department of Biochemistry, University of Utah" />

  <meta name="citation_author_institution" content="Metabolomics Core Facility, University of Utah" />

  <meta name="citation_author_orcid" content="XXXX-XXXX-XXXX-XXXX" />

  <meta name="citation_author" content="James Cox" />

  <meta name="citation_author_institution" content="Department of Biochemistry, University of Utah" />

  <meta name="citation_author_institution" content="Diabetes &amp; Metabolism Research Center, University of Utah" />

  <meta name="citation_author_institution" content="Metabolomics Core Facility, University of Utah" />

  <meta name="citation_author_orcid" content="0000-0002-5977-2350" />

  <meta name="citation_author" content="Bei Wang" />

  <meta name="citation_author_institution" content="School of Computing, University of Utah" />

  <meta name="citation_author_institution" content="Scientific Computing &amp; Imaging Institute, University of Utah" />

  <meta name="citation_author_orcid" content="XXXX-XXXX-XXXX-XXXX" />

  <meta name="citation_author" content="Jared Rutter" />

  <meta name="citation_author_institution" content="Department of Biochemistry, University of Utah" />

  <meta name="citation_author_institution" content="Diabetes &amp; Metabolism Research Center, University of Utah" />

  <meta name="citation_author_institution" content="Howard Hughes Medical Institute, University of Utah" />

  <meta name="citation_author_orcid" content="0000-0002-2710-9765" />

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
title: 'Gazing into the Metaboverse: Automated exploration and contextualization of metabolic data'
...






<small><em>
This manuscript
was automatically generated
on May 13, 2020.
</em></small>

## Authors


[![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0002-5096-0558)
Jordan A. Berg<sup>1</sup>,
[![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/XXXX-XXXX-XXXX-XXXX)
Youjia Zhou<sup>2,3</sup>,
[![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0002-0313-6646)
T. Cameron Waller<sup>4</sup>,
[![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0001-9523-1044)
Yeyun Ouyang<sup>1</sup>,
[![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0002-4744-6101)
Sara M. Nowinski<sup>1</sup>,
[![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/XXXX-XXXX-XXXX-XXXX)
Tyler Van Ry<sup>1,5</sup>,
[![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0002-5977-2350)
James Cox<sup>1,5,6</sup>,
[![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/XXXX-XXXX-XXXX-XXXX)
Bei Wang<sup>2,3</sup>,
[![ORCID icon](images/orcid.svg){height="11px" width="11px"}](https://orcid.org/0000-0002-2710-9765)
Jared Rutter<sup>1,6,7</sup>
<small>

1. Department of Biochemistry, University of Utah
2. School of Computing, University of Utah
3. Scientific Computing & Imaging Institute, University of Utah
4. Division of Medical Genetics, Department of Medicine, School of Medicine, University of California San Diego
5. Metabolomics Core Facility, University of Utah
6. Diabetes & Metabolism Research Center, University of Utah
7. Howard Hughes Medical Institute, University of Utah
</small>


<sup>†</sup> To whom correspondence should be addressed:

<sup>\*</sup> This is a draft of the eventual final manuscript, and should therefore be treated as such. Conclusions, along with author order and contributions, may change as the manuscript is finalized.


## Abstract {.page_break_before}

Metabolism and other biological interactions and reactions are complex, each with their specific inputs, outputs, and modifiers. The harmony between these factors consequently determines the health and stability of a cell or organism. Perturbations often have rippling downstream effects. These effects can be difficult to trace across the global reaction network, particularly when the effects cross canonical illustrations of pathways. Researchers have largely utilized reductionist approaches to understanding these systems; however, these methods are limited in their scope, and even systems-centric -omics approaches are often used to identify the differentially expressed or abundant factors and the downstream analysis of the model is then limited to these handful or "loud" signals in the data. To address these challenges, we developed Metaboverse, a multi-omic computational platform for the interactive exploration and automated extraction of potential regulatory events, patterns, and trends from user data within the context of the metabolic network. This framework will be foundational in increasing our ability to holistically understand static and temporal metabolic events and shifts and gene-metabolite intra-cooperativity, as well as ensure we obtain the maximum extraction of information from our data. Metaboverse if freely available under a GPL-3.0 license at [https://github.com/Metaboverse/](https://github.com/Metaboverse/).


## Introduction

Metabolism is a complex network of reactions and interactions between genes, enzymes, complexes, and metabolites [@doi:10.3390/metabo9040076]. To understand these complex components, researchers normally adopt a reductionist approach to teasing apart the characteristics and mechanics of these processes and how they fit into the larger picture of biology and disease. While a vital component in the scientific process, by doing so, many interesting properties of metabolism can be missed. For example, in differential gene expression analysis, researchers rely on thresholds of magnitude and statistical significance to prioritize genes for follow-up study. However, doing so can inadvertently limit the scope of study of metabolism when in fact metabolism is a highly interconnected system where distal components and their modulation can have rippling effects across the network. The current approach is analogous to telling the story of Little Red Riding Hood, but only by reading the 20 most frequent words used in the study. Certainly doing so efficiently highlights key words like "wolf" and "little red riding hood," but also prevents a coherent story from being told and would make it difficult for someone who had never read the story of Little Red Riding Hood from comprehending the story.

Over the past decade, several computational tools have emerged and become popular for their focus on trying to solve these issues in data contextualization. We will highlight four, and while others exist, we focus on tools representative and most popular for their respective properties. First is MetaboAnalyst, which relies largely on set enrichment methods, or looking at the belongingness of sets of significantly changed analytes (i.e. metabolite, protein, or gene measurements), for extracting interesting information. While network visualization is available, its ability to extract regulatory information is limited, particularly in an automated fashion [@doi:10.1093/nar/gkp356; @doi:10.1093/nar/gky310]. Second is Cytoscape, which focuses on network representations of metabolism and other systems. While a variety of plug-ins are available for customizing analyses, again, comprehensive regulatory identification methods are unavailable [@doi:10.1101/gr.1239303]. MetExplore focuses on the curation of networks, and is particularly useful for collaborative annotation of emerging organisms. It additionally can layer experimental data on the network for visualization [@doi:10.1093/nar/gky301; @doi:10.1093/nar/gkq312]. Reactome, which Metaboverse uses for the curation of biological networks, also offers analytical tools for user data, but again relies on set enrichment or manual methods for identifying patterns. While all have their respective utility, there is still a need for tools that automate pattern and trend detection, especially when data is sparse, across metabolic networks in order to extract regulatory and other features from data [@doi:10.1093/nar/gki072; @pmid:31691815; @pmid:29145629].

In order to address these limitations in current conventions of metabolic data analysis, contextualization, and interpretation, we created the software application, Metaboverse, to aid users in filling in and expanding upon the details of their model's metabolic story. Metaboverse is an interactive tool for exploratory data analysis that searches user data in the context of the metabolic network to identify interesting patterns and trends within the data. Metaboverse will aid scientists in formulating new hypotheses from their data and aid them in designing follow-up experiments for a deeper understanding of their model. Metaboverse operates across the entire metabolic network to quickly and automatically detect patterns and trends from a pre-designed pattern library, or can accept interactive input from the user where they can define certain patterns or trends they would like to identify across the global metabolic network. Figure @fig:overview provides a graphical abstract to illustrate <i>Metaboverse's</i> role in the exploratory data analysis of biological data in the context of metabolism.

![
  **Metaboverse conceptual overview.**
  Illustration comparing traditional metabolic data analysis methods and the holistic approaches that Metaboverse offers. Traditionally, when a scientist performs an -omics experiment, they tend to focus on a couple of features that are differentially regulated. Metaboverse inversely contextualizes the data across the metabolic network and identifies interesting regulatory patterns in the data.
](./content/figures/overview.png "Square image"){#fig:overview}

In order to provide a platform for the exploration of single or multi-omic metabolic data, we developed several computational features to aid in the aims discussed above. First, we developed a pattern search engine for the rapid and automated identification of patterns and trends in -omic data on the metabolic network. Conceptually, this search engine borrows principles of topological motif searching from graph theory [@doi:10.1126/science.1089167; @doi:10.1038/ng881] and builds upon the concept of "activity motifs" [@doi:10.1038/nbt.1499]. Another feature introduced in Metaboverse allows for the interactive exploration of specific reactions or reaction entities with on-the-fly pattern search analysis. Users can explore specific pathways of interest and look for other interesting patterns and trends in pathways of interest. Perturbations in the abundance or behavior of a particular metabolic network component can lead to downstream genotypic and phenotypic modulations in a biological system. We include an interactive perturbation connectivity module to allow users to explore the effects of perturbations on their system. Finally, we tackle the challenge of sparsity, particularly in metabolomics datasets, by introducing a reaction collapsing or bridging feature that allows for searching for motifs across multiple reactions, where intermediate steps of the reaction trajectory may not have measured values for their respective input or output components.

Metaboverse is designed to handle standard two-condition experiments, flux metabolomics (in progress), and time-course experiments (in progress). Time-course inputs can be single-omics, or static RNA-seq and/or proteomics with multiple metabolomic time-points. Users input fold change and statistical measures from their respective -omics, and Metaboverse reconciles the inputs for layering on the metabolic network. Metaboverse can handle data from a variety of model organisms, including humans, mouse, yeast, zebrafish, and more. The foundational curation of Metaboverse is built on the Reactome curations of metabolism, so any of the 90+ species available on that platform are also available within the Metaboverse environment. In order to validate these methodologies available in Metaboverse we analyzed two-condition, flux metabolomics, and time-course datasets and provide vignettes that highlight <i>Metaboverse's</i> reliability in extracting canonical features, as well as novel features and patterns, from well-defined biological models. We outline the technical specs for computational biologists in the methods section, and the biological utilities in the main text for wet bench biologists. We intend that Metaboverse will be foundational in our ability to more deeply and holistically explore metabolism and aid in our ability to provide more context within metabolic models.


## Results

### Metaboverse is a dynamic, user-friendly tool for the exploration of high-throughput biological data in organism-specific pathways.

#### Overview.
We designed Metaboverse as a light-weight, self-contained app for the dynamic exploration of high-throughput biological data. The pathway curations are derived from Reactome, and as of writing, is capable of analyzing data for ## species. A user begins by providing a previously curated Metaboverse file, or the desired output location for a new curation, and selecting their organism of interest. Next, the user provides the relevant gene, protein, and/or metabolite datasets they would like layered onto the global reaction network of their organism of interest. These data categories can be extended to any dataset that uses the relevant mapping IDs; for example, one could provide ribosome profiling translation efficiency values mapped to the appropriate gene IDs for layering onto the network and downstream analysis. During this step, the user will also specify a few experimental parameters for consideration during downstream analysis and visualization. Following these user inputs, the organism's network, data processing, and motif analysis (discussed further below) is curated and a curation file is output for future analysis (see Figure @fig:package_overview).

![
  **Metaboverse package overview.**
  Illustration comparing the data input, processing, and exploration steps of the Metaboverse package.
](./content/figures/package_overview.png "Square image"){#fig:package_overview}

#### Handling data sparsity within the biological global network.
Missing data points, particularly in metabolomics experiments, are frequent and can make analysis of pathways and identification of regulatory patterns in the network challenging.  While thousands of metabolites are known to participate in human metabolism, the current state of the technology for determining which mass spectra belong to which metabolite can be challenging and often results in a limited number of data points being quantified. These can lead to gaps in the metabolic network which can be challenging to explore and analyze. We therefore developed a reaction compression algorithm (detailed more in the Methods section) that collapses up to three reactions with missing data points if they can be bridged with known data on the distal ends of the reaction path. These reactions, or pseudo-reactions are visually distinct during visualization of the network and allow the user to quickly identify interesting patterns in the network, learn what that pseudo-reaction was summarizing, and generate additional hypotheses based on the available information and lack of information. We found that inclusion of these pseudo-reactions in the reaction motif analysis (detailed below), aiding in identifying additional regulatory motifs that would have been missed based on the data sparsity of the measured metabolites from a dataset (see Vignette #1 below).

#### Rapid identification of interesting regulatory patterns in the reaction network.
Following network curation, the user can visualize available reaction motifs identified across the global reaction network. In a computational science context, a motif is simply a reoccurring pattern in network structure, or the organization of network entities and their relationships to one another. However, with -omic data, we are more interested in identifying patterns in expression or abundance of genes, proteins, and metabolites. Previous work by Checkik, et. al. introduced the concept of "activity motifs", where instead of identifying motifs based on network structure, they were identified using the expression characteristics of nodes in transcription factor binding signaling networks [@doi:10.1038/nbt.1499]. We  adapted this methodology to search and interactively display interesting regulatory patterns within the global metabolic network. For example, at a reaction the input may be high and the output low, indicating a regulatory event occurring at that reaction.

In Metaboverse, we define a motif as a regulatory pattern identified across a reaction or pseudo-reaction. Metaboverse contains a library of default motifs to search the network for, and users can define custom motifs they would like to identify across the global network. Metaboverse will search the global network from a pre-defined library of regulatory patterns (or motifs) and return a graphical stamp view of conserved patterns. These motifs can be ordered by strength of the motif from a magnitude of change perspective, or can be ordered based on the associated statistical values from measured components of the reaction. Input data for each -omics type requires associated statistical values associated with each measurement for a measured entity, which are used to weight motifs and prioritize returned results. We use a three-tiered sorting strategy when sorting by the associated statistical values. The highest prioritized motifs are those where the relevant components on either side of the reaction (inputs vs. outputs) that determined the reaction motif are statistically significant. Of these motifs from the first tier, motifs are sorted by lowest to highest cumulative p-value or other relevant statistical value. In the second sorting tier, reactions where at least one side of the reaction had a statistically significant motif component are sorted by statistical strength. Finally, all other motifs are sorted by the cumulative statistical value for the motif components.

For a given pattern, the user can then explore each pathway this particular motif is found in. Motif analysis of the global regulatory network will allow users to rapidly identify interesting features in the data, particularly patterns between canonical pathways or in other pathways that may not be an initial focus in their research. In the data vignettes below, we demonstrate this utility further. Users will also be able to design their own patterns through an interactive pattern drawing tool, and even design specific scenarios that are cognizant of feature type (in progress). For example, one might be interested in a pattern where a protein displays higher expression, but the resulting metabolite is decreased. This could then be coded interactively into the Metaboverse framework by the user.

#### Dynamic visualization of organism-specific reaction pathways.
Following curation of the global network as described above, the user can manually search individual canonical pathways or individual entities and their reaction neighborhoods. For a given selection, all relevant reactions that are annotated as a part of that pathway will be graphed, along with their core input (reactant) and output (product) components. In addition to these core elements, known catalysts and inhibitors are included, as well as the component proteins, genes, and metabolites known to form a functional complex as part of a reaction. Labels can be toggled on or off in the display, and the user can switch between viewing the values or statistics associated with each data point with their relevant color mapping. In cases where a gene value is known, but its protein value is unmeasured, the protein value will be inferred using aggregated gene component values. The same is then done for functional complexes using their inferred or known component values. Relevant pathway and analytical metadata is also displayed. Other information, such as identified motifs found in the pathway can also be found and expanded for further exploration in a new window. Aids for visualization are also available, such as the ability to remove nodes from visualization that contain a high number of relationships to other network features such as that these nodes, which act as hubs in the network, do not lead to cluttered representations of the network. Often, these hub nodes are ubiquitous features such as water and proton which may be of limited interest to the user during data visualization. Compartment domains are also graphed to include a relevant reactions and their components that occur in a given cellular compartment.

#### Visualization of downstream effects of network perturbations.
Users may be interested a particular metabolite or protein and the downstream effects its perturbation has on related pathways. By double-clicking a node of interest, or by selecting the entity name from the drop-down menu, the user can explore all downstream effects across all pathways in the global network. The user can also define how many neighborhoods to display such that one can visualize two or more reaction steps downstream of the selected entity. This functionality moves the analysis away from our traditional, strictly defined pathway approach to analysis, and helps contextualize the far-reaching effects changes in metabolism or other biological systems can have across classical pathways.

#### Exploring perturbation connectivity within the global network
Abundance or behavioral changes of a metabolic network component can lead to downstream genotypic and phenotypic modulations in a biological system. One important measure of robustness of a network is "connectivity". In a biological context, an example of connectivity, or the loss of network connectivity, is easily grasped when considering a transport reaction from the cytosol into the mitochondria of a critical metabolite [@doi:10.1186/1756-0381-4-10; @doi:10.1093/gigascience/giz137; @doi:10.1007/s41109-019-0129-0; @doi:10.1371/journal.pone.0087075]. When the transport hub is abolished and network connectivity is lost, the critical metabolite cannot participate in the required downstream reactions. For example, an example from our laboratory established the consequences of the ablation of the mitochondrial pyruvate carrier on downstream citric acid cycle processes and the corresponding increase in lactate production [@doi:10.1126/science.1218099] and leads to serious cellular complications and dysfunction [@doi:10.1038/ncb3593; @doi:10.1016/j.cmet.2019.11.002].

The importance of connectivity could also be considered in a treatment context. For example, a druggable and critical metabolite may be perturbed in a particular disease context. However, if a metabolite participating in a neighboring, downstream reaction is also perturbed in a way not related to the perturbation of the first metabolite, the efficacy of the drug treatment could be severely impaired [@doi:10.1158/0008-5472.CAN-14-3256; @doi:10.1126/science.1132939; @doi:10.1186/s12918-018-0674-7]. To aid in exploration of the connectivity of the biological network, we also developed a connectivity module where users can display all reactions that have at least one involved component perturbed based on either an abundance or statistical level. By doing so, when the graph is constructed, proximal reactions that were perturbed independently will be "sewn" together to reconstruct a perturbation connectivity map in the user's model.

### Data vignettes
In order to demonstrate the added utility of Metaboverse to the community that is not currently available in other tools, we used Metaboverse to analyze a series of public and new datasets. From the vignettes provided below, we show that Metaboverse not only is able to identify points of interest previously described or expected, but can rapidly identify for the user unexpected and systematic regulatory patterns in a reaction network context.

#### 1. Perturbation of mitochondrial fatty acid synthesis across time reveals expected and unexpected reaction motifs.
Mitochondrial fatty acid synthesis (mtFAS) acts as an important metabolic pathway long known to function to produce lipoic acid, a critical cofactor for several metabolic enzymes. Recent work has begun to uncover additional, important roles for this pathway. For example, we now know that mtFAS can perform metabolic nutrient sensing roles to coordinate lipoic acid synthesis with iron sulfur (FeS) cluster biogenesis, assembly of oxidative phosphorylation complexes, and more [@doi:10.1016/j.cub.2018.08.022; @doi:10.7554/eLife.17828]. Additionally, this pathway has received increased physiological focus with the discovery of patients with mutations in key mtFAS enzymes [@doi:10.1016/j.ajhg.2016.09.021].

<i>MCAT</i>, or <i>MCT1</i>in <i>Saccharomyces cerevisiae</i>, is an acyltransferase responsible for the transfer of a malonyl group from malonyl-CoA to <i>NDUFAB1</i>, the mitochondrial acyl carrier protein. By knocking out this gene, one can simulate the effects of a disruption in mtFAS.

In order to probe the relationship between mtFAS-related protein concentration and the effects of its perturbation on downstream metabolic processes from a systematic perspective, we used a <i>mct1&Delta;</i> model in <i>Saccharomyces cerevisiae</i> to measure steady state proteomics and transcriptomics at 12 hours after a shift to a non-fermentable carbon source, as well as steady state metabolomics at 0, 15, 30, 60, and 180 minutes after this shift in carbon source. By layering these data onto the <i>Saccharomyces cerevisiae</i> metabolic network using Metaboverse, we observed interesting respiratory signatures as expected based on our previous work [@doi:10.1016/j.cub.2018.08.022; @doi:10.7554/eLife.17828]. For example, using Metaboverse, we noticed a strong pattern in the electron transfer from ubiquinol to cytochrome C of complex III of the electron transport chain (ETC) (Figure @fig:mct1_vignette A). At the proteomics level, cytochrome C component proteins, CYC1 and CYC7 are both significantly reduced in concentration compared to wild-type cells (log<sub>2</sub>(fold change): -1.57 & -0.88; p-value: < 0.01 & < 0.01; respectively). This reduction in cytochrome C concentration is paired with a marked reduction in concentration of the protein components of cytochrome C reductase, which is a catalyst of this electron transfer reaction (average log<sub>2</sub>(fold change) of all measured protein components = -2.03, where 9/11 component proteins were measured. Range of log<sub>2</sub>(fold change) values: -0.34 to -3.21; all p-values below 0.01).   

![
  **Metaboverse identifies several reaction motifs of interest in <i>mct1&Delta;</i> cells.**
  (A) (B) (C) . All panels shown used the 180 min. metabolomics values for node shading.
](./content/figures/fig_mct1.png "Square image"){#fig:mct1_vignette}

A second pattern of interest that we expect in this model is the conversion of Succinate to Fumarate by the Succinate dehydrogenase complex (SDH, or Complex II of the ETC) (Figure @fig:mct1_vignette B). We know from previous work that complex assembly and mtFAS are intricately connected [@doi:10.1016/j.cub.2018.08.022; @doi:10.1101/2020.05.09.086199]. However, this particular behavior when pairing the temporal metabolomics data with the steady-state proteomics data is interesting and acts as a potential jumping-off point for further follow up experimentation. Across each time point, we see a steady accumulation of fumarate (log<sub>2</sub>(fold change) >= 1). We pair this with the proteomics data and observe a strong reduction in both SDH and FUM1, which encodes the fumarase needed to convert fumurate to malate in the TCA cycle (-0.49 to -2.96). It is possible that the reduction of FUM1 and build-up of fumurate is acting as a bottleneck and signaling a reduction in Complex II component production and assembly. However, as measurements for succinate and malate are missing, it is difficult to clarify this regulation more without further follow-up experiments. An additional hypothesis may involve SFC1, the mitochondrial succinate-fumarate transporter, which we previously noticed from the analysis of the proteomics data was reduced in concentration 2.5-fold. Unfornately, at this time this transport reaction is not annotated in the Reactome database for <i>Saccharomyces cerevisiae</i>, which raises an important goal for the Metaboverse project, which is to augment these pathway representations to fill in the gaps of knowledge using additional sources. However, with the prior knowledge, it is interested to notice this patten with fumarate as the build-up of fumarate may reflect the inability of the mitochondria to export fumarate.

A final observation of interest from analysis through Metaboverse is that of citrate and isocitate. Normally, the TCA cycle generates citrate from malate to oxaloacetate via MDH1, then oxaloacetate to citrate via CIT1 and CIT3. Building off the observations discussed above, we expect lower levels of malate as due to decreased MDH1. We also observe lower levels of CIT1 (-1.46) and reciprocal decreases in citrate that worsens across the time-course. However, at 30 minutes post-carbon source shift, isocitrate levels are decreased by -1.38 log<sub>2</sub>(fold change) (p-value < 0.01). By 60 and 180 minutes, there is no significant change in isocitrate levels compared to wild-type cells, while citrate levels remain significantly reduced (Figure @fig:mct1_vignette C). Does this indicate some sort of adaptation to a respiratory-required environment with ETC-impaired cells?

By analyzing this multi-omics dataset using reaction motif analysis and other interactive visualization, interesting questions arise. We see several reaction motifs that are expected based on prior knowledge of this biological model, as well as other interesting behaviors worthy of further follow-up. This demonstrates the potential Metaboverse has to act as a valuable hypothesis-generation tool, as well as a convenient platform for visualization and analysis of a user's dataset in the context of the metabolic or other reaction networks.

#### 2. Flux data (in progress)


#### 3. Previously published data (in progress)


## Discussion

In this manuscript, we introduce a new software tool for analysis and exploration of user data layered on the metabolic and global reaction networks. To improve on previous tools with similar capabilities, we introduced several new analytical tools and methods to aid users in the automated identification and discovery of regulatory patterns within their data in a reaction network context. These include the automated ability to identify reaction motifs across the global reaction network, such as a reaction where an input is low abundance and an output is high. Metaboverse also provides dynamic and interactive visualization capabilities to search for patterns and features within the user data on a reaction network within classical pathways. If a user is interested in how a reaction motif is propagating across the global reaction network and not just a single pathway, a user can explore a reaction component's nearest reaction neighborhood. The user can also explore the connectedness of perturbations across the global network and begin to explore hypotheses of the role of redundancy within a biological phenomenon.

In order to handle the challenge of sparsity, particularly in regard to metabolomics data and the metabolic reaction network, we introduce a reaction collapsing feature which summarizing a series of connected reaction where values may be missing for a number of reactions, but where the terminal ends of the reaction path have measured values. Importantly, this augments the capabilities available within Metaboverse, especially in the identification of additional reaction motifs that may be of interest to the user.  

We demonstrated the utility of Metaboverse in exploring single- and multi-omic datasets. We analyzed previously published studies from a variety of organisms (in progress), as well as generated a novel dataset that highlights the time-course capabilities of this framework.

While Metaboverse aims to enhance the computational toolkit for data analysis and hypothesis generation in metabolic and other experiments, a number of challenges still remain, which we intend to address as we continue to maintain and build upon this software. For example, while the reaction collapsing features of Metaboverse aid in identifying patterns across several reactions where data may be missing, there are a variety of biological and technical edge cases that need to be considered in future implementations of this feature. This is particularly challenging in datasets where few metabolites were measured. Hopefully, as technical limitations in metabolomics are also overcome, more complete snapshots of metabolism will be visible within this framework. Additionally, while we take a more straightforward and somewhat rudimentary approach to statistical significance integration in the reaction motif searches, more holistic platforms for cross-omics integration are needed and remain a consequential challenge in multi-omics research.

In summary, we hope that Metaboverse will bring a new perspective to users' data. We envision Metaboverse to be a staple tool in the metabolic research toolkit that will help researchers critically and holistically consider their data in the context of biological network interactions and help draw the connections needed to aid them in extracting new and exciting hypotheses from their data that would be difficult to do without this tool.


## Methods
A tutorial for how to use Metaboverse can be found at metaboverse.readthedocs.io/getting-started.

### 1. Network Curation
Biological networks are curated using the current version of the Reactome database. In particular, the pathway records for each species, complex component and interaction data, Ensembl, and UniProt Reactome mapping tables are integrated into the network database for Metaboverse. Additionally, the ChEBI database names table (ftp://ftp.ebi.ac.uk/pub/databases/chebi/Flat_file_tab_delimited/names.tsv.gz) is integrated. These data are used to generate a series of mapping dictionaries for entities to reactions and reactions to pathways for curation of the global network.

After the relevant information is parsed from each table or record, the global network is propagated using the NetworkX networking framework [cite:networkx] to generate nodes for each reaction and reaction component, and edges connecting components to the appropriate reactions. In some cases, a separate ID is used to generate two nodes for the same metabolite within two separate compartments to aid in visualization downstream; however, user data for the given entity would be properly mapped to both nodes.

After the network is curated for the user-specified organism, each node's degree (or magnitude of edges or connections) is determined to aid in the user's downstream ability to avoid visualizing high-degree components, such as a proton or water, on the metabolic network, which can lead to graphical entanglement and cluttering and a decrease in computational performance [cite:Waller;GigaScience;2020].

### 2. Data overlay and broadcasting for missing entities
In order to overlay user data on the global network, first, user-provided gene expression, protein abundance, and/or metabolite abundances' names are mapped to Metaboverse compatible identifiers. For components that Metaboverse is unable to map, a list will be returned to the user so they can provide alternative names to aid in mapping. Second, provided data values are mapped to the appropriate nodes in the network. In cases where gene  expression data is available, but protein abundance data is missing, Metaboverse will take the average (or user-defined??) of the available gene expression values to broadcast to the protein node. For complexes, all available component values (metabolites, proteins, etc.) are averaged (or user-defined??). Nodes for which values were inferred will be marked by a dashed border during visualization to clearly show which values are known and which were inferred.

### 3. Collapsing reactions with missing expression or abundance user data
After data mapping is complete, Metaboverse will generate a collapsed network representation for optional viewing during later visualization. We did, however, choose to enforce a limit of up to three reactions that can be collapsed as data down a pathway should only be inferred so far. We also enforced certain parameters for reaction collapse as follows:   

1. If a reaction has at least one known or inferred value for inputs (reactants) and one known or inferred value for outputs (products), the reaction will be left as is. During the entire reaction collapse step, known catalysts are included when assessing whether a reaction has measured output values (more of a catalyst should lead to more output in most cases) and inhibitors are included when assessing whether the reaction has measured input values (more inhibitor should lead to accumulation of input in most cases). Catalysts and inhibitors are not included when determining reaction neighbors as described below.   

2. If a reaction has at least one known input, the input is left as is, and each reaction that shares the same input with the assessed reaction inputs are determined whether they have a measured output. If the neighbor reaction does not contain an known output value, the reaction is left as is. If the neighbor reaction does contain a measured output, the original reaction's inputs and the neighbor reactions outputs are collapsed to form a single, pseudo-reaction between the two. If the reaction has at least one known output, the inverse is performed where neighbors with identical components as the reactions inputs are assessed for whether a collapsed reaction can be created.   

3. If a reaction has no measured values, it is determined if the neighboring reactions on both sides (one sharing the reaction's inputs and other sharing the reaction's outputs) have measured values. If both neighbors contain a measured value, a collapsed pseudo-reaction is created summarizing all three reactions.

For pseudo-reactions, appropriate notes are included to describe the collapse. During visualization, these pseudo-reactions are marked by black dashed edges and dashed node borders. A graphical representation of how this reaction collapse is performed can be found in Figure @fig:collapse_schematic.

![
  **Reaction node collapse schematic.**
  (a) For reactions where at least one input and at least one output component contain a measured value from the user data, the reaction will be maintained as is. (b) Where an input of a reaction is known but no output has a known value, Metaboverse will search for all neighboring reactions that contain identical inputs. If the neighboring reaction has a known output value, the two reactions will be merged into one pseudo-reaction. (c) Where an output of a reaction is known but no input has a known value, Metaboverse will search for all neighboring reactions that contain identical outputs. If the neighboring reaction has a known input value, the two reactions will be merged into one pseudo-reaction. (d) For reactions with no known values, neighbor pairs that match the inputs and outputs of the considered reaction will be evaluated for whether their respective outputs and inputs both have known values. If values are known for both neighbors, the three reactions will be merged into one pseudo-reaction. (e) As in (d), but if one neighbor does not contain a value, the one does contain a value, no reaction merging will be performed. (f) As in (d), but if neither neighbors contain known values, no reaction merging will be performed. An asterisk (*) indicates the target reaction being considered for a given reaction collapse. A red node indicates a reaction input or output with a measured value. A white node indicates a reaction input or output with no measured value. A grey node indicates a reaction. A grey node with a dashed border indicates a pseudo-reaction. A solid edge indicates a known relationship. A dashed edge indicates a relationship inferred via reaction merging.
](./content/figures/collapse_schematic.png "Square image"){#fig:collapse_schematic}

### 4. Regulatory pattern (motif) searches




### 5. Nearest neighborhood searches
In order to visualize all global connections, a user can select an entity (a gene, protein, or metabolite) and visualize all reactions that the component is involved in. By doing so, the user can visualize other downstream effects a change of one entity might have across the global network, which consequently aids in bridging and identifying any motifs that may occur between canonically annotated pathways. These neighborhoods can be expanded to view multiple downstream reaction steps and their accompanying genes, proteins, and metabolites by modulating the appropriate user option in the app.

Users can also limit which entities are shown by enforcing a degree threshold. By setting this value at 50, for example, the graph would not show nodes that have 50 or more connections. One caveat, however, is that this will occasionally break synchronous pathways into multiple pieces if one of these high-degree nodes was the bridge between two sides of a pathway.

### 6. Perturbation connectivity
Perturbation connectivity networks are generated by searching each reaction in the global network for any reaction where at least one component is significantly perturbed. Users can modify the necessary criteria to base the search on the expression or abundance value or the statistical value, and can choose the thresholding value to be used. For the expression thresholding, the provided value is assumed to be the absolute value, so a thresholding value of 3 would include any reactions where at least one component, showed a greater than 3 measured change or less than -3 measured change, the value of which is dependent on the data provided by the user, thus could represent log<sub>2</sub> fold changes, z-scores, or any other unit appropriate the biological context.

Once a list of perturbed reactions is collected, the network is constructed included each of these reactions and their components. Perturbed neighboring reactions that share components are thus connected within the graph and perturbed reactions that are not next to other perturbed reactions are shown as disconnected sub-graphs.

### 7. Network visualization and exploration
#### 7.1 Dynamic network plotting
Users interact with Metaboverse through an interactive app interface. The app uses Electron, a cross-platform app framework that uses JavaScript, HTML, and CSS to design the interface. Metaboverse thus comes packaged as a single executable app with all necessary dependencies included for running on Linux, MacOS, and Windows.

Interactive graphing is handled using the D3 and JQuery JavaScript libraries. Force-directed graphs are constructed by taking the user selection for a pathway or entity and determining the reactions that are components of that pathway. All inputs, outputs, modifiers, and other components of these reactions, along with edges where both source and target are found in the sub-graph as nodes, are included and plotted. Relevant metadata, such as user-provided data and reaction descriptions, can be accessed by the user in real time. Metadata for categorical displays, such as edge or node type, are extracted from the metadata during graphing of the sub-network.

Some performance optimization features are included by default to prevent computational overload. For example, nearest neighbor sub-graphs with more than 1500 nodes, or nodes with more than 500 edges will not be plotted as plotting of this information in real-time is computationally prohibitive.

#### 7.2 Visualizing pathways and super-pathways
In order to visualize a pathway, a user selects their pathway of choice and all component reactions and their reactants, products, modifiers, and metadata are parsed from the global network. Super-pathways help categorize these pathways and are defined as any pathway containing more than 200 nodes.

#### 7.3 Visualizing compartments
Compartments are derived from Reactome annotations. Compartment visualizations are generated using D3's hull plotting feature. Compartment boundaries are definde at the reaction levels and made to encompass each reaction's reactants, products, and modifiers for that given compartment.

#### 7.4 Annotations
Annotations for each reaction are derived from the Reactome database. Pseudo-reactions annotations do not include this information; instead they include notes on which reactions were collapsed to create the selected pseudo-reaction. All inferred pseudo-reactions and protein or complex values are displayed with dashed edges to differentiation from measured values.

#### 7.6 Additional features
While Metaboverse will continue to undergo development and new features will be added, we will briefly highlight some additional features available at time of publication. We encourage users to check the documentation for more current updates and information regarding use of Metaboverse [docs].

##### 7.6a Toggle genes
As gene components can crowd the graph space, users can toggle gene display on and off using the appropriate button. The graph is then refreshed to either include or ignore gene components based on their node meta-tag.

##### 7.6b Toggling values
Users can switch between coloring nodes based ono the value or statistic provided by toggling the appropriate button. Colorbar information for the dataset is saved in the graph metadata during curation and used to generate a colorbar. The colorbar for statistics is represented using a -log<sub>10</sub> scale for a statistic value originally ranging between 0 and 1.

##### 7.6c Toggling features/labels
By default, reaction and feature labels are displayed by hovering the mouse over the node. Reaction or feature nodes can have the labels statically displayed by selecting the appropriate button. An event watch function is used to watch for this user selection and update the display of the node labels.

##### 7.6d Toggling collapsed reactions
By selecting the appropriate button, users can toggle between displaying a full or collapsed pathway representation of the sub-network. By selecting this button, the graph is refreshed using the appropriate reaction dictionary, where for graphing of the collapsed representation, a reaction with available pseudo-reactions substituted for the original reactions are included for graph propagation.

##### 7.6e View curated pathway image
While Metaboverse graphs networks dynamically, users may be more familiar or comfortable with classical, curated pathway layouts when exploring their data. For a given pathway graph, the user can select the appropriate button and Metaboverse will open a new window with the Reactome curated pathway layout.

##### 7.6f Saving graphs
Users can generate a PNG output file for any network created in Metaboverse by selecting the appropriate button.

##### 7.6g Nearest neighbor and hub thresholding
The number of nearest neighbors to graph, or the limit to number of edges a graphed node can have, can be modulated by the user using the appropriate input spaces. When graphing a nearest neighbors network, Metaboverse will recursively fetch related reactions and their neighbors until a node display threshold is reached. This allows the user to visualize downstream effects of a change that may propagate across several reactions. The hub threshold option prevents plotting of nodes with more than the specified number of edges. This is handling during graphing by excluding any entity nodes that meet this criteria as the neighborhood is propagated. This is particularly useful in removing hub nodes, such as water or protons, which may be less relevant to the user experience and can quickly clutter the graph. This feature can also help plot more extensive neighborhoods, as often neighborhoods quickly link to high-degree nodes, such as water, and limit graphing ability.

##### 7.6h Metadata display
To help inform the user of selection information and relevant metadata, a space in the legend bar during visualization is reserved for spaces where this information can be displayed, which is updated based on the user's input as it is provided.

### 8. Packaging
The Metaboverse app is packaged using Electron. Back-end network curation and data processing is performed using Python and the NetworkX library. Front-end visualization is performed using Javascript and relies on the D3 and JQuery packages. Saving network representations to a PNG file is performed using the d3-save-svg and string-pixel-width packages (Table @tbl:dependencies). Documentation for Metaboverse is found at metaboverse.readthedocs.io. Continuous integration services are performed by Travis CI to routinely run test cases for each change made to the Metaboverse architecture. The Metaboverse source code can be accessed at https://github.com/Metaboverse/metaboverse. The code used to draft and revise this manuscript, as well as all associated scripts used to generate and visualize the data presented in this manuscript can be accessed at https://github.come/Metaboverse/manuscript.

| Name               | Reference                              |
|--------------------|----------------------------------------|
| HTML               | N/A                                    |
| CSS                | N/A                                    |
| Javascript         | N/A                                    |
| Electron           | [@url:https://electronjs.org]      |
| JQuery             | [@url:https://jquery.com]          |
| D3                 | [@url:https://d3js.org]            |
| string-pixel-width | [@url:https://github.com/adambisek/string-pixel-width]               |
| d3-save-svg        | [@url:https://github.com/edeno/d3-save-svg]   |
| Python             | [@url:https://www.python.org/]            |
| pandas             | [@doi:10.5281/zenodo.3509134; @doi:10.25080/Majora-92bf1922-00a]            |
| numpy              |  [@url:https://web.mit.edu/dvp/Public/numpybook.pdf]           |
| scipy              |  [@doi:10.1038/s41592-019-0686-2]           |
| matplotlib         |  [@doi:10.1109/MCSE.2007.55]           |
| NetworkX           |  [@url:http://conference.scipy.org/proceedings/SciPy2008/paper_2/full_text.pdf]           |

Table: Dependencies table. {#tbl:dependencies}

### 9. Validation using biological data

#### 9.1 <i>mct1</i> perturbation in <i>Saccharomyces cerevisiae</i>

##### Yeast Strains

<i>Saccharomyces cerevisiae</i> BY4743 (MATa/&Alpha;, his3/his3, leu2/leu2, ura3/ura3, met15/MET15, lys2/LYS2) was used to generate the mct1&Delta; strain as described in [@doi:10.1016/j.molcel.2018.06.039].

##### RNA-sequencing sample preparation

RNA sequencing data were generated by growing <i>Saccharomyces cerevisiae</i> biological replicates for strains <i>mct1&Delta;</i> (n=4) and wild-type (n=4). Briefly, cells were grown in glucose and switched to raffinose-supplemented growth medium for 0, 3, and 12 hours such that at time of harvest, cultures were at OD<sub>600</sub>=1. Cultures were flash frozen and later total RNA was isolated using the Direct-zol kit (Zymo Research) with on-column DNase digestion and water elution. Sequencing libraries were prepared by purifying intact poly(A) RNA from total RNA samples (100-500 ng) with oligo(dT) magnetic beads and stranded mRNA sequencing libraries were prepared as described using the Illumina TruSeq Stranded mRNA Library Preparation Kit (RS-122-2101, RS-122-2102). Purified libraries were qualified on an Agilent Technologies 2200 TapeStation using a D1000 ScreenTape assay (cat# 5067-5582 and 5067-5583). The molarity of adapter-modified molecules was defined by quantitative PCR using the Kapa Biosystems Kapa Library Quant Kit (cat#KK4824). Individual libraries were normalized to 5 nM and equal volumes were pooled in preparation for Illumina sequence analysis. Sequencing libraries (25 pM) were chemically denatured and applied to an Illumina HiSeq v4 single read flow cell using an Illumina cBot. Hybridized molecules were clonally amplified and annealed to sequencing primers with reagents from an Illumina HiSeq SR Cluster Kit v4-cBot (GD-401-4001).  Following transfer of the flowcell to an Illumina HiSeq 2500 instrument (HCSv2.2.38 and RTA v1.18.61), a 50 cycle single-read sequence run was performed using HiSeq SBS Kit v4 sequencing reagents (FC-401-4002).

##### Sequence analysis

Sequence FASTQ files were processed using XPRESSpipe [@doi:10.1371/journal.pcbi.1007625]. Batch and log files are available at [@url:https://github.com/Metaboverse/manuscript/tree/master/data/sce_mct1]. Notably, reads were trimmed of adapters (Read1: AGATCGGAAGAGCACACGTCTGAACTCCAGTCA, Read2: AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT). Differential expression analysis was performed using DESeq2 [@doi:10.1186/s13059-014-0550-8] by comparing <i>mct1&Delta;</i> samples with wild-type samples at the 12-hour time-point to match the steady state proteomics data. log<sub>2</sub>(fold change) and false disovery rate ("p-adj") values were extracted from the DESeq2 output.

##### Proteomics analysis

Steady state quantitative proteomics data were generated as described in [@doi:10.1016/j.molcel.2018.06.039]. Briefly, cells were grown in glucose and switched to raffinose-supplemented growth medium overnight, and harvested at mid-log phase. For this analysis, we compared the <i>mct1&Delta;</i> (n=3) with the wild-type (n=3) cell populations. log<sub>2</sub>(fold change) values and p-values were generated by comparing <i>mct1&Delta;</i> with the wild-type cells. p-values were generated using a 2-tailed Student's T-test.

##### Metabolomics sample preparation

Metabolomics data were generated by growing the appropriate yeast strains in synthetic minimal media (S-min) supplemented with 2% glucose until they reached OD<sub>600</sub> between 0.6-0.8. Cells were then transfered to S-min media containing 2% raffinose and harvested after 0, 15, 30, 60, and 180 minutes (n=6/time-point/strain).

##### Metabolite extraction

A 75% boiling ethanol (EtOH) solution containing the internal standard d4-succinic acid (Sigma 293075) was then added to each sample. Boiling samples were vortexed and incubated at 90°C for 5 min. Samples were then incubated at -20 ˚C for 1 hr. After incubation, samples were centrifuged at 5,000 x g for 10 minutes at 4˚C. The supernatant was then transferred from each sample tube into a labeled, fresh 13x100mm glass culture tube. A second standard was then added (d27-myristic acid CDN Isotopes: D-1711). Pooled quality control samples were made by removing a fraction of collected supernatant from each sample and process blanks were made using only extraction solvent and no cell culture. The samples were then dried en vacuo. This process was completed in three separate batches.

##### Mass Spectrometry Analysis of Samples

All GC-MS analysis was performed with an Agilent 5977b GC-MS MSD-HES and an Agilent 7693A automatic liquid sampler. Dried samples were suspended in 40 µL of a 40 mg/mL O-methoxylamine hydrochloride (MOX) (MP Bio #155405) in dry pyridine (EMD Millipore #PX2012-7) and incubated for one hour at 37 °C in a sand bath. 25 µL of this solution was added to auto sampler vials. 60 µL of N-methyl-N-trimethylsilyltrifluoracetamide (MSTFA with 1%TMCS, Thermo #TS48913) was added automatically via the auto sampler and incubated for 30 minutes at 37 °C. After incubation, samples were vortexed and 1 µL of the prepared sample was injected into the gas chromatograph inlet in the split mode with the inlet temperature held at 250°C. A 10:1 split ratio was used for analysis of the majority of metabolites. For those metabolites that saturated the instrument at the 10:1 split concentration, a split of 50:1 was used for analysis. The gas chromatograph had an initial temperature of 60°C for one minute followed by a 10°C/min ramp to 325°C and a hold time of 5 minutes. A 30-meter Phenomenex Zebron AB-5HT with 5m inert Guardian capillary column was employed for chromatographic separation. Helium was used as the carrier gas at a rate of 1 mL/min. Figure @fig:mass_spec_deriv demonstrates an example of the two-step derivatization process used to convert non-volatile metabolites to a volatile form amenable to GC-MS.

![
  **Mass Spectrometry derivatization process.**
  This figure demonstrates an example of the two-step derivatization process used to convert non-volatile metabolites to a volatile form amenable to GC-MS. Pyruvic acid is used here as an example.
](./content/figures/mass_spec_deriv.png "Square image"){#fig:mass_spec_deriv}

##### Analysis of Mass Spectrometry Data

Data was collected using MassHunter software (Agilent). Metabolites were identified and their peak area was recorded using MassHunter Quant. This data was transferred to an Excel spread sheet (Microsoft, Redmond WA). Metabolite identity was established using a combination of an in-house metabolite library developed using pure purchased standards, the NIST library and the Fiehn library. There are a few reasons a specific metabolite may not be observable through GC-MS. The metabolite may not be amenable to GC-MS due to its size, or a quaternary amine such as carnitine, or simply because it does not ionize well. Metabolites that do not ionize well include oxaloacetate, histidine and arginine. Cysteine can be observed depending on cellular conditions. It often forms disulfide bonds with proteins and is generally at a low concentration. Metabolites may not be quantifiable if they are only present in very low concentrations.

Resulting data from all samples were normalized to the internal standard d4-succinate. Samples highlighted in yellow were swapped with normalized data from the unsaturated run. The identity of each peak was ensured by visualization in Mass Hunter Qual and Quant. The data has also been roughly reordered by metabolic process. False positives were removed. All but the best representative of duplicate metabolites, which were created through variability in the derivatization process, were also removed.

### 10. Data availability.

Raw data produced for this study are in the process of being uploaded to the appropriate repositories. In the meantime, the raw data can be accessed at [@url:https://github.com/Metaboverse/manuscript/tree/master/data/sce_mct1].

The curated networks for these data are available at [@url:https://github.com/Metaboverse/manuscript/tree/master/data/sce_mct1]. Networks were generated by taking the 12-hour transcriptomics and proteomics datasets with their appropriate log<sub>2</sub>(fold change) and statistical values, along with the 0, 15, 30, 60, and 180 minute metabolomics datasets with their respective log<sub>2</sub>(fold change) and statistical values and layering these data on the <i>Saccharomyces cereviseae</i> global reaction network as curated by Metaboverse from the Reactome database. Reaction motifs and global connectivity analyses were performed within the Metaboverse platform.

The Metaboverse source code is available at [@url:https://github.com/Metaboverse/Metaboverse] and archived versions can be accessed at Zenodo [].

The source code and data for this manuscript and subsequent analyses is available at [@url:https://github.com/Metaboverse/manuscript] and archived versions can be accessed at Zenodo [].


## Acknowledgements

We thank Alex J. Bott, Ahmad A. Cluntun, Kevin Hicks, and other members of the Rutter lab for their thoughtful insights and suggestions. We thank the Brian Dalley and the University of Utah High-Throughput Genomics Core for help with RNA-sequencing library preparation. The support and resources from the Center for High-Performance Computing at the University of Utah are gratefully acknowledged.

## Funding

J.A.B. received support from the National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK) Inter-disciplinary Training Grant T32 Program in Computational Approaches to Diabetes and Metabolism Research, 1T32DK11096601 to Wendy W. Chapman and Simon J. Fisher (https://www.niddk.nih.gov/). This work was supported by NIDDK fellowship 1T32DK11096601 (to J.A.B.) (https://www.niddk.nih.gov/) and NIH grant R35GM13185 (to J.R.) (https://www.nih.gov/). The computational resources used were partially funded by the NIH Shared Instrumentation Grant 1S10OD021644-01A1 (https://www.nih.gov/). Mass spectrometry equipment was obtained through NCRR Shared Instrumentation Grant 1S10OD016232-01, 1S10OD018210-01A1, and 1S10OD021505-01. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.


## Contributions

* Conceptualization: J.A.B., T.C.W., B.W., J.R.
* Supervision: J.A.B., B.W., J.R.
* Project Administration: J.A.B.
* Investigation: J.A.B., T.C.W., Y.O., S.M.N., T.V.
* Formal Analysis: J.A.B.
* Software: J.A.B., Y.Z.
* Methodology: J.A.B., Y.Z.
* Validation: J.A.B.
* Data Curation: J.A.B., T.C.W.
* Resources: J.A.B., J.C., B.W., J.R.
* Funding Acquisition: J.A.B., J.C., B.W., J.R.
* Writing - Original Draft Preparation: J.A.B.
* Writing - Review & Editing: J.A.B., Y.Z., T.C.W., Y.O., S.N.M., T.V., J.C., B.W., J.R.
* Visualization: J.A.B.


## Supplementary Material {.page_break_before}


## References {.page_break_before}

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>
