# Conda

## Overview

Conda is an open source package management system and environment management system that runs on Windows, macOS and Linux.

Conda installs, runs, and updates packages and their dependencies, while checking compatibility with all preexisting packages. This is in stark contrast to pip, which installs all Python package dependencies required, whether or not those conflict with other packages previously installed. 

In addition, Conda allow you to create, save, load and switch between multiple environments on your local computer, as well as share instructions for how to recreate that environment on a different computer.

While Conda was originally created for Python programs, it can package and distribute software for any language (e.g. R, Ruby, Lua, Scala, Java, JavaScript, C/ C++, FORTRAN).

## Guide

We'll be using conda to create an isolated Python installation that will form the basis of our reproducible workflow. We'll demonstrate (1) how to create a new conda environment from scratch, (2) how to export an environment so that others can create the same environment, (3) how to remove an environment, (4) how to install an environment someone else has created.

__1. New conda environment from scratch__

We can create a new environment with the following steps either in a terminal (MacOS/Linux) or Anaconda prompt (Windows):

+ Create base environment:
We're going to specify the version of python we want, but install no other packages (for now)
```
conda create --name my-first-env python=3.7
```

+ Check install:
You can verify that conda has created an environment called 'my-first-env' by running either of the following commands:
```
conda info --envs
conda env list
```
We can also check which packages have been installed by running:
```
conda list -n my-first-env
```

+ Activate the environment:
You can install additional packages without activating the environment, but it's typically easier to do so from within the environment itself. Once we've activated the environment, all commands are executed within that environment.
From either a terminal or an Anaconda prompt, to activate my-first-env run:
```
conda activate my-first-env
```

+ Install a package:
Let's install numpy, a popular open-source Python library for numeric computing, in particular matrix manipulation.
```
conda install numpy
```
We could also have specified which version of numpy to install:
```
conda install numpy=1.16.4
```

__2. Export conda environment__

We can export a `.yml` file containing a list of all of the packages in our environment. This will allow conda to recreate an identical environment elsewhere. This is done using the following command while the environment is active:
```
conda env export > my-first-env.yml
```
Or if the environment is not active:
```
conda env export -n my-first-env > my-first-env.yml
```

__3. Remove conda environment__

Removing an environment is relatively straightforward. To remove an environment, in your terminal window or an Anaconda Prompt, run:
```
conda remove --name my-first-env --all
```
We can verify that this successfully removed the environment by listing our environments:
```
conda info --envs
```


__4. Install conda environment__

If you followed the instructions provided in the prerequisites, you will already have created an environment using a `.yml` file.
Let's recreate the environment that we just removed. This time, instead of creating it from scratch, we'll create it using the `.yml` file that we produced.

```
conda env create -f my-first-env.yml -n my-first-env
```
