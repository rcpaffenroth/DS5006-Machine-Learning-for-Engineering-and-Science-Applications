# File explanation

jupyter nbconvert --to notebook --execute quickstart_tutorial.ipynb --output=quickstart_tutorial_output.ipynb --ExecutePreprocessor.timeout=-1

jupytext --to py quickstart_tutorial.ipynb

wandb sweep sweep_runner.yml

## demo.py
Simple Python script for demo.

## export_simple_model_to_onnx_tutorial.ipynb
A Jupyter notebook that demonstrates how to export a simple PyTorch model to ONNX format.

## pytorchUsingGPU.py
A Python script that demonstrates how to detect and use GPU in PyTorch.

## quickstart_tutorial.ipynb
A Jupyter notebook that demonstrates pytorch

## quickstart_tutorial.py
A Python version of the quickstart_tutorial.ipynb

## requirements.txt
Pip list of required Python packages.

## Shell scipts to demo Slurm
sbatch_demo.sh*
sbatch_notebook_demo.sh*
sbatch_py_demo.sh*
sbatch_sweep_demo.sh*

## Example of the WandB sweep
sweep_runner.py
sweep_runner.yml

## timing.py
A simple timing script
