# Version control and backup using git and GitHub

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

To speed things up we can configure git locally with out GitHub username and email address to save having to enter these each time we interact with GitHub.

```
git config --global user.name <username>
git config --global user.email <email>
```

First we need to create an empty repository on GitHub. You can find instructions for how to do this [here](https://help.github.com/en/articles/creating-a-new-repository).
To avoid errors when uploading our local repository, don't initialise this repository with a README, licence, or `.gitignore`. These can be added later.

Once we've created the repository on GitHub, we can add it as the *origin* for our local repository *i.e.* the remote location 
where the files are stored.

```
git remote add origin <repo url>
```

For example, using my GitHub account:

```
git remote add origin https://github.com/FBoyles/my-first-repo.git
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
