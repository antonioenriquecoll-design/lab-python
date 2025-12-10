#!/bin/bash
#SBATCH -J lab-python-job
#SBATCH -p hpc-bio-mendel
#SBATCH --chdir=/home/alumno05/lab-python
#SBATCH -n 4
#SBATCH --cpus-per-task=2

module load anaconda/2025.06

# Valor por defecto si no se pasa argumento
VALUE=${1:-10000000}

echo "Ejecutando reduc-operation con N=${VALUE}"

# Ejecutar el script exportado desde el notebook
ipython reduc-operation-alumno05.py -- --value "${VALUE}"

module unload anaconda/2025.06
