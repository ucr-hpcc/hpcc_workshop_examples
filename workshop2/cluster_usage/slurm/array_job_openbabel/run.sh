#!/bin/bash

# This script converts SDF chemical structure files into PNG images.
# We group the SDF files in batches of 20 to avoid spamming the Slurm queue.

#SBATCH --partition=short
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --time=10:00
#SBATCH --job-name="Array job test"
#SBATCH --array=1-5

# Some basic diagnostic info
hostname
date
echo SLURM_JOB_ID: $SLURM_JOB_ID
echo SLURM_ARRAY_TASK_ID: $SLURM_ARRAY_TASK_ID

# Using SLURM_JOB_ID gives us a unique output directory each run.
# This is to prevent accidental overwriting of previous runs.
mkdir -p batch_$SLURM_ARRAY_TASK_ID/output_$SLURM_JOB_ID

module load openbabel

cd batch_$SLURM_ARRAY_TASK_ID

for f in *.sdf; do
  obabel -isdf $f -opng -O output_$SLURM_JOB_ID/$f.png
done

echo Done!
