![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

<div align="left">
  <img src="https://github.com/Shamslux/DataEngineering/assets/79280485/947b9e01-1805-49b2-8aaa-5933bbd2611e" alt="Badge" width="150">
</div>

<div align="right">
  <img src="https://github.com/Shamslux/DataEngineering/assets/79280485/a812dfb8-ebe1-4e47-9204-2f35bc847a1f" alt="Badge" width="150">
</div>

# What is DIO?

DIO is a Brazilian education platform that offers training in various IT areas. Besides courses of various levels, the platform also encourages its community of students and professionals to share knowledge from their study and work routines. With a gamified approach, you can enrich your internal profile with various code challenges, project challenges, and other activities, which, over time, add up to strengthen your professional profile, since the platform brings together a network of recruiters in partnership with DIO, who have access to various profiles of the best and most competent candidates.

# What are Git and GitHub?

Git is a version control system, essentially copies of various stages of what is being versioned. Git operates through the terminal or via more visual and user-friendly tools.

GitHub is a platform that uses Git to provide additional services aimed at facilitating collaboration and project management. It allows us to store versions of projects in a way that several people can collaborate and have their projects securely saved in the cloud, in repositories, providing more security than if everything were saved on local machines.

## How do they relate?

Git allows us to use a command line to execute code commands to create versions, track code (I'll keep the example to code since it's the most common purpose), make changes, etc.

GitHub has repositories (simply put, folders with the project files, generally, we have one repository representing one project, for example). Thus, GitHub relates to Git in that one is the language used within this platform, allowing for tracking, modifying, creating, etc., as well as hosting and protecting data on its servers.

## How to install?

Simply (I won't go into detail, I'm just reviewing my knowledge from the course, I've been using Git and GitHub for a few years), just download Git for Windows from the official website (just download Git Bash, which comes with its own command prompt for executing the commands).

## Configuring

We must first configure the user and email.

```shell
git config --global user.name "<your username>"
```

After configuring the user, let's configure the email:

```shell
git config --global user.email "<your email@email.com>"
```

To check if it was successful, we'll do the following:

```shell
git config --list
```
![config_--list_result](https://github.com/Shamslux/DataEngineering/assets/79280485/8742c5ca-68c8-4c5c-9574-c53a47677451)

```shell
git --version
```

Returns the version of Git installed on the operating system.

# Main Git Commands


```shell
git init
```
Initializes a new Git repository in the current directory.

```shell
git clone <URL>
```

Clones an existing Git repository to the local directory.

```shell
git add .
```

Adds changes to the index (staging area) to prepare them for commit.

```shell
git commit -m "<message>"
```

Commits the added changes, including a message describing the changes made.

```shell
git status
```

Displays the current state of the repository, indicating which files have been modified, added, or removed.

```shell
git log
```

Shows the commit history of the repository.

```shell
git branch
```

Lists all local branches and highlights the current branch.

```shell
git branch <branch-name>
```

Creates a new branch.

```shell
git checkout <branch-name>
```

Switches to a specific branch.

```shell
git merge <branch>
```

Combines the changes from one branch into the current branch.

```shell
git pull
```

Updates the local repository with changes from the remote repository.

```shell
git push remote <branch>
```

Sends local commits to the remote repository.

```shell
git remote -v
```

Lists the configured remote repositories.

```shell
git fetch
```

Retrieves the latest changes from the remote repository but doesn't automatically merge them.

```shell
git reset <file>
```

Undoes changes in the specified file, removing it from the index.

```shell
git rm <file>
```

Removes a file from the repository and includes it in the next commit.

```shell
git diff
```

Shows the differences between changes that haven't been added to the index yet.

```shell
git remote add <remote-name> <URL>
```

Adds a remote repository with a specific name.

```shell
git push add origin main
```

Executed to push local changes to the online repository.
