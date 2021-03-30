library(spqn)
library(data.table)
library(WGCNA)

setwd(
  "C:\\Users\\jorda\\Desktop\\projects\\manuscript\\mct1_analysis")


# Read data 
# Removed gene rows where min value was not 25 or greater
# Performed TPM normalization of gene counts
counts <- read.table(
  "data/mct1_rnaseq_data/sce_mct1_deduped_tpm_threshold25.tsv", 
  sep='\t', 
  header=TRUE, 
  row.names="X")


# Pre-process data
log_data <- log2(counts + 0.5)
ave_log_data <- rowMeans(log_data)
log_data_centered <- log_data - ave_log_data # mean centering
log_data_centered  <- log_data_centered / matrixStats::rowSds(
  as.matrix(log_data_centered)) # variance scaling

# Remove PCs (4) from the gene expression matrix after scaling each gene to 
# have mean=0 and variance=1
log_data_pc4 <- removePrincipalComponents(
  t(scale(t(log_data_centered))), 
  n = 4)


# Perform base correlation of pre-processed data
cor_m <- cor(t(log_data_pc4))

# we re-arrrange the correlation matrix by sortng the row and column by the 
# expression level, and partitioned the correlation matrix into same-size bins, 
# then used each bin to estimate the distribution of correlation for genes with 
# that expression level. Here we use 10 by 10 bins.
# The second plot will show that high-expressed genes' correlation is 
# skewed high
plot_signal_condition_exp(cor_m, ave_log_data, signal=0)
plot_signal_condition_exp(cor_m, ave_log_data, signal=0.001)

# We next plot the marginal relationship between IQR of correlation and the 
# expression level of the lower expression group for each bin, and we also see 
# a positive relationship.
# Note: I do not see with with TPM-normalized data
IQR_list <- get_IQR_condition_exp(cor_m, ave_log_data)
IQR_unlist <- unlist(lapply(1:10, function(ii) IQR_list$IQR_cor_mat[ii, ii:10]))
plot(rep(IQR_list$grp_mean, times = 1:10),
     IQR_unlist,
     xlab="min(average(log2TPM))", ylab="IQR", cex.lab=1.5, cex.axis=1.2, col="blue")

# We further examined the difference of the distributions using Q-Q plot. We 
# used the bins with the second highest expression level on the diagonal as 
# reference, and compared the distribution with other bins in the diagonal. We 
# observe both scale and shape difference in the distributions.
par(mfrow = c(3,3))
for(j in c(1:8,10)){
  qqplot_condition_exp(cor_m, ave_log_data, j, j)
}


# SPQN normalization
cor_m_spqn <- normalize_correlation(
  cor_m, 
  ave_exp=ave_log_data, 
  ngrp=20, 
  size_grp=300, 
  ref_grp=18)

# Distribution of predicted signals and background correlations for bins on the 
# diagonal of the correlation matrix.
# Note: Signal becomes more uniform
plot_signal_condition_exp(cor_m_spqn, ave_log_data, signal=0)
plot_signal_condition_exp(cor_m_spqn, ave_log_data, signal=0.001)

IQR_spqn_list <- get_IQR_condition_exp(cor_m_spqn, ave_log_data)

# Q-Q plots
par(mfrow = c(3,3))
for(j in c(1:8,10)){
  qqplot_condition_exp(cor_m_spqn, ave_log_data, j, j)
}

# Marginal relationship between IQR and the expression level of the lower 
# expressed group for each bin.
IQR_unlist <- unlist(lapply(1:10, function(ii) IQR_spqn_list$IQR_cor_mat[ii, ii:10]))
plot(rep(IQR_spqn_list$grp_mean, times = 1:10),
     IQR_unlist,
     xlab="min(average(log2TPM))", ylab="IQR", cex.lab=1.5, cex.axis=1.2, col="blue")

# Add gene names to row and col names
row.names(cor_m_spqn) <- row.names(cor_m)
colnames(cor_m_spqn) <- colnames(cor_m)

# Output results
write.table(
  cor_m_spqn, 
  file="data/yeast_mct1_rnaseq_spqn_cor.tsv", 
  row.names=TRUE, 
  col.names=TRUE,
  sep="\t")
