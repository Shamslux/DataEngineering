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



