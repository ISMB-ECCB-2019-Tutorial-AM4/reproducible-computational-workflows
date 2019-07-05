# Prerequisites

These prerequisites must be installed prior to attending the tutorial!j

__GitHub Account__

We will host public software repositories on GitHub. If you do not have a GitHub account, sign up for a [free Personal user account](https://github.com/join).

__Software Installation__

**1. Conda** ([Windows](https://conda.io/projects/conda/en/latest/user-guide/install/windows.html), [MacOS](https://conda.io/projects/conda/en/latest/user-guide/install/macos.html), [Linux](https://conda.io/projects/conda/en/latest/user-guide/install/linux.html)) 

We'll be using conda to create an isolated Python installation. If you don't have a conda installation, follow the instructions [here](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).
We recommend installing **Miniconda** rather than Anaconda as it is much smaller and faster to download.

__Windows users__: To use conda, you'll first need to launch an Anaconda prompt session from the Start menu. This will provide a shell-like environment from which you can access your conda installation and environments.

If you already have a conda installation, make sure both conda and conda-build are up-to-date. You can update conda and conda-build in a Terminal window (MacOS, Linux) or Anaconda prompt (Windows) by running:
```
conda update conda
conda update conda-build
```

If you don't have conda-build, you can install it by running:
```
conda install conda-build
```

**2. Git** 

We will be using git for version control. Installation instructions for all platforms can be found [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). You will also need to create a GitHub account if you don't already have one.

__Windows users__: If you are working on Windows, we strongly recommend installing Git BASH. This will provide a shell-like environment that emulates BASH and allows you to use the command line. You won't have access to git from Anaconda prompt, or conda from Git BASH. If you want to use git make sure you're in Git BASH. If you want to use conda (including Jupyter) make sure you're in Anaconda prompt. We recommend keeping both open so that you can navigate between the two.


__3. Create a conda environment__

The file `environment.yml` specifies the Python version and all packages required by the tutorial. To create the conda environment from a Terminal window or Anaconda prompt, run:
```
conda env create -f 0-prerequisites/environment.yml
```

If you have any questions, please contact Peter Rose, pwrose@ucsd.edu