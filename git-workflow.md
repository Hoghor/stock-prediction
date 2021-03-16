## Git Workflow

Everything below takes place in your terminal.

# First time setup

These steps does (hopefully) only have to be performed the first time you start working with the directory.

1. Change to a directory where you want the repository to live locally.
	* Example: cd Documents/Repositories
2. Clone the repository from GitHub
	* Use command: git clone url-to-repo
3. Change ditectory to repository
	* Use command: cd name-of-repository/

You are now within a git repository that is connected to GitHub

# Installing git-flow

Git flow is a high level branching model for git. It is easy to use when working with branches since it removes a lot of steps when it comes to merging and deleting branches.

* Mac: `brew install git-flow`
* Linux: `sudo apt-get install -y git-flow`
* Windows: [link](https://github.com/nvie/gitflow/wiki/Windows "Title")

# Workflow

Now that you have the connected repository locally and git-flow is installed, work can be started. It is nice to always follow this workflow since it is proven to be efficient and minimizes the errors.

Write generall workflow, main + develop.

1. When implementing something new, a new *feature* _emphasize_ branch needs to be created. It is on this branch that your work will proceed until it is good enough to be merged together with the *develop* _emphasize_ branch.


