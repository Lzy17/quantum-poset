#!/usr/bin/env bash

#SBATCH --job-name=poset
#SBATCH --account=sds173
#SBATCH --partition=compute
#SBATCH --time=01:00:00
#SBATCH --nodes=8
#SBATCH --ntasks-per-node=24
#SBATCH --output=poset.o%j.%N

module purge
module list
printenv

python3 spectrum.py
