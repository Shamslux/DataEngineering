<a href="https://www.goodreads.com/user/show/50697219-jo-o-paulo-m-ller-mamede">
    <img src="https://img.shields.io/badge/Goodreads-372213?style=for-the-badge&logo=goodreads&logoColor=white" alt="Goodreads Badge"/>
  </a>
  <img src="https://upload.wikimedia.org/wikipedia/commons/1/13/United-kingdom_flag_icon_round.svg" width=25 height=25/> 
  
## Table of Contents

Please check the three side bars displayed on the above right corner of the screen. Click there and GitHub already produces a ToC automatically for this MD file.

# AWS Certified Cloud Practitioner Exam Guide by Rajesh Daswani

<img src="https://m.media-amazon.com/images/I/41I21sU8XsL.jpg"/> 

# Summary

So, this is another summary of another useful book. I am resuming it since I am to take soon the AWS most basic exam in September.

# CHAPTER 1 - WHAT IS CLOUD COMPUTING

## INTRODUCTION

Cloud computing has become the preferred method for building IT applications worldwide. In the past, companies had to invest in their own infrastructure and hire developers, which was costly and inflexible. However, with cloud computing, businesses can save money, be more innovative, and easily scale their solutions. IT professionals need to learn about cloud computing to stay relevant and deliver efficient solutions. Cloud computing offers various models and deployment options, and understanding them is crucial for creating effective cloud strategies. Virtualization plays a vital role in making cloud computing possible.

In cloud computing, companies access IT services like computing power, storage, and software from third-party providers via the internet. Instead of managing their own infrastructure, they can rent these services from providers like Amazon Web Services (AWS). Cloud computing has been around for a while, with early examples like Hotmail. Today, AWS is a major cloud provider offering cost-effective, secure, and reliable IT solutions, making it a popular choice for many companies and startups.

## THE SIX ADVANTAGES OF CLOUD COMPUTING

Cloud computing offers several advantages for businesses:

1. **Cost savings**: Instead of investing in expensive infrastructure upfront, companies can pay only for the resources they actually use, reducing capital expenses. This flexibility allows businesses to allocate funds to other important areas.

2. **Economies of scale**: Cloud providers like AWS can offer lower prices because they host infrastructure for many customers and have greater buying power.

3. **Improved capacity planning**: Cloud computing allows businesses to scale their infrastructure automatically based on demand, avoiding overprovisioning or underprovisioning resources.

4. **Increased speed and agility**: Cloud vendors like AWS enable quick provisioning of IT resources, allowing organizations to launch applications faster and respond to changing needs more efficiently.

5. **Reduced data center costs**: By using cloud services, businesses can eliminate the need to manage and maintain physical data centers, saving on real estate, power, and maintenance expenses.

6. **Global reach**: Cloud providers have data centers in various regions worldwide, enabling businesses to offer low-latency experiences to customers and ensure compliance with data regulations.

Overall, adopting cloud technologies helps businesses optimize costs, improve scalability, and respond quickly to market demands.

## BASICS ABOUT VIRTUALIZATION

Virtualization is a core technology that revolutionized cloud computing, giving rise to major cloud providers like AWS, Microsoft Azure, and Google Cloud Platform. It enables a wide range of services with high availability, elasticity, and rapid provisioning for customers.

Before virtualization, outsourcing infrastructure involved long lead times to set up physical servers, including CPUs, memory, and storage, along with an operating system and applications.

Advancements in hardware technology have led to powerful physical servers often remaining underutilized. However, software engineering efficiently consumes hardware resources to power applications.

Virtualization allows a single physical server to be emulated as multiple virtual components, deployed as virtual machines (VMs) with their own operating systems and applications.

A hypervisor acts as a bridge between physical hardware and VMs, enabling controlled access and resource isolation. It carves virtualized representations of physical hardware into smaller components presented as VMs.

The key advantage of virtualization is the speedy provisioning of resources. Emulating existing hardware with software reduces lead times for provisioning virtual servers, storage, or network environments significantly.

## VIRTUALIZATION VS CLOUD COMPUTING

Virtualization is a technology that enables cloud computing services but is not cloud computing itself. Cloud providers like AWS utilize virtualization to offer self-service management tools for provisioning virtualized infrastructure resources. These tools include a Management Console, CLI, and APIs, allowing customers to easily provision servers, network, storage, and databases without waiting for manual configuration.

Cloud computing providers leverage virtualization and modern hardware technologies to deliver shared computing resources and Software-as-a-Service (SaaS) products over the internet. They offer elasticity, automation, scalability, and high availability on a pay-as-you-go pricing model, making their services accessible to a wide range of clients globally.

## EXPLORING CLOUD COMPUTING MODELS

Cloud computing offers businesses the opportunity to shift away from managing and hosting applications, with providers offering mainstream applications and bespoke line-of-business (LOB) applications as complete services. Different cloud models cater to specific needs:

1. **Infrastructure as a Service (IaaS)**: Provides flexibility by giving customers access to configure virtualized infrastructure components such as network, storage, and compute services, similar to owning physical infrastructure.

2. **Platform as a Service (PaaS)**: Focuses on application development, removing the burden of managing underlying infrastructure. The provider provisions the necessary infrastructure, with some flexibility in configuration.

3.**Software as a Service (SaaS)**: Applications are fully hosted and managed by the provider, eliminating the need for physical infrastructure setup. Users access applications via the internet, and configuration may still be required to meet specific business requirements.

## UNDERSTANDING CLOUD DEPLOYMENT MODELS

When deploying cloud services for an organization, three primary deployment models must be considered:

1. **Public Cloud**: Businesses consume IT services from third-party vendors like AWS over the internet. It offers a vast array of services with pay-as-you-go pricing, enabling cost management and flexibility. Public cloud provides self-service capabilities and access to management consoles, APIs, and command-line interfaces.

2. **Private Cloud**: The organization procures, installs, configures, and manages all necessary infrastructure and software components in-house. Additional management software allows self-service provisioning. A private cloud is highly customizable, offering maximum control over security and infrastructure configuration.

3. **Hybrid Cloud**: Combines on-premises IT services managed solely by the organization with services from one or more third-party cloud providers. It is used for reducing CAPEX investment, disaster recovery projects, and testing new technologies. Connectivity options like VPN tunnels or dedicated fiber-based connections facilitate integration between on-premises and cloud environments. Hybrid cloud deployments enable phased migration approaches, minimal business interruption during migration, and implementation of high availability (HA) solutions. They also allow redirecting consumers to replica services hosted by the public cloud provider during downtime.

# CHAPTER 2 - INTRODUCTION TO AWS AND THE GLOBAL INFRASTRUCTURE

## WHAT IS AWS?

Amazon Web Services (AWS) is the world's largest public cloud-computing provider, offering over 175 distinct services accessible over the internet on a pay-as-you-go model. It serves a wide range of clients, including start-ups, enterprises, and governmental organizations like the United States Navy. AWS has consistently been recognized as a leader in the cloud computing market by Gartner Research's Magic Quadrant for Cloud Infrastructure and Platform Services.

AWS's history began in 2002 with a few ad hoc services, and it has since grown exponentially. The company's global infrastructure, comprising data centers across the globe, is critical to delivering its vast array of cloud services. You can access analytical research reports, including Gartner's Magic Quadrant, on AWS's website to learn more about its offerings and leadership in the cloud industry.

## EXPLORING THE AWS GLOBAL INFRASTRUCTURE

The AWS Global Infrastructure consists of multiple data centers spread across different geographical regions worldwide. These data centers host servers, storage devices, and networking equipment. Currently, AWS has 77 Availability Zones (AZs) within 24 Regions, with plans for 18 more AZs and 6 additional AWS Regions in the future.

Regions are physical locations where AWS hosts clusters of data centers, each containing two or more AZs. AZs are logically and physically separated groups of data centers within a Region. The purpose of having multiple AZs is to provide high availability, fault tolerance, and scalability for customers' applications.

In addition to Regions and AZs, AWS also operates edge locations, which are used for content delivery and caching. Edge locations are strategically placed and connected to AWS Regions through high-speed links, allowing faster access to frequently accessed content.

Some AWS services are global, meaning they are accessible from any Region without the need to specify a particular location. These services include IAM, Amazon CloudFront, Amazon Route 53, and Amazon S3.

AWS also offers on-premises services like the AWS Snow Family, Amazon Storage Gateway, and Amazon Outposts. These services are designed to facilitate hybrid cloud deployments, aid in data migration, and cater to clients with strict data residency requirements.

Understanding the AWS Global Infrastructure, Regions, and AZs allows customers to design highly available and fault-tolerant architectures while providing low-latency access to content and digital assets. Selecting the right AWS support plan is also essential for efficient use of AWS resources and ensuring the appropriate level of support for your specific use case.

## CHOOSING THE RIGHT AWS SUPPORT PLAN FOR YOUR BUSINESS

AWS provides different support plans tailored to meet the varying needs of businesses. The support plans range from Basic to Enterprise and offer different levels of technical assistance and response times.

1. **Basic Support Plan**: This plan is free for all AWS accounts and covers basic customer support, account-related issues, and access to publicly available documentation and support forums. It also includes limited access to the Trusted Advisor tool for best practices and the Personal Health Dashboard for service interruptions alerts.

2. **Developer Support Plan**: Recommended for non-production workloads and testing, this plan offers technical support via email during business hours. Response times for general guidance are within 24 hours and 12 hours for system-impaired issues. It includes access to the Trusted Advisor tool's basic checks.

3. **Business Support Plan**: Suitable for production environments, this plan provides 24/7 support via email, chat, and phone. Response times vary based on the severity of the issue. It includes help with troubleshooting and interoperability issues. Businesses can opt for AWS Infrastructure Event Management (IEM) for additional guidance during project launches or migrations.

4. **Enterprise Support Plan**: Designed for large organizations with extensive workloads, this premium plan includes a designated Technical Account Manager (TAM) who actively assists in planning, design, and implementation of cloud projects. It offers access to senior cloud engineers and Well-Architected reviews for optimizing solutions. The response time for business-critical issues is 15 minutes.

Each plan has distinct features and benefits, and businesses should choose based on their specific requirements and budget. More details about the support plans can be found on the AWS website.

## OVERVIEW OF THE AWS SERVICE HEALTH DASHBOARD

AWS provides a Service Health Dashboard that offers real-time service status information across all data centers in various Regions. This is the first place to check if a service appears to be non-responsive. AWS also offers Service Level Agreements (SLAs) for its service offerings, ensuring specific levels of reliability and availability.

The AWS Personal Health Dashboard (PHD) provides tailored information about issues that may affect your applications and resources. It offers personalized views of service health, proactive notifications, detailed troubleshooting guidance, integration with CloudWatch Events for automation, and the ability to aggregate health events across AWS Organizations for centralized management.

Before using any service on the AWS Platform, it is essential to review and agree to the AWS Acceptable Use Policy (AuP), which outlines the terms and conditions for service usage.

## THE AWS AUP

Absolutely, it is essential to comply with the AWS Acceptable Use Policy (AuP) when signing up for an AWS account for personal or business use. The policy outlines the acceptable and prohibited uses of AWS services. Failure to adhere to the guidelines in the policy may result in account suspension or termination, potentially affecting your deployed workloads. By signing up for AWS services, you automatically agree to the latest version of this policy. To review the full policy, you can visit https://aws.amazon.com/aup/.

AWS Certified Cloud Practitioner Exam Guide
Rajesh Daswani

# CHAPTER 3 - EXPLORING AWS ACCOUNTS, MULTI-ACCOUNT STRATEGY, AND AWS ORGANIZATIONS

## WHY HAVE A MULTI-ACCOUNT AWS ENVIRONMENT?

Certainly, a multi-account architecture is essential for effectively managing complex workloads in AWS. Hosting all resources in a single AWS account can become overwhelming and hinder proper management. By separating workloads into different accounts, you gain several benefits:

1. **Administrative Isolation**: Different business units can have varying levels of administrative control. For instance, developers might not need full access to the production account.

2. **Limited Visibility**: AWS accounts create a natural boundary, ensuring that resources in one account are not accessible to identities from other accounts without explicit permission.

3. **Security and Identity Management**: Centralize user identity accounts in one AWS identity management account, reducing duplicate accounts and simplifying management. Cross-account access ensures users can work in other accounts with the necessary permissions.

4. **Recovery and Audit Isolation**: Disaster recovery and business continuity workloads can be placed in separate accounts for efficient recovery and operational continuity.

In the upcoming section, we delve into AWS services that aid in designing and implementing a multi-account strategy. AWS Landing Zone, which assists in creating a customized baseline architecture for multi-account deployments, and AWS Control Tower, an automated solution aligning with industry best practices, are discussed in detail. These services provide the framework for efficiently managing and securing your AWS resources across various accounts.

## AWS LANDING ZONE X AWS CONTROL TOWER

**Summary:**
Designing a multi-account environment on AWS can be complex and time-consuming. AWS provides best practice methodologies for this purpose. The deprecated AWS Landing Zone has been replaced by AWS Control Tower. While Landing Zone remains in support, Control Tower is recommended. Control Tower automates landing zone setup with AWS Organizations, IAM, logging, and security policies.

**Key Elements:**
- **AWS Landing Zone:**
  - Baseline blueprint for multi-account architecture.
  - Identity management, governance, security, and logging.
  - Deprecated in favor of AWS Control Tower.
  - May appear in exams despite lack of new features.

- **AWS Control Tower:**
  - Automates landing zone setup using latest blueprints.
  - Includes AWS Organizations and multi-account setup.
  - Utilizes AWS Single Sign-On (SSO) for identity management.
  - Supports account federation with SSO.
  - Centralized logging with AWS CloudTrail and AWS Config.
  - Comes with recommended security policies (guardrails).
  - Enables customization to align with organizational policies.

- **Benefits:**
  - Simplifies complex multi-account architecture.
  - Saves time compared to manual setup.
  - Provides security and compliance out-of-the-box.

- **Next Steps:**
  - Understanding AWS Organizations for central account management.
  - Importance of tools in building secure cloud architecture.

## AWS ORGANIZATIONS

**Summary:**
Managing multiple AWS accounts efficiently is crucial for workload separation and compliance. AWS Organizations offers centralized management, allowing creation of a management account and multiple member accounts. Organization Units (OUs) group accounts logically, and Service Control Policies (SCPs) enforce service restrictions. Consolidated billing aids cost management, and different OU structures meet diverse business needs.

**Key Elements:**
- **AWS Organizations:**
  - Centrally manages multiple AWS accounts.
  - Offers a free service with chargeable resources.
  - Creates a management account and member accounts.
  - OUs organize accounts hierarchically.
  - SCPs apply guardrails to services per OU.
  - Provides consolidated billing for cost management.
  - Enables various OU structures based on needs.
  - Facilitates security boundaries and compliance.

- **Core OUs:**
  - Infrastructure OU: Shared services (e.g., directory, networking).
  - Security OU: IAM, cross-account policies, logging.
  - Separates non-production and production accounts.

- **Additional OUs:**
  - Sandbox OUs: Isolated environment for experiments.
  - Workloads OUs: Hosts customer-facing apps (Dev, Test, Prod).
  - Suspended OUs: Accounts for auditing, with restricted access.

- **Benefits:**
  - Efficiently manage multiple AWS accounts.
  - Ensure workload separation and security.
  - Enforce compliance with SCPs.
  - Optimize costs through consolidated billing.

- **Considerations:**
  - Determine necessary AWS accounts based on business needs.
  - Balance functional and technical requirements.
  - Follow recommended OU structures for guidance.

- **Next Steps:**
  - Explore recommended OU structures:
    [Recommended OU Structure Guide](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/recommended-ous.html).
  - Learn about AWS Free Tier accounts and creation in the next section.

## AWS FREE TIER ACCOUNTS

**Summary:**
The AWS Free Tier account offers a standard account for various workloads, free for the first 12 months. It provides access to over 85 AWS services, with specific usage thresholds. Key offerings include Amazon S3 storage, EC2 instances, and RDS instances. Additional tools like AWS CloudFormation and Elastic Beanstalk are free to use, but resources deployed have charges. Certain services like CloudWatch, Lambda, and AWS Organizations are always free up to specified limits. There are also free trial services such as Amazon Workspaces, Detective, and Redshift. The Free Tier is valuable for learning and experimentation.

**Key Elements:**
- **AWS Free Tier Account:**
  - Standard account for diverse workloads.
  - Free for 12 months with usage thresholds.
  - Access to 85+ AWS technologies and services.
  - Examples of usage under Free Tier:
    - Amazon S3 storage up to 5 GB.
    - t2.micro EC2 instance for 750 hours/month.
    - Amazon RDS instance for 750 hours/month.

- **Free Tools:**
  - AWS CloudFormation: Templates for infrastructure deployment.
  - Amazon Elastic Beanstalk: Orchestration service for applications.
  - Tools are free, but resources have charges.

- **Always Free Services:**
  - Amazon CloudWatch: 10 custom metrics, 10 alarms, 1M API requests.
  - Amazon Lambda: 1M free requests, 3.2M compute seconds.
  - AWS Organizations: Centrally manage accounts with consolidated billing.

- **Free Trials:**
  - Amazon Workspaces: Virtual desktops trial with usage limits.
  - Amazon Detective: Security data analysis trial (30 days).
  - Redshift: Data warehousing trial (2 months, 750 hours/month).

- **Benefits:**
  - Experiment with AWS services.
  - Create sandbox environments.
  - Learn and prepare for exams.
  - Architect solutions with hands-on experience.

- **Considerations:**
  - Usage thresholds and limitations apply.
  - Useful for exploring complex configurations.
  
- **Next Steps:**
  - Leverage AWS Free Tier for learning, experimentation, and preparation.
  - Understand usage limits and explore more advanced AWS configurations.

# CHAPTER 4: IDENTITY AND ACCESS MANAGEMENT

## INTRODUCTION TO THE AWS IAM SERVICE

In this section of the book, we delve into the fundamentals of the AWS Identity and Access Management (IAM) service. It starts by emphasizing the importance of the root user, who is essentially the creator of the AWS account and possesses significant privileges. Protecting the credentials of the root user is stressed, and it's recommended not to use this account for day-to-day tasks.

The introduction highlights the concept of IAM users, which are additional user accounts that can be created to carry out routine operations. The IAM console is introduced as the primary interface to access AWS services, and readers are informed that it can be accessed through the web-based management console, the command-line interface (CLI), or AWS SDKs for coding purposes.

The structure of the AWS Management Console is discussed, revealing that services are categorized under headings like Compute, Network, and Storage. AWS IAM is situated within the Security, Identity, & Compliance category. The capability to search for services using the search bar is also mentioned.

Upon entering the IAM console, security alerts and best practices are presented. A unique sign-in URL is revealed for IAM users in the account, allowing customization for ease of use. This URL, which contains the AWS account ID, can be tailored to a more recognizable name. The process of customizing the sign-in URL is detailed.

The customized IAM sign-in URL can then be shared with other IAM users, enabling them to access the account if they possess an IAM user account. The significance of IAM users and their creation is elaborated upon. The text concludes by hinting at the next topic to be discussed: the root user account and the implementation of Multi-Factor Authentication (MFA) for enhanced security.

## THE ROOT USER ACCOUNT AND IMPLEMENTING MULTI-FACTOR AUTHENTICATION (MFA)

In this portion of the book, the focus is on the significance of the root user account in AWS and the implementation of Multi-Factor Authentication (MFA) to enhance security. Initially, the limitations of relying solely on a username and password for authentication are highlighted, considering the prevalent threats of malware attacks, hacking, and brute force attacks. To counteract these risks, MFA is introduced as a mechanism to ensure identity verification using two sets of credentials: something you know (username and password) and something you have (a one-time password pin generated on a personal device).

The recommendation to set up MFA for the root user account is emphasized. The process of setting up MFA is explained in detail, and readers are guided through the steps. It's suggested to use smartphone-based authenticators supported by AWS, such as Google Authenticator or Microsoft Authenticator.

The steps to set up MFA involve accessing the IAM management console and enabling MFA, followed by activating a virtual MFA device. The process includes scanning a QR code using the chosen authenticator app, then entering the generated MFA codes to complete the setup. This ensures that the root user account is now protected by MFA.

The benefits of MFA are reiterated, emphasizing that when logging in as the root user, the MFA code from the authenticator app will be required in addition to the email address and password. The temporary nature of the MFA code is noted, requiring prompt input. Once the MFA code is provided, successful login leads to access to the AWS Management Console.

The section also recaps the topics covered, including an introduction to the basic AWS Management Console and AWS IAM, as well as the practical implementation of MFA for the root user account. The upcoming focus is hinted at: password policies for enforcing robust and intricate passwords for IAM users created within the AWS account.

## THE IMPORTANCE OF DEFINING IAM PASSWORD POLICIES

The focus shifts towards the significance of establishing robust IAM (Identity and Access Management) password policies within an AWS (Amazon Web Services) environment. After securing the root user account using Multi-Factor Authentication (MFA), the next step involves creating IAM user accounts for members of an organization who require access to AWS services. The root user's elevated privileges necessitate the avoidance of its use for day-to-day operations.

The text anticipates the need for configuring passwords for IAM user accounts. The importance of enforcing password policies is highlighted, particularly when dealing with numerous IAM user accounts. AWS offers password policy capabilities that allow administrators to define rules that enhance password complexity. By doing so, users are compelled to select passwords that adhere to the stipulated complexity rules, thereby promoting the use of strong passwords across all IAM user accounts.

The process of configuring these password policies is described to be accessible from the Account Settings section of the IAM dashboard. This enables administrators to maintain control over the security of the IAM user accounts.

The following section is hinted at, focusing on the creation of additional IAM users and the establishment of IAM groups. IAM users are distinct identities that can be generated in addition to the root user account. These users represent actual individuals within the organization who require access to AWS services for their respective roles, such as developers or server administrators.

In summary, this portion of the text emphasizes the importance of enforcing IAM password policies to ensure strong security measures across the organization's IAM user accounts, while also introducing the concept of IAM users and their relevance within the AWS environment.

## KEY DIFFERENCES BETWEEN IAM USERS AND IAM GROUPS

In this section of the book, the focus is on the key distinctions between IAM (Identity and Access Management) users and IAM groups within the AWS (Amazon Web Services) ecosystem.

**IAM Users**:
As explained earlier, IAM users are additional accounts that can be created alongside the root user. These users can represent real individuals in an organization, such as members of a development team or server administrators. IAM users are provided with their own credentials and can use them to log into the AWS account, carrying out tasks based on the permissions assigned to them.

IAM user accounts can also be employed by applications and services that need to authenticate themselves with AWS services. For example, an application needing to modify an Amazon RDS database can be granted an IAM user account with appropriate permissions. However, this approach isn't ideal for most situations due to security concerns associated with storing credentials in plain text and the need for regular credential rotation. AWS introduces IAM roles as a better alternative for these cases, which are covered later in the chapter.

Access to AWS services can be achieved through the web-based management console, CLI (Command Line Interface), or AWS SDKs. IAM users can use username and password combinations for console access, while programmatic access through the CLI requires access keys, comprising an access key ID and a secret access key.

**IAM Groups**:
The concept of IAM groups is introduced as a means to efficiently manage permissions for users who share common roles in the organization. When configuring permissions for an IAM user, policies can be attached directly. However, a more streamlined approach involves grouping users based on their roles and then applying policies to the group itself, allowing those policies to cascade down to the individual users within the group.

For instance, if a team of developers requires the ability to manage Amazon S3 storage buckets, instead of manually assigning the same permission to each developer, a single permission can be granted to an IAM group named "Developers." All members of this group will inherit the specified permission, simplifying permission management.

In summary, this section emphasizes the value of setting up IAM users and groups, which allows for effective control over access and permissions within the AWS account. IAM groups are highlighted as a way to efficiently manage permissions for users who share similar job roles.

The upcoming section is previewed to delve into IAM policies in detail, elucidating how these policies empower administrators to define permissions for various identities, thereby governing their actions within the AWS account.

## DEFINING PERMISSIONS WITH IAM POLICIES

In this section, the book discusses the concept of IAM (Identity and Access Management) policies within the AWS (Amazon Web Services) ecosystem and how they are used to define permissions for various IAM identities, such as IAM users, groups, and roles. IAM policies play a crucial role in enforcing the principle of least privilege, ensuring that identities are granted only the access necessary for their roles.

**IAM Policies Overview**:
IAM policies are JSON documents attached to IAM identities, specifying the actions an identity can perform within the AWS account. The book presents an illustration of Bob, a member of the developers group, and how his access to the "Marketing Documents" S3 bucket is controlled by an attached IAM policy.

**Types of IAM Policies**:
The book introduces six types of IAM policies:

1. **Identity-based policies**: Attached to IAM identities like users, groups, and roles to define their permissions within the AWS account.
2. **Resource-based policies**: Attached to resources, granting permissions to principals (identities) within or outside the AWS account.
3. **Permission boundaries**: A policy that sets the maximum permissions for an IAM entity, controlling what an identity-based policy can grant.
4. **Organization Service Control Policies (SCPs)**: Define maximum permissions for organization members, restricting what IAM policies can allow.
5. **Access Control Lists (ACLs)**: Manage access to specific resources like Amazon S3 buckets and objects, granting permissions to AWS accounts.
6. **Session policies**: Passed during programmatic access, limiting permissions for a specific session.

**Types of Identity-based Policies**:
Identity-based policies can be categorized into three types:

1. **Managed AWS policies**: Pre-configured policies with specific permissions provided by AWS. These can be attached to multiple identities.
2. **Customer-managed policies**: Policies created by customers, offering more granularity in permission sets.
3. **Inline policies**: Policies created and directly attached to an IAM identity, maintaining a one-to-one relationship.


**Example of an IAM Policy**:
An example IAM policy is provided, demonstrating a managed AWS policy named "AmazonS3ReadOnlyAccess." The JSON structure of the policy includes components like version, statements, effects, actions, resources, and conditions. The example policy grants read access to all S3 buckets.

**IAM Policy Simulator**:
The book introduces the IAM policy simulator, a tool to test and troubleshoot policies without making actual API calls. This tool helps identify permissions granted or denied based on the policies attached to IAM identities.

**IAM Roles and Temporary Credentials**:
IAM roles are discussed as independent identities that can be assumed by other entities, offering secure access to AWS services and resources. IAM roles are used for scenarios like cross-account access, federated users, and AWS service access. Roles use temporary credentials assigned by the Security Token Service (STS), providing short-term access to resources without storing long-term credentials. A trust policy defines entities that can assume the role, and the book emphasizes using roles instead of IAM user accounts for enhanced security.

In conclusion, this section explores the significance of IAM policies in controlling access and permissions within AWS. It introduces the various types of policies and delves into identity-based policies in detail. The IAM policy simulator and the use of IAM roles with temporary credentials are also discussed. The next section is a preview of credential reports and their role in auditing IAM identities.

## REVIEWING CREDENTIAL REPORTS

In this section, the book discusses the importance of credential reports in AWS's IAM (Identity and Access Management) service. Credential reports provide valuable insights into the security state of IAM users, allowing administrators to review and audit key information about their identities and their access status.

**Credential Reports Overview**:
AWS offers the capability to download credential reports in CSV format. These reports are updated every 4 hours and provide administrators with a comprehensive view of the IAM users in their AWS account. The reports contain essential details such as user names, status of credentials (passwords and access keys), and whether users have Multi-Factor Authentication (MFA) configured.

**Use Cases for Credential Reports**:
Monitoring and analyzing credential reports can offer several benefits:

1. **Auditing IAM Users**: The reports allow you to review and audit the security status of your IAM users. You can assess whether their credentials are properly configured, including passwords and access keys.

2. **MFA Verification**: The reports highlight whether users have set up Multi-Factor Authentication (MFA), adding an extra layer of security to their accounts.

3. **User Activity**: By tracking user activity, you can identify IAM users who haven't accessed resources in your AWS account recently. This helps you evaluate whether those users still require access and whether any unused accounts can be removed, improving overall security.

4. **Access Control Review**: Credential reports assist in maintaining a clear overview of your IAM users' access patterns and their corresponding credentials, aiding in better access control management.

5. **Security Compliance**: Regularly reviewing credential reports supports your organization's security compliance efforts by ensuring that users adhere to best practices and security policies.

**Conclusion of Credential Reports Section**:
In this section, the book introduces the concept of credential reports as a valuable tool for IAM administrators. It emphasizes the significance of regularly monitoring these reports to maintain the security of IAM users, track their access status, and identify any unused or unnecessary accounts. The next sections will provide hands-on exercises to help readers gain practical experience in using AWS IAM to enhance security within their AWS accounts.







