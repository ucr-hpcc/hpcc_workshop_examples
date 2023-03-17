#!/bin/bash -l

#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=10G
#SBATCH --time=1-00:15:00
#SBATCH --mail-user=useremail@address.com
#SBATCH --mail-type=ALL
#SBATCH --job-name="Python Example"
#SBATCH -p intel

# Remove all modules and load miniconda3 (has python3)
module purge
module load miniconda3

echo "Job ID: $SLURM_JOB_ID"
echo "Nodelist: $SLURM_JOB_NODELIST"

# Use Python3 to run Python script
equation=$(sed -n "1p" equations.txt)
value=$(sed -n "1p" values.txt)
echo "$equation at x = $value : "
python3 myPyscript.py $equation $value