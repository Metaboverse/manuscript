# Metaboverse manuscript

[![CC BY 4.0][cc-by-shield]][cc-by]
[![bioRxiv preprint](https://img.shields.io/badge/bioRxiv-10.1101%2F2020.06.25.171850-BF2636)](https://www.biorxiv.org/content/10.1101/2020.06.25.171850v1)
[![Github All Releases](https://img.shields.io/github/downloads/Metaboverse/Metaboverse/total.svg)]()
[![DOI](https://zenodo.org/badge/239609832.svg)](https://zenodo.org/badge/latestdoi/239609832)

These works are licensed under a Creative Commons Attribution 4.0 International License.

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

### Local execution

The easiest way to run Manubot is to use [continuous integration](#continuous-integration) to rebuild the manuscript when the content changes.
If you want to build a Manubot manuscript locally, install the [conda](https://conda.io) environment as described in [`build`](build).
Then, you can build the manuscript on POSIX systems by running the following commands from this root directory.

Installation:
```sh
conda env create --file environment.yml
```

```sh
# Activate the manubot conda environment (assumes conda version >= 4.4)
conda activate manubot

# Build the manuscript, saving outputs to the output directory
bash build/build.sh

# At this point, the HTML & PDF outputs will have been created. The remaining
# commands are for serving the webpage to view the HTML manuscript locally.
# This is required to view local images in the HTML output.

# Configure the webpage directory
manubot webpage

# You can now open the manuscript webpage/index.html in a web browser.
# Alternatively, open a local webserver at http://localhost:8000/ with the
# following commands.
cd webpage
python -m http.server
```

Sometimes it's helpful to monitor the content directory and automatically rebuild the manuscript when a change is detected.
The following command, while running, will trigger both the `build.sh` script and `manubot webpage` command upon content changes:

```sh
bash build/autobuild.sh
```

# Table of Contents
- 01.abstract.md: Abstract
- 02.introduction.md: Background information, introduction
- 03.results.md: Software description, validation
- 04.discussion.md: Summary, innovations, caveats, future directions
- 05.methods.md: Methods for software dev. and data production, curation, and analysis
- 06.acknowledgements.md: Acknowledgements and funding information
- 07.contributions.md: Authorship contributions (refer to https://github.com/akenall/Open-Contributorship-Badges/blob/master/Badge%20Files.md for more information)
- 08.supplment.md: Supplemental data, methods
- metadata.yaml: Author metadata (contact, initials, ORCID, affiliations, etc.)

# Revisions log:
## Draft 2 Changes
- For detailed changes, see files ending in `.md` at https://github.com/Metaboverse/manuscript/compare/413e2c1..b40c7d6

#### Abstract
- Minor spelling/phrasing changes

#### Introduction
- Added description of MetScape plug-in for Cytoscape in other tools comparison
- Added information about the size of the metabolic network and GC-MS coverage when discussing network sparsity
- Removed specification of flux integration and saving for when it is actually incorporated as to not confuse the reader as to what is currently available
- Minor spelling/phrasing changes
- Changed `desktop application` to `application`
- Added citations for network interconnectedness discussion

#### Results
- Added explanation of data input in `Overview`
- Added sentence explaining how our approach limits pathway-centric biases in analysis.
- Added Cohen's d effect size calculations to all values with a fold change
- Improved description of glutaminolysis in lung tumor analysis vignette

#### Discussion
- Future features list
  - Flux balance
  - Interactive motif designer
  - Integrate external QC tools
  - UpSet plots


#### Methods
- Updated mass spec methodology based on James' feedback
- Minor spelling/phrasing changes
- Added explanation of time course and multi-condition experiment visualization

#### Other
- Improved figure legends to be more descriptive
- Added mct1 transcriptomics raw data GEO ID
- Added metabolomics data Metabolomics Workbench ID
- Changed "reactant" to "substrate"
- Changed "graph" to "visualize" or "network" (depending on context)
- Added supplemental figures
  #### Handling data sparsity within the biological global network.
  - Added paragraph to showcase utility of reaction collapse (in murine tumor microenvironment study)





## To do:
- Continue to clean up some visualization aspects (e.g., options for display in perturbation networks)
- Flux integration
- Interactive motif searcher
