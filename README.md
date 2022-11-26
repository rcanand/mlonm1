# ML on M1 mac

This document tries different components of a (python based) Machine Learning (ML) stack on Apple Silicon (M1) macs.

Everything here is the thinking as of 11/03/2022, and is subject to change.

Apple Silicon includes all macs from original m1 all the way to the latest apple silicon (m1, m1 pro, m1 max, m1 ultra, m2). Practically, the following were tested on the original m1 mac mini running macOS Ventura 13.0 (22A380) with vs code and terminal.

We have many choices for a package manager - venv+pip, miniconda+(conda-forge/pip), miniforge, anaconda, mamba, mambaforge.
miniconda3 now supports m1 macs with python 3.9.latest. So, we will use miniconda to create the conda environment.

So, download and install miniconda for Apple M1 from [here](https://docs.conda.io/en/latest/miniconda.html), following the instructions there.

## Classical ML

  ```sh
  conda create --name=ml_py_lt_3_10 "python<3.10"
  # if you any conda environment is active, even base, then deactivate it first
  # also do this if it seems to pick up the wrong python version
  conda deactivate
  conda activate ml_py_lt_3_10
  ```

- The core classical python stack:
  - numpy - `conda install -c conda-forge numpy`
  - matplotlib - `conda install -c conda-forge matplotlib`
  - scipy - `conda install -c conda-forge scipy`
  - pandas - `conda install -c conda-forge pandas`
  - scikit-learn - `conda install -c conda-forge scikit-learn`
  - seaborn - `conda install -c conda-forge seaborn` (which includes statsmodels - installed but not tried out yet)

## Tensorflow 2 on M1 Mac

- Tensorflow 2 has been compatible with M1 macs via Apple Metal for a while now
  - official instructions [here](https://developer.apple.com/metal/tensorflow-plugin/) fail with grpcio install - see [open issue](https://github.com/grpc/grpc/issues/25082)
  - [This](https://wandb.ai/tcapelle/apple_m1_pro/reports/Deep-Learning-on-the-M1-Pro-with-Apple-Silicon---VmlldzoxMjQ0NjY3) one works
    - Use tf_apple.yml from [here](https://github.com/tcapelle/apple_m1_pro_python/blob/main/tensorflow/tf_apple.yml)
      - change the name of the environment as needed (from tf2 in the file) - tf2_metal
      - (remove wandb and fastcore if not needed)
    - `conda env create --file=tf_apple.yml`
    - deactivate previous environments till no environment remains - call repeatedly - `conda deactivate`
    - activate the environment - `conda activate tf2`
    - run a test tensorflow script like the one in [this article - see section 4. Verify](https://developer.apple.com/metal/tensorflow-plugin/)
    - this environment also has jupyter, so you can run tensorflow in a notebook:
      - first, install the environment as a kernel in jupyter - `python -m ipykernel install --user --name tf2_metal --display-name "Python3.9.13(tf2_metal)"`
      - launch `jupyter notebook`
      - create a new notebook
      - paste tensorflow code (like the [code from before](https://developer.apple.com/metal/tensorflow-plugin/)) into this cell
      - run the cell

## Pytorch on M1 Mac

- Based on [this article](https://wandb.ai/capecape/pytorch-M1Pro/reports/PyTorch-Runs-On-the-GPU-of-Apple-M1-Macs-Now-Announcement-With-Code-Samples---VmlldzoyMDMyNzMz#-run-this-benchmark-and-contribute-to-this-table-🚀) steps from September 2022
  - deactivate conda (as many times as needed to get out of any environment) - `conda deactivate`
  - Create conda environment: `conda create --name="pytorch_metal" python`
  - Activate the environment: `conda activate pytorch_metal`
  - Install the pytorch nightly build: `pip install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu`
  - Run code from [pytorch tutorial](https://github.com/pytorch/tutorials/blob/master/beginner_source/basics/quickstart_tutorial.py)
  - Try running from jupyterlab - first, install it: `pip install jupyterlab`
  - Install the kernel into jupyter: `python -m ipykernel install --user --name pytorch_metal --display-name "Python3.10.6(pytorch_metal)"`
  - Launch jupyterlab: `jupyter lab`
  - Paste pytorch code (like [the one before](https://github.com/pytorch/tutorials/blob/master/beginner_source/basics/quickstart_tutorial.py)) into the cell
  - run the cell

## Huggingface transformers with pytorch on M1 Mac

- We have to pick an environment that runs pytorch or tensorflow (maybe we can combine both, but that is for another day). For now, picking pytorch.
  - Clone the pytorch_metal environment created above to create new environment pytorch_metal_transformers: `conda create --name pytorch_metal_transformers --clone pytorch_metal`
  - deactivate (multiple times if needed), then activate the new environment: `conda activate pytorch_metal_transformers`
  - Install transformers from huggingface: `conda install -c huggingface transformers`
  - TIP: You may need to deactivate and reactivate again (installing new libraries sometimes switches python to base python - always check `which python` - if the python is not from current env folder, then deactivate and reactivate, and check again)
  - Run some simple transformers code - you can find examples in the [quicktour](https://huggingface.co/docs/transformers/v4.24.0/en/quicktour)

## TODOs

- 🤗Training, fine tuning, inference on huggingface transformers
- 🤗 with tensorflow
- Jax
- 🤗Diffusers (Note: there were some issues getting stable-diffusion to work)
- 🤗Accelerators
- Pytorch lightning
- Kitchen sink 🤗+torch stack (with all other common libraries)
- Kitchen sink 🤗+tensorflow stack
- Many others to try: spacy, parquet, boto3, tqdm, onnxruntime, statsmodels, xgboost, lightgbm, catboost, bokeh, etc.
- Combined torch and tensorflow 🤗 kitchen sink stack (is this supported?)
