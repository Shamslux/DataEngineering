![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

<div align="left">
  <img src="https://github.com/Shamslux/DataEngineering/assets/79280485/947b9e01-1805-49b2-8aaa-5933bbd2611e" alt="Badge" width="150">
</div>

<div align="right">
  <img src="https://github.com/Shamslux/DataEngineering/assets/79280485/a812dfb8-ebe1-4e47-9204-2f35bc847a1f" alt="Badge" width="150">
</div>

# What is DIO?

DIO is a Brazilian education platform that offers training in various IT areas. Besides courses of various levels, the platform also encourages its community of students and professionals to share knowledge from their study and work routines. With a gamified approach, you can enrich your internal profile with various code challenges, project challenges, and other activities, which, over time, add up to strengthen your professional profile, since the platform brings together a network of recruiters in partnership with DIO, who have access to various profiles of the best and most competent candidates.

# Training Details

The GitHub Certification Program is an educational journey aimed at technology professionals, focusing on essential skills such as version control, collaboration, and administration within the Git and GitHub ecosystem. Across three modules, participants learn to apply modern development practices, manage projects efficiently, and explore innovative products from GitHub. This Training prepares developers, project managers, and system administrators to meet the challenges of software development, offering a competitive advantage and raising productivity and security standards within the GitHub ecosystem and its certifications.

Essentially, this Training promotes an indispensable proficiency in today's technological landscape, transforming you into highly skilled and versatile professionals, ready to implement innovative solutions and lead in complex development environments. It is a strategic investment for those seeking excellence in their careers and a competitive edge in the technology job market.

**Total Course Hours: 10 hours**

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

## A Git Cheat Sheet!

![cheat_sheet](https://github.com/Shamslux/DataEngineering/assets/79280485/ac332ed7-4443-430c-9463-48afc5a42824)

# GitHub Authentication

## USERNAME AND PASSWORD

There are different ways to authenticate on GitHub. One of them is using a username and password, but this option is considered risky for sensitive information. It's recommended to explore other, more secure options available.

## PERSONAL ACCESS TOKENS

PATs (Personal Access Tokens) are like special passwords that replace the use of a normal password when accessing GitHub through the API or the command line. You create this token in the GitHub settings and decide which actions it can perform in a repository or organization. When you use the Git command line to work on GitHub, instead of typing your username and password, you enter this token to authenticate. This makes the interaction more secure and practical.

## SSH KEYS

SSH keys are like special keys that help people connect to remote computers securely, without always having to type a password or token.

When setting up SSH, people create a special key and add it to their profile on GitHub. This key is protected by a "secret phrase" for even more security. They can configure their computer to use this key automatically, or type the "secret phrase" when needed.

It's even possible to use these keys in organizations that use an advanced form of login. If the organization provides special certificates, people can use them to access the repositories without needing to add anything to their GitHub account. In summary, SSH keys make interactions with GitHub more secure and convenient.

## DEPLOYMENT KEYS

Deployment keys are like special keys that allow access to just one specific place on GitHub, like a digital vault. On GitHub, the part of the key that everyone can see is directly connected to the desired location (a repository), while the secret part is kept on your own computer.

These keys are configured to allow read-only access by default, which means you can see what's inside but not modify anything. However, if you also want to make changes, you can configure these keys to have write permission by adding them to the specific location (repository). In summary, they are like digital keys that open the door to a specific place on GitHub, and you decide if you just want to look or also touch things.

## Additional Security Options

### Two-Factor Authentication - 2FA

Two-factor authentication (2FA) is like adding an extra layer of security when you log into websites or apps. In addition to typing your username and password, you need to provide another proof that it's really you.

In the case of GitHub, this extra proof is usually a code generated by an app on your phone or sent via text message. After activating 2FA, whenever someone tries to log into your account, GitHub asks for this additional code. That is, to log in, the person needs not only the password but also the code sent to their phone.

Organization owners on GitHub can require all members or collaborators to activate 2FA on their personal accounts. This makes it harder for malicious people to access important information.

Furthermore, in companies, owners can enforce security rules for all organizations linked to a corporate account, ensuring additional protection for all involved. In summary, it's a way to make things safer on the internet.

### SAML SSO

SAML SSO is a form of security on GitHub that allows for centralized control of access to the organization's resources. Instead of using passwords, users are redirected to a central login system (IdP), like Microsoft Enter ID or Okta. After being authenticated there, they return to GitHub with access to the organization's resources.

This approach simplifies management, as organization owners control who can access what. GitHub supports several popular providers, such as Active Directory, Microsoft Enter ID, and Okta. In summary, it's a more secure and efficient way to manage access to data on GitHub.

### LDPA

LDAP is a protocol used to access and organize information in directories, especially in large companies. In the context of GitHub Enterprise Server, it allows for the integration and centralized management of access to repositories using existing accounts.

GitHub Enterprise Server is compatible with various well-known LDAP services, such as Active Directory, Oracle Directory Server Enterprise Edition, OpenLDAP, and others. In summary, LDAP is a tool that helps in the organization and access control in corporate environments on GitHub.

# Creating a Repository on GitHub

Simply click the button (see the image below) to open the repository creation window (using the features of the GitHub platform).

![repository_click_create](https://github.com/Shamslux/DataEngineering/assets/79280485/a92f5c8f-18a4-49ed-ae08-bb2b5848a4dc)

## Main Steps of Creation

![repository_creating](https://github.com/Shamslux/DataEngineering/assets/79280485/d3edb585-0ec3-4d88-b09a-87b1bcf2f5fe)

1. **Define a name for your repository**

2. **Choose whether you want a README.md (markdown) file to be created**

3. **Choose a license type if desired**

4. **Click the button to finalize and create your repository!**

## Cloning the Repository

![cloning](https://github.com/Shamslux/DataEngineering/assets/79280485/33113993-1966-4a6a-94a2-8514513cee9b)

To clone the repository, after creating it, note that there is a button with the name "<> Code". When you click on it, a box will appear on the screen with some options. One of the most common ways that many developers use is to copy the HTTPS path and then use the command *git clone <URL>* to bring the repository created on the server to the local machine.

# Personal Access Tokens

The GitHub personal access token is a form of authentication used to access resources and perform actions on the GitHub platform on behalf of a user.

## Step-by-Step Guide - Practical:

- Step 1: Create a Personal Access Token

- Access GitHub and go to your profile's "Settings".

- In the side menu, select "Developer settings".

- Click on "Personal access tokens" and then on "Generate token".

- Follow the instructions to configure the necessary permissions and click "Generate token" at the end.

- Copy the generated token.

- Step 2: Clone a Repository Using the Token

- Open Git Bash on your computer.

- In the terminal, use the following command to clone a repository using the token:

```shell
git clone https://YOUR_TOKEN_HERE@github.com/your-username/your-repository.git
```

- Replace YOUR_TOKEN_HERE with the token you copied and your-username/your-repository.git with the path of the repository you want to clone.

For example:

```shell
git clone https://your-token-here@github.com/your-username/my-project.git
```

# Generating SSH Keys

To generate an SSH key, we should open the terminal and use the command:

```shell
ssh-keygen
```

The keys will be saved in the designated location (usually in the user's operating system). A *.ssh* folder will be created with two pairs of keys: one public and one private. We will use the public one *example_file.pub*, the private key should be well protected and kept safe, it's personal and non-transferable.

Note: We can check if we already have SSH keys with the command below in the terminal:

```shell
ls -al ~/.ssh
```

Note²: If we want to be more detailed in the key creation, we can pass the following parameters:

```shell
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

- **-t rsa**: specifies an RSA key type

- **-b 4096**: sets the number of bits in the key, with 4096 bits being a good practice for increased security.

- **-C "your_email@example.com"**: adds a comment pointing to your GitHub email to aid in identification


## Configuring the SSH Key on GitHub

To configure, we should access the "settings" part of GitHub and use the appropriate tab to configure SSH keys. When we click the button to create an SSH key, we will be redirected to the appropriate window to name and insert the data of the public key we generated earlier. See the images below to understand the process.

![ssh_settings](https://github.com/Shamslux/DataEngineering/assets/79280485/99a226e0-7503-4907-b076-5e16db18300b)

![ssh_settings_inside](https://github.com/Shamslux/DataEngineering/assets/79280485/3267da3d-65d5-4fa1-abd0-c73878a822ff)

## Changing the Project URL to SSH instead of HTTPS

If you try to *git push* with authentication via SSH key, however, your remote repository has been cloned via HTTPS, there will be an error. To fix this, we should use the following command:

```shell
git remote set-url origin <SSH URL>
```

After this change, the *pushes* will be accepted with the configured SSH key.



