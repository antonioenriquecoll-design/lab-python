#!/bin/bash
#SBATCH -J lab-python-job
#SBATCH -p hpc-bio-mendel
#SBATCH --chdir=/home/alumno05/lab-python
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH -t 00:10:00
#SBATCH -o slurm-%x-%j.out
#SBATCH -e slurm-%x-%j.err

module load anaconda/2025.06

# Valor por defecto si no se pasa argumento
VALUE=${1:-10000000}

echo "==> Ejecutando reduc-operation-alumno05.py con N=${VALUE}"
ipython reduc-operation-alumno05.py -- --value "${VALUE}"

module unload anaconda/2025.06

