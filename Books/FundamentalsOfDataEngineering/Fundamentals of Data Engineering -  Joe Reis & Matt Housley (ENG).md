<a href="https://www.goodreads.com/user/show/50697219-jo-o-paulo-m-ller-mamede">
    <img src="https://img.shields.io/badge/Goodreads-372213?style=for-the-badge&logo=goodreads&logoColor=white" alt="Goodreads Badge"/>
  </a>
  <img src="https://upload.wikimedia.org/wikipedia/commons/1/13/United-kingdom_flag_icon_round.svg" width=25 height=25/> 
  
## Table of Contents
- [Fundamentals of Data Engineering - Joe Reis & Matt Housley](#fundamentals-of-data-engineering---joe-reis--matt-housley)
  - [Chapter 1 Summary](#chapter-1-summary)
    - [Fundamentals](#fundamentals)
    - [The Task of Data Engineering](#the-task-of-data-engineering)
    - [The Evolution of Data Engineering](#the-evolution-of-data-engineering)
    - [Data Engineering vs Data Science](#data-engineering-vs-data-science)
    - [Data Engineer Skills and Activities](#data-engineer-skills-and-activities)
    - [Data Maturity Stages](#data-maturity-stages)
    - [The Background and Skills of a Data Engineer](#the-background-and-skills-of-a-data-engineer)
    - [Whom Data Engineers Work With](#whom-data-engineers-work-with)
  - [Chapter 2 Summary](#chapter-2-summary)
    - [Introduction](#introduction)
    - [Generation: Source Systems](#generation-source-systems)
    - [Evaluating Source Systems: Key Engineering Considerations](#evaluating-source-systems-key-engineering-considerations)
    - [Data Schema and Challenges](#data-schema-and-challenges)

# Fundamentals of Data Engineering - Joe Reis & Matt Housley

<img src="https://m.media-amazon.com/images/I/41BCu6h1rWL.jpg"/> 

## Chapter 1 Summary
### Fundamentals 
Data engineering is a critical field in data and technology, responsible for building the foundation for data science and analytics in production. 
Despite its popularity, there's often confusion about what data engineering entails. 
It emerged alongside the rise of data science in the 2010s and involves creating interfaces and mechanisms for the flow and access of information. 
Data engineers are dedicated specialists who set up and operate an organization's data infrastructure, ensuring data remains available and usable for further analysis by data analysts and scientists. 
Different experts have varying definitions of data engineering, but its main focus lies in the movement, manipulation, and management of data.

### The Task of Data Engineering 
Data engineering involves the development, implementation, and maintenance of systems and processes that handle raw data, transforming it into high-quality, 
consistent information to support various downstream use cases, such as analysis and machine learning. It intersects with security, data management, 
DataOps, data architecture, orchestration, and software engineering. The data engineering lifecycle includes five stages: Generation, Storage, Ingestion, 
Transformation, and Serving, with undercurrents of security, data management, DataOps, data architecture, orchestration, and software engineering. 
The data engineering lifecycle helps data engineers view their role holistically, focusing on the data itself and its end goals. 
The book delves deeper into the data engineering lifecycle and its core concepts in Chapter 2.

### The Evolution of Data Engineering
The evolution of data engineering has been marked by significant developments and transformations over the years. The field's origins can be traced back to data warehousing in the 1970s, 
with the term "data warehouse" coined in 1990. The rise of the internet in the mid-1990s gave birth to web-first companies, leading to the need for scalable backend systems to handle the 
enormous amounts of data generated. The early 2000s saw the emergence of contemporary data engineering, driven by the explosion of data and the availability of cheap commodity hardware. 
The term "big data" gained popularity during this time, and open-source big data tools in the Hadoop ecosystem rapidly matured. However, the complexity and administrative overhead of managing 
these systems led to simplification, and the focus shifted to delivering insights and value. As a result, the term "big data engineer" evolved into "data engineer." In the 2020s, 
data engineering has further evolved, with a greater emphasis on abstraction, simplification, and modularity. Data engineers now focus on data lifecycle management, including security, 
data governance, data quality, compliance, and privacy. The present is seen as a golden age of data lifecycle management, with data engineers equipped with better tools and techniques than ever before.

### Data Engineering vs Data Science
Data engineering and data science are two distinct but complementary fields in the realm of data and technology. 
While some may debate whether data engineering is a subdiscipline of data science, they are generally regarded as separate disciplines. 
Data engineering sits upstream from data science, meaning data engineers provide the foundational inputs used by data scientists in their work. 
The Data Science Hierarchy of Needs illustrates that data scientists spend a significant portion of their time on data-related tasks such as gathering, 
cleaning, and processing data, before they can focus on advanced analytics and machine learning (ML). Data engineers play a crucial role in building a 
solid data foundation, allowing data scientists to spend more time on analysis and ML tasks. In an ideal scenario, data scientists should dedicate the 
majority of their time to analytics, experimentation, and ML, while data engineers handle the data engineering aspects to support their work. 
Both data engineering and data science are essential and equally significant for delivering value from data in production environments. 
Data engineers bridge the gap between obtaining data and deriving value from it, making them integral to the success of data science in real-world applications.

### Data Engineer Skills and Activities

Data engineering requires a diverse skill set that encompasses various aspects, including security, data management, DataOps, data architecture, 
and software engineering. Data engineers must have the ability to evaluate data tools and understand how they fit together throughout the data engineering lifecycle. 
They need to be aware of how data is produced in source systems and how data analysts and data scientists will use and derive value from the processed and curated data. 
Additionally, data engineers must handle complex moving parts and continually optimize their solutions in terms of cost, agility, scalability, simplicity, reuse, and interoperability.

In the past, data engineers were expected to have in-depth knowledge of powerful and monolithic technologies like Hadoop, Spark, Teradata, and Hive. 
However, the modern data-tooling landscape has evolved to significantly abstract and simplify workflows, allowing data engineers to focus on balancing 
cost-effective and value-driven services. While data engineers should have a functional understanding of areas such as ML models, data analysis, 
and software applications, their primary responsibilities do not include directly building ML models, creating reports or dashboards, performing data analysis, 
building KPIs, or developing software applications.

The level of data engineering complexity in a company is influenced by its data maturity. Data maturity refers to the progression towards higher data utilization, 
capabilities, and integration across the organization, regardless of the company's age or revenue. Data maturity models can vary, and the book presents a simplified 
three-stage model: starting with data, scaling with data, and leading with data. Each stage represents different levels of data utilization and impacts a data engineer's job responsibilities and career progression.

### Data Maturity Stages

**Stage 1: Starting with data**

In Stage 1, a company is in the early stages of data maturity. Goals may be loosely defined, and data architecture and infrastructure are still in the early planning and development phases. Adoption and utilization of data are likely low or nonexistent, and the data team is small and often multi-functional, with data engineers playing various roles like data scientists or software engineers. The data engineer's primary goal is to move quickly, gain traction, and add value.

At this stage, the practicalities of extracting value from data may be poorly understood, and the focus should be on building a solid data foundation. While it might be tempting to jump into machine learning (ML) initiatives, it is crucial to avoid doing so prematurely. Without a solid data foundation, data engineers may lack the necessary data for reliable ML models and the means to deploy these models in a scalable and repeatable manner.

To navigate Stage 1 successfully, data engineers should focus on:

1. Getting buy-in from key stakeholders, including executive management, and having a sponsor for critical initiatives to design and build a data architecture that supports the company's goals.
2. Defining the right data architecture based on business goals and competitive advantage.
3. Identifying and auditing data that will support key initiatives within the designed data architecture.
4. Building a solid data foundation that enables future data analysts and data scientists to generate valuable reports and models. During this stage, data engineers may also be responsible for generating these reports and models.

To avoid pitfalls in Stage 1, data engineers should:

1. Strive for quick wins to establish the importance of data within the organization, but also plan to reduce technical debt to avoid future delivery friction.
2. Communicate and collaborate with stakeholders outside the data team to avoid working in silos and ensure that efforts align with business needs.
3. Use off-the-shelf, turnkey solutions wherever possible to avoid undifferentiated heavy lifting and unnecessary technical complexity.
4. Build custom solutions and code only where it creates a competitive advantage.

**Stage 2: Scaling with data**

In Stage 2, the company has moved beyond ad hoc data requests and has established formal data practices. Data engineering roles shift from generalists to specialists, with individuals focusing on specific aspects of the data engineering lifecycle. The data engineer's goals in Stage 2 are to:

1. Establish formal data practices.
2. Create scalable and robust data architectures.
3. Adopt DevOps and DataOps practices.
4. Build systems that support ML.
5. Continue avoiding undifferentiated heavy lifting and customizing only when it provides a competitive advantage.

Challenges in Stage 2 include the temptation to adopt bleeding-edge technologies based on social proof from other companies. Data engineering decisions should be driven by the value they deliver to the customers. The main bottleneck for scaling is often the data engineering team's capacity, so focusing on solutions that are simple to deploy and manage can help expand throughput.

At this stage, data engineers should focus on pragmatic leadership and communication with other teams, highlighting the practical utility of data and teaching the organization how to consume and leverage data effectively.

**Stage 3: Leading with data**

In Stage 3, the company is fully data-driven, with automated pipelines and systems enabling self-service analytics and ML. The introduction of new data sources is seamless, and tangible value is derived from the data. Data engineers at this stage build on the achievements of previous stages and take on additional responsibilities, such as creating automation for introducing new data and focusing on enterprise aspects of data management and DataOps.

Data engineers in Stage 3 should deploy tools that expose and disseminate data throughout the organization, enabling efficient collaboration among software engineers, ML engineers, analysts, and other stakeholders. To avoid complacency, organizations in Stage 3 must constantly focus on maintenance and improvement to sustain their data maturity level and not regress to a lower stage.

It is important to stay vigilant against technology distractions and pursue custom-built technology only when it provides a clear competitive advantage. At this stage, data engineers should create a community and environment that fosters collaboration and open communication, regardless of role or position within the organization.

### The Background and Skills of a Data Engineer

Becoming a data engineer can involve a significant amount of self-study, as formal training programs and standardized paths are limited due to the relative novelty of the field. Individuals from various educational and career backgrounds can enter data engineering, but transitioning from an adjacent field like software engineering, ETL development, database administration, data science, or data analysis can provide a good starting point due to their data awareness and relevant technical skills.

To be successful as a data engineer, a requisite body of knowledge exists, requiring a good understanding of data management best practices and various technologies. A data engineer should be proficient in software engineering, DataOps, data architecture, and be able to view responsibilities through both business and technical lenses.

**Business Responsibilities**

In addition to technical skills, a data engineer should possess essential business skills, including:

1. _Communication_: Ability to communicate effectively with both technical and non-technical individuals across the organization, building rapport and trust.
2. _Scoping and Gathering Requirements_: Understanding what to build and ensuring stakeholders agree with the assessment, as well as knowing how data and technology decisions impact the business.
3. _Cultural Foundations_: Understanding the cultural aspects of Agile, DevOps, and DataOps, as these practices require buy-in across the organization.
4. _Cost Control_: Focusing on optimizing time to value, total cost of ownership, and opportunity cost to keep costs low while providing value.
5. _Continuous Learning_: The data field is constantly evolving, and successful data engineers stay abreast of new developments while sharpening their fundamental knowledge.

**Technical Responsibilities**

Data engineers must possess technical skills in building architectures that optimize performance and cost. They should be familiar with various technologies and languages used in the data engineering lifecycle, which includes stages like generation, storage, ingestion, transformation, and serving. The undercurrents of data engineering encompass security, data management, DataOps, data architecture, and software engineering.

The primary programming languages for data engineering include SQL, Python, a JVM language (Java or Scala), and bash. SQL, despite having once been sidelined by big data technologies like MapReduce, has reemerged as a powerful tool for processing large amounts of data, and competent data engineers should be highly proficient in it. Data engineers should also know when SQL is not suitable for a particular task and be skilled in using other languages.

To keep pace with the fast-moving field of data engineering, it is essential to focus on fundamentals to understand what is unlikely to change while staying updated on ongoing developments to know where the field is heading. Strive to understand how new technologies can enhance the data engineering lifecycle and be helpful in achieving business objectives.

By possessing both business and technical skills, data engineers can excel in their role and contribute significantly to the success of their organizations in leveraging data as a competitive advantage.

### Whom Data Engineers Work With

Data engineers interact with various roles within an organization, both technical and nontechnical. Let's explore the key stakeholders with whom data engineers collaborate:

**Upstream Stakeholders**

_Data Architects_: Data architects design the blueprint for organizational data management, mapping out processes and overall data architecture and systems. They collaborate with data engineers to ensure the smooth flow of data.

_Software Engineers_: Software engineers build the software and systems that generate internal data, which data engineers consume and process. Collaboration with software engineers is essential for understanding data generation and data engineering requirements.

_DevOps Engineers and Site-Reliability Engineers (SREs)_: DevOps and SREs often produce data through operational monitoring. They may serve as upstream stakeholders to data engineers, providing data for further processing.

**Downstream Stakeholders**

_Data Scientists_: Data scientists build models to make predictions and recommendations. Data engineers work with them to provide the necessary data automation and scale, enabling smooth data science workflows.

_Data Analysts_: Data analysts seek to understand business performance and trends. Data engineers collaborate with them to build pipelines for new data sources and improve data quality.

_Machine Learning Engineers and AI Researchers_: ML engineers develop advanced ML techniques, and AI researchers work on new ML approaches. Data engineers may work closely with them in designing ML processes and ensuring successful model deployment.

**Business Leadership**

_C-Level Executives_: C-level executives, including CEOs, CIOs, CTOs, CDOs, and CAOs, are increasingly involved in data and analytics, as they recognize data as a significant asset for modern businesses. Data engineers interact with them to provide insights into data capabilities and possibilities.

_Project Managers_: Data engineers often work on significant initiatives that require project management. Project managers direct and coordinate these initiatives, and data engineers collaborate with them to plan sprints and communicate progress and blockers.

_Product Managers_: Product managers oversee product development, including data products. Data engineers interact with them to align data engineering efforts with the needs of the customer and business.

_Other Management Roles_: Data engineers may serve as part of centralized data engineering teams or work under specific managers, projects, or products. Their interactions with management depend on the organizational structure.

Data engineers play a crucial role as organizational connectors, bridging the gap between technical teams and business stakeholders. They actively participate in strategic planning, data product development, and key initiatives that extend beyond the boundaries of IT.

**Chapter 1 Summary Conclusion**

This chapter provided an overview of the data engineering landscape, defining the role of data engineers and describing their responsibilities. We also discussed the types of data maturity in a company.

Data engineers work with a wide range of stakeholders, including technical roles like data architects, software engineers, and data scientists, as well as business leadership such as C-level executives, project managers, and product managers.

Understanding the interactions between data engineers and various stakeholders is essential for building successful data engineering teams and driving data-driven initiatives within organizations.

## Chapter 2 Summary

### Introduction

Chapter 2 of the book introduces the concept of the Data Engineering Lifecycle as the central theme of the book. The main goal is to move beyond viewing data engineering as a specific collection of data technologies and to emphasize the principles of data lifecycle management. The data engineering lifecycle comprises five stages: Generation, Storage, Ingestion, Transformation, and Serving data. These stages involve turning raw data ingredients into a useful end product, ready for consumption by analysts, data scientists, ML engineers, and others.

The chapter explains that storage is a foundational element that underpins other stages, and although the stages are distinct, they may not always follow a neat, continuous flow. They can repeat, occur out of order, overlap, or intertwine in various ways. The undercurrents of the data engineering lifecycle, such as security, data management, DataOps, data architecture, orchestration, and software engineering, are essential bedrock elements that cut across multiple stages and are necessary for the proper functioning of each stage.

Furthermore, the chapter clarifies the difference between the Data Lifecycle and the Data Engineering Lifecycle. The Data Engineering Lifecycle is a subset of the overall Data Lifecycle. While the full data lifecycle encompasses data across its entire lifespan, the data engineering lifecycle specifically focuses on the stages controlled by a data engineer.

Overall, the Data Engineering Lifecycle is the framework that guides the transformation of raw data into valuable insights and products, ensuring that data engineers play a critical role in managing data from "cradle to grave" and enabling its utilization by various stakeholders.


### Generation Source Systems

A source system is the origin of the data used in the data engineering lifecycle. It can be an IoT device, an application message queue, or a transactional database. Data engineers consume data from source systems but don’t typically own or control them. Understanding how source systems work, generate data, and the frequency, velocity, and variety of data they produce is crucial for data engineers.

**Source System Examples**

1. _Traditional Source System_: Application database with several application servers supported by a database. This pattern gained popularity with the success of relational database management systems (RDBMSs) in the 1980s. It remains widely used, especially in modern software development practices where applications consist of many small service/database pairs with microservices.

2. _Modern Source System_: IoT swarm where a fleet of devices sends data messages to a central collection system. This type of IoT source system is increasingly common as IoT devices, sensors, and smart devices become more prevalent.

### Evaluating Source Systems Key Engineering Considerations

Data engineers must consider various factors when assessing source systems:

- **Data characteristics**: Is it an application or a swarm of IoT devices?
- **Data persistence**: Is data persisted long term, or is it temporary and quickly deleted?
- **Data generation rate**: How many events per second? How many gigabytes per hour?
- **Data consistency**: How often do data inconsistencies occur, such as nulls where not expected or formatting issues?
- **Error occurrence frequency and data duplicates**.
- **Late-arriving data**: Will some data values arrive much later than others produced simultaneously?
- **Data schema**: Will data engineers need to join across several tables or systems to get a complete picture?
- **Handling schema changes and communication with downstream stakeholders**.
- **Data retrieval frequency and performance impact**.
- **Upstream data dependencies and characteristics of these systems**.
- **Data-quality checks for late or missing data**.

### Data Schema and Challenges

The schema defines the hierarchical organization of data. Source systems handle data schema in different ways:

- **Schemaless**: Application defines the schema as data is written (e.g., MongoDB).
- **Fixed Schema**: Relational database storage with a fixed schema enforced in the database.

Schemas may change over time, presenting challenges for data engineers. Schema evolution is encouraged in Agile software development, and data engineers must transform raw data input in the source system schema into valuable output for analytics.

Sources produce data consumed by downstream systems, including human-generated spreadsheets, IoT sensors, web, and mobile applications. Data engineers need to understand the source data generation, quirks, and nuances, as well as the limits of the source systems they interact with.




