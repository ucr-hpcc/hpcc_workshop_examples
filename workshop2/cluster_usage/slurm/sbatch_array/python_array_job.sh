#!/bin/bash -l

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
#SBATCH --time=00:05:00
#SBATCH --mail-user=useremail@address.com
#SBATCH --mail-type=ALL
#SBATCH --job-name="Python Array Example"
#SBATCH -p short

# Remove all modules and load miniconda3 (has python3)
module purge
module load miniconda3

echo "Job ID: $SLURM_JOB_ID"
echo "Nodelist: $SLURM_JOB_NODELIST"

# Use Python3 to run Python script
equation=$(sed -n "${SLURM_ARRAY_TASK_ID}p" equations.txt)
value=$(sed -n "${SLURM_ARRAY_TASK_ID}p" values.txt)

echo "Evaluating equation $SLURM_ARRAY_TASK_ID"
echo "$equation at x = $value : "
python3 myPyscript.py $equation $value
