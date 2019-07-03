# Conda

We'll be using conda to create an isolated Python installation that will form the basis of our reproducible workflow. We'll demonstrate (1) how to create a new conda environment from scratch, (2) how to export an environment so that others can create the same environment, (3) how to install an environment someone else has created.

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
```
source activate my-first-env # MacOS/Linux
conda activate my-first-env  # Windows
```

+ Install a package:
Let's install scipy, a popular open-source Python library for scientific computing.
```
conda install scipy
```
We could also have specified which version of scipy to install:
```
conda install scipy=1.2.1
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

__3. Install conda environment__

If you followed the instructions provided in the prerequisites, you will already have created an environment using a `.yml` file.
Let's create a new environment that is the same as the above environment, using the `.yml` file that we produced.

```
conda env create -f my-first-env.yml -n duplicate-first-env
```
