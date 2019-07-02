# Prerequisites

We will make use of several pieces of software in the tutorial. The below instructions are designed to work across all platforms (Windows/MacOS/Linux). If you have any of the software already installed please feel free to skip these steps.

In addition, you will need to download materials for use in the workshop, and create a python environment using conda.

__Software Installation:__

1. Conda ([Windows](https://conda.io/projects/conda/en/latest/user-guide/install/windows.html), [MacOS](https://conda.io/projects/conda/en/latest/user-guide/install/macos.html), [Linux](https://conda.io/projects/conda/en/latest/user-guide/install/linux.html)) 

We'll be using conda to create an isolated Python installation. If you don't have a conda installation, you can follow the instructions [here](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).
We recommend installing Miniconda rather than Anaconda as it is much smaller, and we'll be installing the specific python packages we need later anyway.

If you already have a conda installation, you'll want to make sure both conda and conda build are reasonably up-to-date. You can update conda and conda build in a Terminal window (MacOS, Linux) or Anaconda prompt (Windows) by running:
```
conda update conda
conda update conda-build
```

If you don't have conda build, you can install it by running:
```
conda install conda-build
```

2. Git ([all platforms](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git))

We will be using git for version control. Installation instructions for all platforms can be found [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

If you are working on Windows, we strongly recommend installing Git BASH. This will provide a shell-like environment that emulates BASH and allows you to use the command line. You won't have access to git from Anaconda prompt, or conda from Git BASH. If you want to use git make sure you're in Git BASH. If you want to use conda (including Jupyter) make sure you're in Anaconda prompt. We recommend keeping both open so that you can navigate between the two.


__Materials and Environment Setup:__

1. Download all materials by cloning this repository
```
git clone https://github.com/ISMB-ECCB-2019-Tutorial-AM4/reproducible-computational-workflows
cd reproducible-computational-workflows
```

2. Create a conda environment for the workshop:

The file `ismb2019.yml` specifies the python version and all packages used when running the notebooks. To create the conda environment from a Terminal window or Anaconda prompt, run:
```
conda env create -f 0-prerequisites/ismb2019.yml
```
