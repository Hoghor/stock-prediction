## Git Workflow

Everything below takes place in your terminal.

# First time setup

These steps does (hopefully) only have to be performed the first time you start working with the directory.

1. Change to a directory where you want the repository to live locally.
	* Example: `cd Documents/Repositories`
2. Clone the repository from GitHub
	* `git clone url-to-repo`
3. Change ditectory to repository
	* `cd name-of-repository/`

You are now within a git repository that is connected to GitHub

# Installing git-flow

Git flow is a high level branching model for git. It is easy to use when working with branches since it removes a lot of steps when it comes to merging and deleting branches.

* Mac: `brew install git-flow`
* Linux: `sudo apt-get install -y git-flow`
* Windows: [link](https://github.com/nvie/gitflow/wiki/Windows "Title")

# Nice to remember commands

**General commands**

* Print working directory: `pwd`
* Change directory: `cd`
* List files in directory: `ls`

**Git commands**

* List branches and show current branch: `git branch`
* Show status of current branch: `git status`
* Change active branch: `git checkout name-of-branch`
* Create new branch (alt 1): `git branch name-of-new-branch`
* Create new branch (alt 2): `git checkout -b name-of-new-branch`

**Git-flow commands**

* Start new feature branch: `git flow feature start name-of-feature-branch`
* Finish feature branch: `git flow feature finish name-of-feature-branch`
* Start new release branch: `git flow release start name-of-feature-branch`
* Finish release branch: `git flow release finish name-of-feature-branch`

**Vim commands**

* Save (write) and quit: `:wq`
* Quit: `:q`


# Workflow

Now that you have the connected repository locally and git-flow is installed, work can be started. It is nice to always follow this workflow since it is proven to be efficient and minimizes the errors.

The general workflow will be as follows. The live and currently working branch will be the *main branch*. All development of new stuff will be done in the *development branch*. From the *development branch*, new *feature branches* will be created where work will be done on new featuers that is going to be implemented. The *feature branches* will then be merged into the development branch. When the *development branch* has reached a state where we think it is ready to update the *main branch*, we will do so through a *release branch*. This workflow is demonstrated in the figure below.

![workflow](workflow.png)

1. When implementing something new, a new *feature branch* needs to be created. It is on this branch that your work will proceed until it is good enough to be merged together with the *develop* branch.

	* `git flow feature start name-of-feature-branch`

You will automatically be the new branch. 

2. Proceed with your work and when you are done or tired, push it to GitHub.

If new files were created they need to be *added* to the repository.

	* `git add name-of-file`

Next we need to commit the changes.

	* `git commit -am "commit comment of your choice"`

Lastly, push it to your new *feature branch* on GitHub

	* `git push origin name-of-feature-branch`

There will now be three branches both locally and on GitHub.

3. When you are happy with your new feature and want to add it for everyone else to use, there are two possible options for doing this.

	1. *Merge locally*. This is a quick way of merging new features but it prevents other people from reviewing them first. Git flow comes in handy here since it boils the process down to just one line.

		* `git flow feature finish name-of-feature-branch`

	The feature is now merged into the *develop branch* and the *feature branch* is deleted. We now need to push the *develop branch* to GitHub so other people can make use of the changes.

		* `git push origin develop`
