# Jupyter

For the demonstration we'll be using JupyterLab, a browser-based computational environment that marries full support for jupyter notebooks with a host of handy features, such as a file browser, console, and support for multiple notebooks and test files in tabs. If you appreciate the interactivity of Jupyter notebooks but want some of the powerful features normally found in an IDE, we recommend giving JupyterLab a try.

__1. Launching JupyterLab__

To launch JupyterLab, run the following from terminal (MacOS/Linux) or Anaconda prompt (Windows):
```
jupyter-lab
```

You do not need to be within a conda environment in order to have access to your conda environments, but if you don't have jupyter installed within your base conda environment, you will need to activate a conda environment with jupyter first.

__2. Opening a Notebook__

From here, you can view the files in your current directory, and choose a kernel to start a new notebook. Try loading `jupyter-test.ipynb` and experimenting with the features available.

Note: when you run jupyter it will set up a notebook server locally on your machine, launch your default browser, and navigate to the noteook server. If your browser doesn't launch, you can get the link to the browser from the terminal output. You should see something like this:
```
The Jupyter Notebook is running at:
http://localhost:xxxx/?token=sometoken
```
In this url, xxxx is the port Jupyter is running on and "sometoken" is a security token used to access the notebook. You should be able to access the Jupyter session by navigating to this link using your favourite browser. If you close your browser, you can return to the Jupyter session by navigating to this link as long as the kernel is still running in your termnial.

__3. Closing a Notebook__

The easiest way to close all notebooks is to shut the JupyterLab GUI and then pressing `CTRL+C` within the terminal (MacOS/Linux) or Anaconda prompt (Windows) that you launched JupyterLab from.
Alternatively, you can shutdown individual kernels from within the JupyterLab GUI. 
