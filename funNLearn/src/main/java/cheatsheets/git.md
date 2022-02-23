### Resets
-----------
- this takes out the commit and puts it back on the branch by doing this you will come back to point P1
    ```
    git reset --soft HEAD~1
    ```

- trash the last 1 commit and then set it back to Head
    ```
    git reset --hard HEAD~1
    ```

### Review
-----------
```
git checkout develop
git pull
git checkout -b feature/vishalm/<my_feature_branch>
git commit <Files>
git checkout develop
git pull
git checkout feature/vishalm/<my_feature_branch>
git rebase develop

git push -u develop
```

### Complete rinse 
-------------------
```
git clean -xfd
git submodule foreach --recursive git clean -xfd
git reset --hard
git submodule foreach --recursive git reset --hard
git submodule update --init --recursive
```

### Submodule
-------------
```
git submodule update --init
```

### Remove Local Changes
--------------------------------------------

There could be only three categories of files when we make local changes:
1. Staged Tracked files
2. Unstaged Tracked files
3. Unstaged UnTracked files a.k.a UnTracked files

* Staged - Those that are moved to staging area/ Added to index
* Tracked - modified files
* UnTracked - new files. Always unstaged. If staged, that means they are tracked.

What each commands do:
```
git checkout .     - Removes Unstaged Tracked files ONLY [Type 2]
git clean -f       - Removes Unstaged UnTracked files ONLY [Type 3]
git reset --hard   - Removes Staged Tracked and UnStaged Tracked files ONLY[Type 1, Type 2]

git stash -u       - Removes all changes [Type 1, Type 2, Type 3]
```

1. combination of 
```
git clean -f
git reset --hard
```

2. `git stash -u`
   
   Stashing, as the word means 'Store (something) safely and secretly in a specified place.' 
   This can always be retrieved using git stash pop. So choosing between the above two options is developer's call.


## Rollback last commit from remote
```bash
    git reset HEAD^
    git push origin +HEAD
    # after this remote is reset and you should see the last commit changes as pending in local
```

## reset a local branch to exactly match a remote branch. 
```bash
    git fetch origin
    git reset --hard origin/<remote_branch_name>

    # eg: 
    git reset --hard origin/master
```

