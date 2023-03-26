# Git and GitHub Exercises

## Git Basics from Command-Line

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

