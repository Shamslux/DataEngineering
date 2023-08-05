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

