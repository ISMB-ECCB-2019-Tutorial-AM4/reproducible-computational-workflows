# Projects

In the previous sesssions you were introduced to

* How to setup a project in GitHub
* How to create an environment in Conda
* How to run a Jupyter Notebook
* How to setup a project in Binder

The goal of this session is to combine these steps and to create a project in your own GitHub account and then share and run it on Mybinder.org.

You can either use one or more of the provided Jupyter Notebooks or use your own Jupyter Notebooks. 

#### Provided Jupyter Notebooks

This directory contains two subdirectories with example Notebooks and data files.
* scop-class-prediction: a binary classification problem
* 3D-visualization: a visualization example

## Create your own project

1. Follow the [instructions](https://help.github.com/en/articles/creating-a-new-repository) to create an empty repository on GitHub. 

**Do not initialise this repository with a README, licence, or .gitignore file.**

2. Check your current working directory (make sure that your are *not* inside the ISMB tutorial directory!)
```
pwd
```

3. Create a directory with your project name (same name as the repository you've created on GitHub)
```
mkdir <your-project>
```

4. cd into the project directory
```
cd <your-project>
```

5. Create a ```data``` directory and copy any required data files from this tutorial
```
mkdir data
cp  <path>/<data-file>  data
```

6. Create a ```notebooks``` directory and copy either provided or your own Jupyter Notebook(s)
```
mkdir notebooks
cp  <path>/<notebook.ipynb>  notebooks 
```

7. Copy the ```binder``` directory and its content from the ISMB tutorial
```
cp  -r  <path>/binder  .
```

8. If you used your own Jupyter Notebook(s), update dependencies in the `binder/environment.yml` file (do not include Jupyter and Jupyterlab as dependencies since they will be provided by MyBinder.org)

9. Copy the LICENSE and .gitignore file from the ISMB tutorial
```
cp  <path>/LICENSE  .
cp  <path>/.gitignore  .
```

11. Using jupyter-lab, create a README.md file, add a brief description, and save the file. Preview the README.md in jupyter-lab.

12. Run jupyter-lab and test your notebooks. You may need to change the path to your data files to match the directory structure.

## Put your project under version control

1. Create a Git repository (run `git init` in your project directory, use `pwd` to confirm location!) and add the remote location where your files are stored on GitHub.
```
git init
git remote add origin https://github.com/your-user-name/your-project.git
```

2. Show the files to be added to the repository
```
git status
```

3. Add all files
```
git add  .
```

4. Commit your files
```
git commit -m 'initial commit'
```

5. Push your files to GitHub
```
git push origin master
```

6. Open your GitHub project in a web browser and make sure all required files are present.
```
https://github.com/your-user-name/your-project
```

## Setup your project in MyBinder.org

1. Copy the GitHub URL of your project

2. Go to [MyBinder.org](https://mybinder.org) and paste in the GitHub URL. If your repository contains a single Notebook, create a specific link for the Notebook. 

3. Copy the Binder Badge Markdown text snippet.

3. Paste the text snippet into your README.md file. Optionally, modify the launch link to use jupyter-lab ([see](../5-binder/Binder.pdf)).

4. Add the modified README.md file to Git
```
git status
git add README.md
```

5. Commit you changes
```
git commit -m "added binder badge"
```

6. Push the README.md file to GitHub
```
git push origin master
```


## Test your project

1. Open your Git project in a web browser and click the "Launch Binder" badge.

2. Wait, wait, ... it may take several minutes to build a binder image ... until Jupyter launches.

3. Run your Notebooks on MyBinder

## Congratulations

You've created and hosted your first Jupyter Notebook on Binder! Use this project as a template for your future reproducible science projects.

Demo what you did at our next work or lab meeting! Share a binder link with your co-workers or tweet it.

If you found this tutorial helpful, please click the __* Star__ button at the top-right corner of this repository!





