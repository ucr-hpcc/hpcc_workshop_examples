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

a. Generate a new remote repository on GitHub online or use hub or GitHub CLI command-line wrappers for this. To avoid errors with the online method, do not initialize the new repository with README, license, or .gitignore files. You can add these files after your project has been pushed to GitHub.
```
git remote add origin git@github.com:<user_name>/<repos_name>.git
```


