#!/bin/bash
#SBATCH --time=168:00:00
#SBATCH --nodes=1
#SBATCH -o /uufs/chpc.utah.edu/common/home/rutter-group1/j-berg/slurmjob-logs/slurmjob-%j
#SBATCH --account=rutter-gpu-np
#SBATCH --partition=rutter-gpu-np
#SBATCH --gres=gpu:2080ti:4
#SBATCH --mem=0

# Rutter lab GPU node specs
# - 40 cores
# - 192 GB of memory
# - 4x RTX2080TI GPUs

# Note: Change --gres command to up to `:4` to gain access to all 4 GPUs on node
# Note: --mem=0 reserves all node memory for the current job
# See https://www.chpc.utah.edu/documentation/guides/gpus-accelerators.php for more information on options
echo "+ Checking CUDA devices..."
echo "Devices: $CUDA_VISIBLE_DEVICES"
nvidia-smi -L

# Activate conda environment
source /uufs/chpc.utah.edu/common/home/u0690617/miniconda3/etc/profile.d/conda.sh
source activate xpresspipe

# Set instance variables
SCRUSER=/scratch/general/lustre/$USER
SCRDIR=/scratch/general/lustre/$USER/$SLURM_JOBID
PROJDIR=/uufs/chpc.utah.edu/common/home/rutter-group1/j-berg


cd /uufs/chpc.utah.edu/common/home/rutter-group1/j-berg/projects/manuscript/

#python mct1_analysis/notebooks/total_correlations.py
python mct1_analysis/notebooks/rnaseq_correlations.py
