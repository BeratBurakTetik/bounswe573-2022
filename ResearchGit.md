## Introduction to Git

Git is a version control system used for sofware projects. It can be used for tracking changes in text based files.
Since, codes are basically texts, it is recommended too use git for software development processes. :smiley:

#### Here are some terms and commands that may help before using git.

| Term   | Description | 
| :---      |    :----:   |  
| repository      | Repository includes whole project files. Generally each project has one repository.|
| branch       | Repositories includes branches. When an update is made on the code new branch is created from master by the developer and the change is commited and pushed to the new branch. So the code on the master is not affected. | 
| remote      | Remote holds the last pushed version of a branch. Remote branches persisted in the servers of the git.|
| HEAD       | HEAD points the last commmit for the actual branch.| 
| conflict       | Conflicts occurs when you make a change in a file than want to pull a branch which has changes on the same file and merge into the actual branch. Needs to resolved. :rage:| 
| merge       | When two branches needed to combined, the changes(commits) in one branch are copied to another. To merge two branches pull requests are used. | 

#### Here are some basic commands to use git.

| Command   | Description | 
| :---      |    :----:   |  
|init      | Starts a local repository.         |
| add       | Makes git to track newly created folder.       | 
| commit      | Persists the changes for your local branch and moves the HEAD to point last commit.       |
| push       |Uploads the changes in your local branch to the remote so the changes persisted in the git servers.        | 
| pull      | Downloads the remote version of the specified branch and merges into actual branch.         |
| checkout       | Used for switching between branches. You can operate one one local branch at the same time.        | 
| fetch       | Receives the updates from remote branches. But not downloads them. Just checks if there is a commit that your local doesn't have.         |
