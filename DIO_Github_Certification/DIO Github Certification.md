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

# Collaboration with GitHub

## First of all, what is a repository?

A repository is the place where all the files of our project are contained. It's like a folder that holds all these project files, such as our software projects. It is with them that we can collaborate, manage our work, track changes, store the history of changes, etc...

## What are Branches?

It is a separate development line in version control. It allows us to work on modifications to the code without directly affecting the main code (usually called the main branch, such as "main" or "master"). This facilitates simultaneous development of features or bug fixes without interfering with the stable code of the main version. After completing the changes in a branch, you can merge these changes back into the main branch.

## And Pull Request and Merge?

A Pull Request (PR) is a common feature in collaborative source code hosting platforms like GitHub. The main purpose of a Pull Request is to propose changes to a repository and request that these changes be reviewed and merged into the main code.

The "merge" is an operation in version control that combines the changes from two different branches. When we finish development on a branch and want to incorporate those changes back into the main branch (or another desired branch), we perform a merge.

## What about Fork?

It is basically a copy of a repository (a software project) from someone else to your own space on GitHub. This allows you to make changes to the code without affecting the original project. If you want to contribute back, you can send a "pull request" for the owner of the original project to consider your changes and incorporate them.

## And Issues?

Issues are used to track tasks, bugs, improvements, or any discussion related to the source code of the project. They provide us with a means of communication and collaboration among team members and the community. Issues can be opened by anyone, including project developers and external users. They serve for discussions, planning, task assignment, and progress tracking.

# Creating a New Branch

We can create branches in two ways. Either we use the platform (see the image below):

![new_branch_with_platform](https://github.com/Shamslux/DataEngineering/assets/79280485/cbb63659-be06-4f54-82ca-fae72a050c13)

Or we can use the following command:

```shell
git branch <branch-name>
```

Then, we need to switch to the newly created branch:

```shell
git checkout <branch-name>
```
# Performing a Merge (without pull request)

In the terminal, simply type the following command:

```shell
git merge <branch-name>
```

Assuming we were on the `main` branch, using the code above, let's say we wanted to merge based on a task called `task_changing_form`, we would have the following code:

```shell
git merge task_changing_form
```

Everything that was changed and tested in the `task_changing_form` branch will now be merged into the `main` branch.

# Performing a Pull Request and a Fork

## Fork

To create a fork, simply visit a page on GitHub of someone you follow and admire, then select the desired repository and click on "fork". A new screen with "create a new fork" will appear and you just need to fill in some data (it looks a bit like creating a repository).

![fork_click](https://github.com/Shamslux/DataEngineering/assets/79280485/43046414-783c-4e16-a864-8091b2bfe69d)

![fork_click_open](https://github.com/Shamslux/DataEngineering/assets/79280485/86a46eff-f231-4342-9618-a7cdb83ebd33)

# Performing a Pull Request and a Fork

## Pull Request

If we use the fork on someone else's repository and make changes, we can then create a Pull Request to the original owner of the repository, suggesting our changes. This user will need to review and approve (or reject) it. If they accept the Pull Request, what we suggested will be merged with the branch of the original repository, and we will thus be contributors to their project as well.

We can also use the Pull Request for modifications in our own repositories. For example, let's remember the use of new branches. If we had a project with the `main` branch and wanted to change something, let's assume we created the `dev-298` branch, after the changes were made, we could create a Pull Request for the `dev-298` to be reviewed by ourselves or another member of our repository, before being merged.

![pull_request](https://github.com/Shamslux/DataEngineering/assets/79280485/c8e1f414-57d8-4247-a818-53d7725b9e0e)

# Tags

We create `tags` using the command:

`git tag -a <tag> -m "<message">`

Then we push the created `tag`:

`git push origin <tag>`

![tag_icon](https://github.com/Shamslux/DataEngineering/assets/79280485/cb36b081-1334-4c82-818b-06047a562114)
***Note**: I don't have tags in my project.*

# Releases

While tags are historical points that can help mark code versions, releases are more refined options for showcasing that version of the code. It also includes a tag and provides more details, in addition to making the files available for download.

To create a release, we should select the base tag and the previous tag, then it's a matter of writing the details before being able to publish it.

![release_window](https://github.com/Shamslux/DataEngineering/assets/79280485/bb6743e7-55eb-4e59-8ded-664e60cc1efb)

# What are Gists?

Gists are a feature of GitHub that allow you to share snippets of code, text, or markdown files with others. They are like small repositories but are often used for sharing single files or pieces of code rather than entire projects.

## Key Features:

- **Code Sharing**: Gists are commonly used to share small snippets of code with others, either for collaboration or demonstration purposes.

- **Version Control**: Like regular repositories, Gists support version control using Git. This means you can fork, clone, and pull Gists just like you would with a regular repository.

- **Markdown Support**: Gists can contain Markdown files, making them suitable for sharing formatted text, documentation, or even blog posts.

- **Privacy Options**: You can choose whether a Gist should be public or private. Public Gists are visible to anyone, while private Gists are only accessible to you or selected collaborators.

## Common Use Cases:

- **Sharing Code Snippets**: Quickly share small pieces of code with others, whether it's for troubleshooting, asking for help, or showcasing a particular technique.

- **Embedding in Documentation**: Use Gists to embed code examples or formatted text in your documentation or README files.

- **Collaborative Editing**: Collaborate on small coding tasks or fixes by sharing Gists with team members or collaborators.

## How to Create a Gist:

1. **Visit GitHub**: Go to the Gists section of your GitHub profile or directly to gist.github.com.

2. **Create a New Gist**: Click on the "New gist" button.

3. **Add Files**: Enter the content of your Gist, including code, text, or Markdown files.

4. **Configure Settings**: Choose whether the Gist should be public or private, add a description, and select the syntax highlighting for code files.

5. **Create Gist**: Click the "Create public gist" or "Create secret gist" button to finalize and create your Gist.

![pre-creating_gist](https://github.com/Shamslux/DataEngineering/assets/79280485/4eab483b-5560-497e-b525-8858b9b1113e)

![gist_created](https://github.com/Shamslux/DataEngineering/assets/79280485/b740a548-1601-40b7-884e-7d63ed99ae94)

# GitHub Issues

GitHub Issues are a fundamental tool for tracking tasks, bugs, enhancements, and discussions related to a software project hosted on GitHub. They enable effective and collaborative communication among team members and the developer community. Below are the key points about issues:

- **Definition:** Issues are like virtual tickets that can be opened by anyone, including project developers and external users.

- **Purpose:** They are used to discuss ideas, report bugs, request new features, propose enhancements, assign tasks, and track the progress of software development.

- **Characteristics:** Each issue has a descriptive title summarizing the problem or task, along with a more detailed description. They can also be assigned to team members, labeled with tags for categorization and organization, and marked with milestones to indicate their status in relation to specific software versions.

- **Comments:** Team members and collaborators can add comments to issues to provide feedback, clarify questions, and discuss solutions.

- **Workflow:** The typical workflow involves opening an issue, discussing the problem or task, assigning responsibilities, implementing the solution, and closing the issue when completed.

- **References in Commits:** Issues can be linked to specific commits, allowing developers to track the progress of an issue directly in the commit history.

## Resolving an Issue

When committing changes that address an issue, simply use the keyword `fixed` followed by `#<issue-number>` in the commit message.

Example: `update my-python.py fixed #567`

This will automatically close the corresponding issue when the commit is merged into the main branch.

# GitHub Wiki

GitHub Wiki is a collaborative space where users can create and share documentation, guides, and other content related to a project. Here are the key points about GitHub Wiki:

- **Definition:** A Wiki is a section within a GitHub repository dedicated to storing and organizing documentation, tutorials, FAQs, and any other information related to the project.

- **Purpose:** It serves as a centralized knowledge base for project contributors and users to access relevant information, instructions, and resources.

- **Features:** Users can create and edit Wiki pages using Markdown syntax, making it easy to format text, add images, and create links. The Wiki's revision history allows for tracking changes and reverting to previous versions if needed.

- **Collaboration:** Multiple contributors can collaborate on Wiki pages, making it a valuable resource for documenting project details, best practices, and troubleshooting guides.

- **Accessibility:** Wiki pages can be accessed directly from the repository's main page, providing easy navigation for users seeking information about the project.

- **Integration:** GitHub Wikis can be integrated with other project management tools and workflows, enhancing collaboration and knowledge sharing among team members.

- **Versioning:** Like other content in a GitHub repository, Wiki pages are version-controlled, allowing users to view and revert changes as necessary.

- **Customization:** Repository owners can customize the Wiki's settings, including permissions for editing and viewing, to suit the project's needs and ensure content integrity.

GitHub Wiki is a powerful tool for creating and maintaining project documentation, enabling effective communication and collaboration among project stakeholders.

![wiki](https://github.com/Shamslux/DataEngineering/assets/79280485/5a09248d-057a-4d72-9639-cab055297af6)

# GitHub Search

GitHub offers powerful search capabilities that allow users to find specific content within repositories, issues, pull requests, users, and more. 

GitHub's search tool is a valuable resource for developers, project managers, and users seeking to explore and discover content within the GitHub ecosystem. With its comprehensive search capabilities and advanced features, users can quickly find the information they need to support their projects and collaboration efforts.

Here's a clear and concise explanation of GitHub's search tool:

- **User Account Search:** Users can search within their own GitHub account to find repositories, issues, pull requests, and other content related to their projects. This feature enables users to quickly locate specific files, code snippets, or discussions within their repositories.

- **Global Search:** GitHub's global search functionality allows users to search across all public repositories on the platform. Users can specify search criteria such as keywords, file names, repository names, programming languages, and more to narrow down the search results.

- **Search Filters:** GitHub provides various search filters to refine search queries and target specific types of content. Users can filter search results by repository, user, organization, file extension, code language, and more to find the most relevant information.

- **Advanced Search Syntax:** GitHub supports advanced search syntax, including boolean operators, qualifiers, and wildcards, to perform complex search queries. Users can use operators like "AND," "OR," and "NOT" to combine search terms and refine search results further.

- **Code Search:** GitHub's code search feature allows users to search for specific code snippets or files within repositories. Users can specify search terms, file paths, and code language to find relevant code samples quickly.

- **Issue and Pull Request Search:** Users can search for specific issues and pull requests using keywords, labels, assignees, and other criteria. This feature is particularly useful for project management and collaboration, allowing users to track and resolve issues efficiently.

- **Saved Searches:** GitHub allows users to save frequently used search queries for quick access. Saved searches can be organized and managed within the user's account settings, making it easy to revisit important search results.

![git_search](https://github.com/Shamslux/DataEngineering/assets/79280485/d784a6fe-fbe2-4055-be35-d363823a2816)

# Markdown Formatting

In this lesson, we'll discover the structure and syntax of Markdown. We'll also explore GitHub-Flavored Markdown (GFM) features, which are syntax extensions that allow integrating GitHub's features.

## What is Markdown?

Markdown is a markup language that offers a simplified approach to editing content, shielding content creators from the complexities of HTML. While HTML is excellent for rendering content exactly as intended, it can be space-consuming and challenging to work with, even in small doses. The invention of Markdown offered a great balance between HTML's power for content description and the simplicity of plain text for editing.

## Structure and Syntax of Markdown

In this unit, we'll discuss the structure and syntax of Markdown. We'll also cover GitHub-Flavored Markdown (GFM) features, which are syntax extensions that allow integrating GitHub features into content.

## Syntax

**Emphasizing Text**

The most important part of any communication on GitHub is often the text itself, but how do we show that some parts of the text are more important than others?

Using italics in the text is as easy as surrounding the target text with a single asterisk (*) or a single underscore (_). Just make sure to close an emphasis with the same character you opened it with. Be mindful of combining asterisks and underscores. Here are some examples:

Markdown:

```markdown
This is *italic* text.
This is also _italic_ text.
```

Output:

This is *italic* text.
This is also _italic_ text.

Create bold text using two asterisks (**) or two underscores (__).

Markdown:

```markdown
This is **bold** text.
This is also __bold__ text.
```

Output:

This is **bold** text.
This is also __bold__ text.

You can also mix different emphases.

Markdown:

```markdown
_This is **italic and bold**_ using a single underscore for italic and two asterisks for bold.
__This is bold and *italic*__ using two underscores for bold and a single asterisk for italic.
```

Output:

_This is **italic and bold**_ using a single underscore for italic and two asterisks for bold.
__This is bold and *italic*__ using two underscores for bold and a single asterisk for italic.

To use a literal asterisk, precede it with an escape character; in GFM, this is a backslash (\). This example results in underscores and asterisks being displayed in the output.

Markdown:

```markdown
\_This is all \*\*simple text\*\*.
```

Output:

\_This is all \*\*simple text\*\*.

**Declaring Headers**

HTML provides content headers, such as the `<h1>` tag. In Markdown, this is supported via the symbol `#`. Simply use a `#` for each header level from 1 to 6.

Markdown:

```markdown
###### This is H6 text
```

Output:

###### This is H6 text

**Linking to Images and Websites**

Image and website links use similar syntax.

Markdown:

```markdown
![Link to an image.](/learn/azure-devops/shared/media/mara.png)
```

Output:

![Link to an image.](/learn/azure-devops/shared/media/mara.png)

Markdown:

```markdown
[Link to Microsoft Training](/training)
```

Output:

[Link to Microsoft Training](/training)

**Creating Lists**

You can define ordered or unordered lists. It's also possible to define nested items through indentation.

Ordered lists start with numbers. Unordered lists can use asterisks or dashes (-).

Here's the Markdown for an ordered list:

Markdown:

```markdown
1. First
1. Second
1. Third
```

Output:

1. First
2. Second
3. Third

Markdown:

```markdown
- First
  - Nested
- Second
- Third
```

Output:

- First
  - Nested
- Second
- Third

Here's the Markdown for an unordered list:

Markdown:

```markdown
- First
  - Nested
- Second
- Third
```

Output:

- First
  - Nested
- Second
- Third

**Building Tables**

You can build tables using a combination of vertical bars (|) for column breaks and dashes (-) to designate the row above as the header.

Markdown:

```markdown
First | Second
-|-
1 | 2
3 | 4
```

Output:

First | Second
-|-
1 | 2
3 | 4

**Quoting Text**

You can create block quotes using the greater than symbol (>).

Markdown:

```markdown
> This is quoted text.
```

Output:

> This is quoted text.

**Fill in the blanks with Inline HTML**

If you encounter an HTML scenario not supported by Markdown, you can use inline HTML.

Markdown:

```markdown
Here's a<br />line break
```

Output:

Here's a<br />line break

**Working with Code**

Markdown provides default behavior for working with inline code blocks delimited by the backtick character (`). By decorating the text with this character, it's rendered as code.

Markdown:

```markdown
This is `code`.
```

Output:

This is `code`.

If you have a code segment spanning multiple lines, you can use three backticks (```) before and after to create a surrounded code block.

```markdown
var first = 1;
var second = 2;
var sum = first + second;
```

```csharp
var first = 1;
var second = 2;
var sum = first + second;
```

GFM extends this support with syntax highlighting for popular languages. Just specify the language as part of the first sequence of backticks.

```javascript
var first = 1;
var second = 2;
var sum = first + second;
```

```csharp
JavaScript 

var first = 1;
var second = 2;
var sum = first + second;
```

**Linking Issues and Pull Requests**

GFM supports various shortcode formats to easily link to issues and pull requests. The easiest way to do this is to use the #ID format, such as #3602. GitHub automatically adjusts longer links to this format if you paste them. There are also additional conventions you can follow if you're working with other tools or want to specify other projects/branches.

Reference type | Raw reference | Short link
--- | --- | ---
Issue or pull request URL | https://github.com/desktop/desktop/pull/3602 | #3602
Issue or pull request number | #3602 | #3602
GH- and issue or pull request number | GH-3602 | GH-3602
Username/Repository# and issue or pull request number | desktop/desktop#3602 | desktop/desktop#3602

**Linking Specific Commits**

You can link to a commit by pasting its ID or simply using its secure

 hash algorithm (SHA).

Reference type | Raw reference | Short link
--- | --- | ---
Commit URL | https://github.com/desktop/desktop/commit/8304e9c271a5e5ab4fda797304cd7bcca7158c87 | 8304e9c
SHA | 8304e9c271a5e5ab4fda797304cd7bcca7158c87 | 8304e9c
User@SHA | desktop@8304e9c271a5e5ab4fda797304cd7bcca7158c87 | desktop@8304e9c
Username/Repository@SHA | desktop/desktop@8304e9c271a5e5ab4fda797304cd7bcca7158c87 | desktop/desktop@8304e9c

**Mentioning Users and Teams**

Typing an @ symbol followed by a GitHub username sends a notification to that person about the comment. This is called "@mentioning" because you're mentioning the individual. You can also @mention teams within an organization.

Markdown:

```markdown
@githubteacher
```

Output:

@githubteacher

**Tracking Task Lists**

You can create task lists within issues or pull requests using the following syntax. This can be useful for tracking progress when used in the body of an issue or pull request.

Markdown:

```markdown
- [x] First task
- [x] Second task
- [ ] Third task
```

Output:

- [x] First task
- [x] Second task
- [ ] Third task

**Slash Commands**

Slash commands can save time by reducing the typing required to create complex Markdown.

You can use slash commands in any description or comment field in issues, pull requests, or discussions where that slash command is supported.

Command | Description
--- | ---
/code | Inserts a Markdown code block. You choose the language.
/details | Inserts an expandable details area. You choose the title and content.
/saved-replies | Inserts a saved reply. You choose from saved replies for your user account. If you add %cursor% to your saved reply, the slash command places the cursor at that location.
/table | Inserts a Markdown table. You choose the number of columns and rows.
/tasklist | Inserts a task list. This slash command only works in an issue description.
/template | Shows all templates in the repository. You choose the template to insert. This slash command works for issue templates and a pull request template.

# GitHub Accounts and Plans

In this section, we'll delve into GitHub account types and plans, highlighting the distinctions between them.

## GitHub Account Types

GitHub offers three primary types of accounts:

1. **Personal**: Every individual who uses GitHub.com has a personal account, also known as a user account. This account serves as their identity on the platform and includes a username and profile.

2. **Organization**: Organization accounts are shared accounts where multiple individuals can collaborate across various projects simultaneously. Unlike personal accounts, permissions within organization accounts follow a tiered approach.

3. **Enterprise**: Enterprise accounts on GitHub.com enable administrators to centrally manage policies and billing for multiple organizations. These accounts facilitate inner sourcing between organizations within an enterprise.

Now, let's explore each account type in detail.

## Personal Accounts

Personal accounts are individual accounts used by users on GitHub.com. These accounts own resources such as repositories, packages, and projects. Personal accounts can be either GitHub Free or GitHub Pro.

- **GitHub Free**: Offers unlimited public and private repositories and unlimited collaborators, albeit with some limitations on feature sets for private repositories.
  
- **GitHub Pro**: Similar to GitHub Free but with enhanced features such as GitHub Support via email and increased GitHub Actions minutes.

## Organization Accounts

Organization accounts are shared accounts used by teams to collaborate across projects. Permissions within organization accounts are managed through team access controls, and each person signs in with their personal account. Organization accounts can own repositories, packages, and projects.

## Enterprise Accounts

Enterprise accounts allow administrators to manage policies and billing for multiple organizations centrally. These accounts promote collaboration between organizations within an enterprise and offer additional security and compliance controls.

## GitHub Plans

GitHub offers several plans to improve software management processes and team collaboration:

1. **GitHub Free**: Provides basic features for individuals and organizations, including unlimited public and private repositories.

2. **GitHub Pro**: Offers advanced tools and insights for individual developers, including GitHub Support via email and additional GitHub Actions minutes.

3. **GitHub Team**: Similar to GitHub Pro but tailored for organizations, providing increased GitHub Actions minutes and extra GitHub Packages storage.

4. **GitHub Enterprise**: Offers a greater level of support and additional security, compliance, and deployment controls for organizations.

Within GitHub Enterprise, there are two options:

- **GitHub Enterprise Server**: A self-hosted solution that allows organizations full control over their infrastructure.
  
- **GitHub Enterprise Cloud**: A cloud-based solution with increased GitHub Actions minutes and GitHub Packages storage, along with a service level agreement for monthly uptime.

Each plan offers a unique set of features and benefits tailored to different user needs and organizational requirements.

# GitHub Mobile and GitHub Desktop

In addition to the website github.com, there are other ways to access your GitHub account. With GitHub Mobile and GitHub Desktop, you can have an easy-to-use experience from anywhere.

Let's take a quick look at GitHub Desktop and GitHub Mobile, and what they offer.

## GitHub Mobile

GitHub Mobile allows you to perform important tasks on GitHub quickly and from anywhere. It's a secure way to access your GitHub data through an official and trusted app.

With GitHub Mobile, you can:

- Manage notifications from github.com.
- Read, review, and collaborate on issues and pull requests.
- Edit files in pull requests.
- Search, browse, and interact with users, repositories, and organizations.
- Receive notifications when your username is mentioned.
- Schedule notifications for specific times.
- Secure your account with two-factor authentication.
- Check login attempts from unrecognized devices.

## GitHub Desktop

GitHub Desktop is a tool that makes managing your projects on GitHub directly from your computer easier. With GitHub Desktop, you can:

- Perform basic operations such as cloning, committing, and pushing changes.
- View and switch between branches easily.
- Collaborate with others on shared projects.

# GitHub Billing

Each account, whether personal or organizational, receives a separate invoice. This invoice combines subscription costs and usage-based products.

- Subscriptions cover the plan (such as GitHub Pro or GitHub Team) and fixed-cost monthly paid products, such as GitHub Copilot and GitHub Marketplace apps.

- Usage-based billing applies when the cost of a product depends on how much you use it. For example, GitHub Actions costs based on the minutes used and storage consumed.

**Note:** Your plan may include a certain amount of free usage-based products. With GitHub Pro, your personal account has 3,000 free minutes of GitHub Actions per month. You control additional expenses by setting limits.

# Introduction to GitHub Copilot 🤖

![copilot](https://github.com/Shamslux/DataEngineering/assets/79280485/5eadf0e7-b92c-45c0-9730-26113cfab3ba)

GitHub Copilot is an AI coding partner that provides autocomplete suggestions while you code. Get suggestions by typing code or describing it in natural language.

## But what exactly is GitHub Copilot?

GitHub Copilot is a service that provides an AI programmer as a partner, compatible with all popular programming languages, and dramatically accelerates overall developer productivity. In recent research, GitHub and Microsoft found that developers experience a significant increase in productivity when working on real-world projects and tasks using GitHub Copilot. In fact, in less than two years since its launch, developers experienced the following when using GitHub Copilot:

- 46% of new code is now written by AI.
- 55% increase in overall developer productivity.
- 74% of developers feel more focused on satisfying work.

Developed in collaboration with OpenAI, GitHub Copilot is powered by OpenAI Codex, an AI system created by OpenAI. OpenAI Codex has broad knowledge of how people use code and is more capable than GPT-3 in generating code, in part because it was trained on a dataset that includes a higher concentration of public source code.

GitHub Copilot is available as an extension for Visual Studio Code, Visual Studio, Vim/Neovim, and JetBrains' suite of integrated development environments (IDEs).

## GitHub Copilot Features

GitHub Copilot has initiated a new era in software development as an AI programmer that keeps developers in flow, autocompleting comments and code, but AI-powered autocompletion was just the starting point. Here are some features of GitHub Copilot that truly make it a developer tool of the future, surpassing just being an editor and becoming a readily accessible AI assistant throughout the development cycle.

- **ChatGPT-like Experience in Your Editor with GitHub Copilot Chat:**
GitHub Copilot brings a chat interface to the editor focused on developer scenarios and natively integrates with VS Code and Visual Studio. It recognizes the code a developer has typed, which error messages are displayed, and is deeply integrated with the IDE. A developer can get detailed insights and explanations about what code blocks intend to do, generate unit tests, and even get proposed bug fixes.

- **Copilot for Pull Requests:**
This new feature is powered by the new GPT-4 model from OpenAI and adds support for AI-powered tags in pull request descriptions via a GitHub app that organization admins and individual repository owners can install. These tags are automatically filled in by GitHub Copilot based on the changed code. Developers can review or modify the suggested description.

- **AI-Generated Documentation Responses:**
GitHub is rolling out GitHub Copilot for Docs, an experimental tool that uses a chat interface to provide users with AI-generated responses to documentation questions, including questions that developers have about the languages, frameworks, and technologies they are using.

- **Copilot for Command Line Interface (CLI):**
In addition to the editor and pull request, the terminal is where developers spend most of their time. However, even the most proficient developers need to scroll through many pages to recall the precise syntax of many commands. GitHub Copilot CLI can compose commands and loops, and utilize obscure search flags to fulfill your query.

## GitHub Copilot Business

GitHub Copilot is available through personal GitHub accounts with GitHub Copilot Individual, or through organization or enterprise accounts with GitHub Copilot Business and GitHub Copilot Enterprise.

Copilot Business allows you to control who can use GitHub Copilot in your company. After granting access to an organization, its administrators can then grant access to individuals and teams.

With Copilot Business, GitHub Copilot is open to all developers, teams, and organizations, and businesses.

With features such as code completion, IDE and mobile chat, security vulnerability filtering, code reference, public code filtering, IP and security indemnification, enterprise-level privacy, GitHub Copilot Business aims to make organizations more productive, secure, and satisfied. These features enable developers to code more quickly and focus on more satisfying work.

## GitHub Copilot Enterprise

GitHub Copilot Enterprise is available to organizations through GitHub Enterprise Cloud.

Copilot Enterprise allows your development teams to quickly familiarize themselves with your codebase, search and build documentation, receive suggestions based on internal and private code, and quickly review pull requests.

GitHub Copilot Enterprise includes everything in GitHub Copilot Business, plus an additional layer of customization for organizations and integration with GitHub as a chat interface to allow developers to discuss their codebase and action buttons across the platform. GitHub Copilot Enterprise can index an organization's codebase for deeper understanding of customer knowledge for more personalized suggestions and provide customers access to GitHub Copilot Customization to adjust custom and private models for code completion.

>> **Set up, configure, and troubleshoot GitHub Copilot**
Please note that when signing up for the GitHub Copilot free trial, you will be asked to provide a payment method, although you will not be charged until the end of the free trial. Be sure to cancel before 30 days to avoid payment.

## Sign Up for GitHub Copilot

Before you begin using GitHub Copilot, you need to set up a free trial or subscription for your personal account.

Select your profile picture, then select Settings. Copilot is in the menu on the left, under Code, Planning, and Automation.

After signing up, you will need to install an extension for your preferred environment. GitHub Copilot is compatible with GitHub.com, Visual Studio Code, Visual Studio, JetBrains IDEs, and Neovim as a discreet extension.

## Configure GitHub Copilot in Visual Studio Code

*Add Visual Studio Code Extension*

Follow these steps to add the Visual Studio Code extension for GitHub Copilot.

In the Visual Studio Code Marketplace, go to the GitHub Copilot extension page and select Install.

A popup will appear asking to open Visual Studio Code. Select Open.

In the Extension: GitHub Copilot tab in Visual Studio Code, select Install.

If you have not previously authorized Visual Studio Code in your GitHub account, you will be asked to log in to GitHub in Visual Studio Code. Select Log in to GitHub.

GitHub Copilot can autocomplete code as you type when using Visual Studio Code. After installation, you can activate or deactivate GitHub Copilot and configure advanced settings within Visual Studio Code.

## Enable or Disable GitHub Copilot in Visual Studio Code

To enable or disable GitHub Copilot, select the status icon in the bottom panel of the Visual Studio Code window.

Screenshot of the status icon for GitHub Copilot in the bottom panel of the Visual Studio Code window. The background color corresponds to the color of the status bar when activated.

When turning off GitHub Copilot, you will be asked whether you want to turn off suggestions globally or for the file language you are currently editing.

To disable GitHub Copilot suggestions globally, select Disable globally.

To disable GitHub Copilot suggestions for a specific language, select Disable for LANGUAGE.

## Enable or Disable Inline Suggestions in Visual Studio Code

In the File menu, go to Preferences and select Settings.

Screenshot of the File menu in Visual Studio Code. The Preferences dropdown is open with Settings selected.

In the left panel of the Settings tab, select Extensions, and then select Copilot.

Under Inline Suggest: Enable, select or deselect the checkbox to enable or disable inline suggestions.

Additionally, you can choose to enable or disable inline suggestions and specify for which languages you want to enable or disable GitHub Copilot.

## Troubleshoot GitHub Copilot in Visual Studio Code

In Visual Studio Code, log files are useful for diagnosing connection issues. The GitHub Copilot extension stores log files in the default location for

# Introduction to Codespaces

Let's understand a bit about the lifecycle of Codespaces

GitHub Codespaces is a fully configured development environment hosted in the cloud. When using GitHub Codespaces, your workspace, along with all your configured development environments, are available on any computer with internet access.

## The Codespace Lifecycle

![codespace](https://github.com/Shamslux/DataEngineering/assets/79280485/fcf4f622-aee1-4a76-b994-0437cbb6b490)

GitHub Codespaces is configurable, allowing you to create a custom development environment for your project. By setting up a custom development environment for your project, you can have a repeatable Codespace configuration for all users of your project.

The lifecycle of a Codespace begins when you create a Codespace and ends when you delete it. You can disconnect and reconnect to an active Codespace without affecting your running processes. You can stop and restart a Codespace without losing changes made to your project.

## Create a Codespace

You can create a Codespace on GitHub.com, in Visual Studio Code, or using the GitHub CLI. There are four ways to create a Codespace:

1. From a GitHub template or any repository in GitHub.com to start a new project.

2. From a branch in your repository for new feature work.

3. From an open pull request to explore work in progress.

4. From a commit in a repository's history to investigate a bug at a specific point in time.

You can temporarily use a Codespace to test code, or you can return to the same Codespace to work on long-running features.

You can create more than one Codespace per repository or even per branch. However, there are limits to the number of Codespaces you can create and run simultaneously. If you reach the maximum number of Codespaces and try to create another one, you'll see a message informing you that an existing Codespace needs to be removed/deleted before a new one can be created.

You can create a new Codespace whenever you develop on GitHub Codespaces or keep a long-running Codespace for a feature. If starting a new project, create a Codespace from a template and later publish it to a repository on GitHub.

When creating a new Codespace each time you work on a project, you should regularly push your changes to ensure any new commits are on GitHub. When using a long-running Codespace for a new project, pull from the default branch of the repository whenever you start working in the Codespace. This allows the environment to get the latest commits. The workflow is similar to working with a project on a local machine.

Repository administrators can enable GitHub Codespaces prebuilds for a repository to speed up Codespace creation.

## Codespace Creation Process:

![codespace-2](https://github.com/Shamslux/DataEngineering/assets/79280485/2191c154-8a33-4d62-909f-a5fea66664d8)

When creating a GitHub Codespace, four processes occur:

1. VM and storage are assigned to your Codespace.
2. A container is created.
3. A connection to the Codespace is made.
4. A post-creation setup is made.

## Save Changes in a Codespace

When you connect to a Codespace via the web, AutoSave is automatically activated to save changes after a specific period of time. When connecting to a Codespace through Visual Studio Code running on your desktop, you must enable AutoSave.

Your work is saved on a virtual machine in the cloud. You can close and stop a Codespace and return to the saved work later. If you have unsaved changes, you'll receive a prompt to save them before exiting. However, if your Codespace is deleted, your work will be lost. To save your work, you must commit your changes and push them to your remote repository or publish your work to a new one if you created your Codespace from a template.

## Open an Existing Codespace

You can reopen any of your active or stopped Codespaces on GitHub.com, in a JetBrains IDE, in Visual Studio Code, or using GitHub CLI.

To resume an existing Codespace, you can go to the repository where the Codespace exists and press the "," key on the keyboard and select "Resume this codespace" or open https://github.com/codespaces in the browser, select the repository, and then select the existing Codespace.

## Timeouts for a Codespace

If a Codespace is inactive, or if you exit the Codespace without explicitly stopping it, the app will expire after a period of inactivity and stop running. The default timeout period is after 30 minutes of inactivity. You cannot customize the duration of the timeout period for new Codespaces. When a Codespace expires, your data is retained since the last time your changes were saved.

## Internet Connection when using GitHub Codespaces

A Codespace requires an internet connection. If the internet connection is lost while you're working in a Codespace, you won't be able to access your Codespace. However, any uncommitted changes will be saved. Upon restoring the internet connection, you can access the Codespace in the same state as it was when the connection was lost.

If you have an unstable internet connection, you should commit and push your changes frequently.

## Closing or Stopping a Codespace

If you exit the Codespace without running the stop command (e.g., by closing the browser tab) or leave the Codespace running without interaction, the Codespace and its running processes will continue during the idle timeout period. The default idle timeout period is 30 minutes. You can set your personal timeout configuration for created Codespaces, but this can be overridden by an organization's timeout policy.

Only running Codespaces incur CPU charges. A stopped Codespace incurs only storage costs.

You can stop and restart a Codespace to apply changes. For example, if you change the machine type used for your Codespace, you'll need to stop it and restart it for the change to take effect. When you close or stop your Codespace, all uncommitted changes are preserved until you connect to the Codespace again.

You can also stop the Codespace and choose to restart or delete it if you encounter an error or something unexpected.

## Rebuilding a Codespace

You can rebuild your Codespace to implement changes in the development container configuration. For most uses, creating a new Codespace is possible as an alternative to rebuilding a Codespace. When rebuilding your Codespace, cached images speed up the rebuilding process. You can also perform a full rebuild to clear the cache and rebuild the container with new images.

When rebuilding the container in a Codespace, changes made outside the /workspaces directory are cleared. Changes made within the /workspaces directory, including the clone of the repository or template from which you created the Codespace, are preserved during a rebuild.

## Delete a Codespace

You can create a Codespace for a specific task. After pushing your changes to a remote branch, you can safely delete that Codespace.

If you try to delete a Codespace with unsent git commits, the editor will notify that there are changes that have not been sent to a remote branch.

You can send any desired changes and delete your Codespace. You can also proceed to delete your Codespace and any uncommitted changes or export the code to a new branch without creating a new Codespace.

Inactive Codespaces that remain idle for a specified period of time are automatically deleted. Idle Codespaces are deleted after 30 days, but you can customize Codespace retention intervals.

# Customizing your Codespace

GitHub Codespaces is a dedicated environment for you. You can configure your repositories with a development container to define your GitHub Codespaces environment.

## Tips for customizing your Codespace

There are many ways to customize your Codespace. Let's understand each of them:

- **Settings Sync:** You can synchronize Visual Studio Code (VS Code) settings between the desktop application and the VS Code web client.

- **Dotfiles:** You can use a dotfiles repository to specify scripts, shell preferences, and other configurations.

- **Rename a Codespace:** When you create a Codespace, it gets an automatically generated display name. If you have multiple Codespaces, the display name will help differentiate between Codespaces.

- **Change your shell:** You can change your shell in a Codespace to maintain the configuration you're accustomed to. While working in a Codespace, you can open a new terminal window with a shell of your choice, change your default shell for new terminal windows, or install a new shell. You can also use dotfiles to configure your shell.

- **Change machine type:** You can change the machine type running your Codespace to use appropriate resources for the work you're doing.

- **Set default editor:** You can set your default editor for Codespaces on your personal settings page. Set your editor preference so that when you create a Codespace or open an existing Codespace, it opens in your default editor.

   - Visual Studio Code (desktop application)
   - Visual Studio Code (web client app)
   - JetBrains Gateway - to open Codespaces in a JetBrains IDE
   - JupyterLab - the web interface of the Jupyter Project

- **Set default region:** You can set your default region on the GitHub Codespaces profile settings page to customize where your data is kept.

- **Set timeout:** A Codespace will stop functioning after a period of inactivity. By default, this period is 30 minutes, but you can specify a longer or shorter default timeout period in your personal GitHub settings. The updated setting applies to any new Codespaces you create or existing Codespaces the next time you start them.

- **Set up auto-delete:** Inactive Codespaces are automatically deleted. You can choose how long your stopped Codespaces will be retained, up to a maximum of 30 days.

## Add to your Codespace with extensions or plugins

You can add plugins and extensions in a Codespace to customize your experience in JetBrains and VS Code.

**VS Code extensions**

If you work in your Codespaces in the VS Code desktop application or web client, you can add any necessary extensions from the Visual Studio Code Marketplace. Refer to Remote Development Support and GitHub Codespaces in the VS Code documentation for information on how extensions run in GitHub Codespaces.

If you already use VS Code, you can use Settings Sync to automatically synchronize extensions, settings, themes, and keyboard shortcuts between your local instance and any Codespaces you create.

**JetBrains plugins**

If you work in your Codespaces in a JetBrains IDE, you can add plugins from the JetBrains Marketplace.

# Codespaces X GitHub.dev

You're probably wondering: when should I use GitHub Codespaces and when should I use GitHub.dev?

You can use GitHub.dev to browse through files and source code repositories on GitHub and make and commit code changes. You can open any repository, branch, or pull request in the GitHub.dev editor.

If you want to do heavier work, such as testing your code, use GitHub Codespaces. It has associated computing so you can build your code, run it, and have access to the terminal. GitHub.dev does not contain computing. With GitHub Codespaces, you get the power of a personal virtual machine (VM) with access to the terminal, just like you would use your local environment, but in the cloud. Codespaces vs GitHub.dev Comparison

The following table lists the main differences between Codespaces and GitHub.dev:

|                     | GitHub.dev                                   | GitHub Codespaces                          |
|---------------------|----------------------------------------------|--------------------------------------------|
| **Costs**           | Free                                         | Free tier usage quota for personal accounts |
| **Availability**    | Available for everyone on GitHub.com        | Available for everyone on GitHub.com       |
| **Start**           | GitHub.dev opens instantly with a key press | When you create or resume a Codespace, a VM is assigned to the Codespace and the container is configured based on the content of a devcontainer.json file. This setup takes a few minutes to create the development environment. |
| **Computing**       | No computing associated, so you cannot build and run your code or use the integrated terminal | With GitHub Codespaces, you get the power of a dedicated VM to run and debug your application. |
| **Terminal Access** | None                                         | GitHub Codespaces provides a common set of tools by default, meaning you can use the Terminal exactly as you would in your local environment. |
| **Extensions**      | Only a subset of extensions that can run on the web appear in the extensions view and can be installed | With GitHub Codespaces, you can use most extensions from the Visual Studio Code Marketplace. |

## Continue working with Codespaces

You can start your workflow in GitHub.dev and continue working in a Codespace. If you try to access the Run, Debug, or Terminal view, you will be notified that they are not available in GitHub.dev.

To continue your work in a Codespace, select Continue working on.... Select Create new codespace to create a codespace in your current branch. Before choosing this option, you should confirm any changes.