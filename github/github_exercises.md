# Git and GitHub Exercises

## 1. Git Basics from Command-Line

### Finding help from command-line
```
git <command> --help
```

### Initialize a directory as a Git repository
```
git init
```

### Add specific files to Git repository (staging area)
```
git add myfile
```

### Add all files recursively
To ignore specific files (e.g. temp files), list them in a .gitignore file in your repository’s root directory. Regular expressions are supported. See [here](https://help.github.com/articles/ignoring-files/) for more details.
```
git add -A :/
```

### After editing file(s) in your repos, record a snapshot of the staging area
```
git commit -am "some edits"
```

## 2. GitHub Basics from Command-Line

(a) Generate a new remote repository on GitHub online or use hub or GitHub CLI command-line wrappers for this. To avoid errors with the online method, do not initialize the new repository with README, license, or .gitignore files. You can add these files after your project has been pushed to GitHub.

```
git remote add origin git@github.com:<user_name>/<repos_name>.git
```

(b) Push updates to remote. Next time one can just use git push

```
git push -u origin master
```

(c) Clone existing remote repository

```
git clone git@github.com:<user_name>/<repos_name>.git
```

(d) Before working on project, update local git repos

```
git pull 
```

(e) Make changes and recommit local to remote

```
git commit -am "some edits"; git push -u origin master
```

Note, in order to work with private GitHub repositories, users need to activate under _Settings_ in their GitHub account as authentication method either a [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) or an [ssh key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account). The latter ssh key method is usually preferred. Instructions are given in the corresponding links of the previous sentence. To commit to a private GitHub repository from the HPCC cluster, you need to generate an ssh key from your home account using the standard Linux `ssh-keygen` method as described [here](https://hpcc.ucr.edu/manuals/login/#ssh-keys), and then upload the newly generated public ssh key of your HPCC account located under `~/.ssh/id_rsa.pub` to GitHub.

3. Exercise

Run the following git/github excercise from the command-line. Do this after creating a GitHub repos according to the instructions above.

```
git clone git@github.com:<user or org>/<repo name> 
cd <repo name>
git pull
touch test # Creates empty file for testing
git add test # or use '-A' for all
git commit -am "some edits"
git push 
##-> Edit test file online and then run `git pull` to inspect changes
```


