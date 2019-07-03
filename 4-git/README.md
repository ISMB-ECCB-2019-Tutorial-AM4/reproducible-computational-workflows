# Version control and repository hosting using git and GitHub

In this section of the tutorial we'll cover the basics of using git for version control on our local codebase. We'll then go over hosting our git repository on GitHub, and pushing and pulling changes between the local and remote repositories. We'll finish by forking a project on GitHub, creating a development branch, implementing some changes, and merging our changes with the master branch hosted on GitHub. We'll do all of this in a Jupyter notebook to demonstrate how notebooks are hosted on GitHub.

## Introduction to git and GitHub

First, let's create a directory for our project and add a readme file:

```
mkdir my-first-repo
touch my-first-repo/README.md
```

__Creating a repository__

To put our project under version control, the first thing we need to do is create a git repository. 

```
cd my-first-repo
git init
```

This creates a subdirectory called .git where git will store all the files it uses to manage the repository.

__Adding files to the repository__

When you first create a repository it will be empty, even if there were already files in the directory.
There are two steps to updating the files in the repository: staging and committing. The commands `git add` and `git commit`
are used to stage and commit changes respectively. 'Staging' a file tells git that you want to include the changes to that file next time the repository is updated, but doesn't actually change 
the version of the file recorded by git. 'Committing' the staged changes updates the repository to include all of 
the staged changes. At any point we can use the command `git status` to check for files in the directory that have not 
been staged, or staged changes that have not been committed.

Let's go ahead and update the repository to include our readme:

```
git add README.md
git commit -m 'initial commit'
```
__Remote backup on GitHub__

You've already created a local copy of a GitHub repository when you cloned the material for this tutorial. Cloning a repository creates a 
local copy of both the project and the git repository, which you can then interact with locally using git. We can also go the 
other way around and host a copy of our local repository on GitHub.

First we need to create an empty repository on GitHub. You can find instructions for how to do this [here](https://help.github.com/en/articles/creating-a-new-repository).
To avoid errors when uploading our local repository, don't initialise this repository with a README, licence, or `.gitignore`. These can be added later.

Once we've created the repository on GitHub, we can add it as the *origin* for our local repository *i.e.* the remote location 
where the files are stored.

```
git remote add origin <repo url>
```

For example, using your personal GitHub account:

```
git remote add origin https://github.com/<username>/my-first-repo.git
```

Finally, we can push our local changes to the remote repository using the `git push` command:

```
git push origin master
```

- `push` tells git to upload the changes to a remote server and merge them into the repository
- `origin` tells git to push to the remote origin we set previously
- `master` tells git to push to the master branch

Great, now our code is under version control locally and backed up remotely on GitHub.

The last thing we're going to do here is learn how to copy changes on the remote repository to our local repository.
First let's add a file to the repository on GitHub. From the GitHub repository, click the 'Create new file' button 
and add your favourite piece of code. When you're finished, click the 'Commit changes' button to commit the new file 
to the repository.

To update our local repository to reflect the changes to the remote, we use the `git pull` command:

```
git pull origin master
```

`pull` tells git to download changes from the remote repository and merge them into our local repository. 
Just like `push` we can specify which remote server and branch we want to pull from.

## Forking, branching, and merging

So far we've seen how to create and manage a project by working on the master branch of a repository. Often when working on a project with multiple contributors on different 
issues, it is beneficial to work on a separate branch to ensure our changes are isolated from the master branch until we are satisfied the code is complete and functional.
In addition, we might want to build on or extend a project for which we are not already contributors. To accomplish this efficiently, we need to understand the concepts of
forking, branching, and merging repositories.

In this part of the tutorial, we'll create a fork of the tutorial repository to use as the remote origin for the version we cloned earlier. We'll create a 'development' branch
to work on our changes, before merging with the master branch. Finally, we'll submit a pull request to the original repository on GitHub to add our work to the project.

__Fork the original repository__

When a repository is cloned, the remote origin of each branch will also be copied to the cloned repository. In the case of cloning a repository from Github, the remote origin will be the original GitHub repository. Chances are if you're cloning a project you found on GitHub you won't have contributor rights to the project, so will need to set an alternative origin if you want to host your changes to GitHub. Fortunately, by also forking the repository we cloned, we can set our fork as the remote origin for our repository and push our changes straight to GitHub.

To fork a repository, simply navigate to the [repository](https://github.com/ISMB-ECCB-2019-Tutorial-AM4/reproducible-computational-workflows) on GitHub and click the 'fork' button.

Boom! Now you have a copy of the repository you can edit. Your fork is completely independent of the original repository: changes there won't be reflected in the fork, and your changes won't be submitted to the original. We'll cover merging changes between forks later in the tutorial.

First, let's set the forked repository as the remote for the tutorial repository we cloned earlier. Open a terminal (Linux/mac) or Git BASH session (Windows) and navigate to the repository:

```
cd reproducible-computational-workflows
```

To see the forked repository as the remote, we use the `git remote set-url` command:

```
git remote set-url <remote name> <remote url>
```

- `remote name` is the name of the remote we want to change. In this case it's 'origin'. To list all remotes associated with a repository, use the command `git remote -v`.
- `remote url` is the new url we wish to set the remote to, in this case it's the url of our fork.

We can now push and pull changes between the cloned repository and our fork on GitHub.

__Creating a new branch__

__Merging branches__

__Merging forks and pull requests__
