#!/bin/bash

# The partition we want (short==24 hours, long=7 days)
#SBATCH --partition short
# One node
#SBATCH -N 1
# One job on that node
#SBATCH -n 1
# Please give me a GPU
#SBATCH --gres=gpu
# Give a CPU from the following list
##SBATCH --constraint="A100"

# Ask for memory
#SBATCH --mem=16gb

# Get a node for more general use.

# Run a python program using our local virtual environment
cd /home/rcpaffenroth/tmp/DSCS553_example/turing_example
venv/bin/python quickstart_tutorial.py

