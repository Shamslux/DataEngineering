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

