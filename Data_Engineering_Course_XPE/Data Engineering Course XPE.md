![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
<div align="right">
  <img src="https://github.com/Shamslux/DataEngineering/assets/79280485/db0c60d3-d801-4719-9103-9bee9cee6406" alt="Badge" width="150">
</div>

# About the Course

I took this course from May 2022 to August 2022. The course was conducted on the XPE platform (XP Educação), formerly
known as IGTI. It is a highly regarded platform in Brazil, offering undergraduate and postgraduate programs as well as
bootcamps in the leading technologies and methodologies in the market.

Focused on preparing students for the job market, XPE has partnerships and provides qualified workforce to some of the
major Brazilian corporations. The below image shows some of these major corporations to where they provided qualified workforce.

![companies](https://github.com/Shamslux/DataEngineering/assets/79280485/ce3e3131-7a05-4972-8d20-d6a8b04a0ffa)

# 1st Module 

Chapter 1. Fundamental Concepts of Big Data

- Data, Data Sources, and Data Types
- Concept and Characteristics of Big Data
- Semantic Web
- Open Data and Linked Data
- Ontologies
- Big Data and Data Engineering Data Pipeline
- Overview of Major Data Analysis Types

Chapter 2. Data Modeling

- Fundamentals of Database
- Conceptual Data Model
- Building the ERD (Entity-Relationship Model)
- Relational Model (Logical Data Model)
- Relational Database Management Systems
- Physical Data Model
- Installation of MySQL Workbench and MySQL Server
- Data Modeling using MySQL Workbench

Chapter 3. SQL Language

- Introduction to SQL Language
- Data Definition Language (DDL)
- Data Manipulation Language (DML)
- Data Control Language (DCL)
- DBeaver Tool
- Relational Database in the Cloud - Amazon RDB

Chapter 4. SQL Language: Data Query Language (DQL)

- Selecting Data (SELECT FROM, DISTINCT, ORDER BY, Arithmetic Operators, Concatenation)
- Filtering Data (WHERE, LIKE, BETWEEN, IS NULL, IS NOT NULL)
- Aggregate Functions and Data Grouping (COUNT, MIN, MAX, AVG, SUM, GROUP BY, HAVING)
- Practice: SQL Querying using a Single Table
- Queries with Multiple Tables (JOIN, INNER JOIN, CROSS JOIN, and OUTER JOIN)
- MySQL Practice: Queries with Multiple Tables
- Nested Queries (IN, EXISTS)
- Practice: SQL Querying using DQL
  - Note: Practical lessons alternate between using MySQL Workbench and DBeaver.

Chapter 5. Data Warehouse and Dimensional Modeling

- Introduction to Data Warehousing
- Online Analytical Processing
- Dimensional Data Modeling
- Practice: Dimensional Data Modeling

## 1st Module Remarks

- This 1st module of the course was taught by Dr. Fernanda Farinelli, associate professor at the University of Brasília
(UnB).

- I did not summarize the topics on ontology, open data, and linked data because they are very theoretical topics, and I
preferred to leave them out of the summary to provide a more professional approach rather than a theoretical-educational
one.

- I also did not summarize the topics of data modeling and SQL because I already have educational and professional
experience with this part. In summary, the professor worked again on the conceptual model in the relational database,
normalization rules, the Entity-Relationship Model (ERM), and the main SQL commands.

- The course concludes its first module with a practical assignment involving questions similar to a university exam. I
will not share the questions because I cannot provide an accurate translation of the entire content (some images would
remain in Portuguese), and also because I do not know if the questions are reused in their course, which could generate
issues as they are in a public repository.

## What is Data?

### Data

Data is a representation of facts about the real world.

### Information 

Information is data endowed with relevance and purpose.

For example, "green" is an example of data. A tree is green, and that is information.

### Knowledge

Knowledge is information contextualized by experience.

For example, the fact that a green tree is a characteristic of seasons like summer or spring (in some countries) is an
example of knowledge, information contextualized by experience.

In this way, data is an isolated fact, information is purposeful data, and knowledge is our experience applied to
obtained information.

## Types of Data

Data can be structured, semi-structured, or unstructured.

### Structured data

Structured data has a homogeneous and predefined structure, being a prescriptive structure (it prescribes how the
data will be organized) and very clear (e.g., a relational database with predefined structured tables, where we know
that one field is of integer type, another is a date, etc.).

### Semi-structured data 

Semi-structured data has a more heterogeneous schema and a structure that can be predefined but is less rigid. The
structure comes with the data. Some examples are XML or JSON files, where we can see that the data is accompanied by
structures (tags).

### Unstructured data

Unstructured data does not have predefined schemas, does not have a defined structure, and the structure and data
are mixed. Video and audio files, for example, are examples of unstructured data.

Currently, a significant portion of data is being collected as unstructured data. In this understanding, a tweet can be
unstructured data because such text is subject to subjectivity, and we do not know how the author (user) will present
their opinion (in what structure).

## Datafication

It is the phenomenon in which there is massive data collection through various devices and applications. For example,
our product opinions are collected (on social networks or specific platforms), our feelings (on social networks), our
choices and preferences (on social networks, shopping websites, web browsing), our professional profile (LinkedIn), etc.

As a result, we have a multitude of data sources such as:

- Open data (public)
- Official documents
- Articles and newspapers
- Websites
- Audio and video
- Spreadsheets
- Social networks
- Information systems
- Integration files
- Internet of Things (IoT)
- Web data and LOD (Linked Open Data)
- Databases

## Big Data

Big Data refers to a massive amount of data. The datafication process has generated massive volumes of data. Thus, Big
Data refers to the challenge of processing increasingly larger volumes of data produced in various formats (videos,
images, texts, etc.), at speeds in the range of seconds, and providing real-time responses.

## The 3 Vs of Big Data:

- Diverse formats and structures (variety)
- Speed in creation and processing (velocity)
- Massive quantities (volume)

## The 8 Vs of Big Data:

Over time, the characteristics of the concept have expanded, and the Vs have increased. To avoid excessive terminology
(some articles mention 42 Vs), let's focus on a maximum of 8 characteristics of these Vs:

- Variety
- Velocity
- Value
- Virulence
- Visualization
- Viscosity
- Veracity
- Volume

**Veracity**: Processed data must be real and true.

**Value**: Is there a need to collect this data for my company? Will it truly generate value?

**Visualization**: I need to create data visualization mechanisms that are fast and provide insights.

**Virulence**: The ability to spread (through the network).

**Viscosity**: The ability to persist data (e.g., how long it remains active).

## Big Data vs Small Data:

In **Big Data**:

- Randomly generated data: Data emerges unpredictably, for example, a new follower bringing new interactions.

- Unknown data sources: Data from unplanned sources, for example, data from Facebook, X, etc.

- Unfriendly data: Generally semi-structured or unstructured data.

- Questionable validity or veracity: Data tends to be valid or true, but validation is necessary.

In **Small Data**:

- Data generated within my information system.

- Known data sources, i.e., the company's own systems.

- Friendly data, as they often come from known structures and have a greater tendency to be structured data (e.g., the
company's relational database).

- Controlled validity or veracity, as they usually come from validated company systems.

## What Big Data is not:

- **A hardware product**: but it involves hardware (architectures and platforms) with the capacity to process massive data
(scalability, parallelism, distribution, etc.).

- **A software product**: but it involves various applications for data collection, storage, integration, analysis, and
visualization.

- **A methodology**: but it requires practices compatible with the questions and answers desired and is present in the
development processes of systems and solutions.

## Knowledge Discovery in Databases (KDD)

![kdd](https://github.com/Shamslux/DataEngineering/assets/79280485/eecd1e3f-d32c-4f7b-beeb-670ba1d9780b)


### Overview

Knowledge Discovery in Databases (KDD) is a complex, multidisciplinary field that aims to extract valuable insights from
large and diverse datasets. KDD encompasses a range of techniques from data processing, data mining, and analysis,
integrating methods from statistics, machine learning, database technology, and pattern recognition.

### Process

The KDD process involves several key steps:

**Data Preparation and Selection**: This involves gathering the data, selecting the relevant subsets for analysis, and
transforming it into a suitable format.

**Data Cleaning and Preprocessing**: This step is crucial for improving the quality of the data by removing noise,
handling missing values, and ensuring consistency.

**Incorporation of Prior Knowledge**: Leveraging domain knowledge to guide the discovery process.

**Data Mining**: Applying algorithms to identify patterns, relationships, or anomalies. Common techniques include
clustering, classification, regression, and association rule mining.

**Interpretation and Evaluation**: Analyzing the mined patterns to extract actionable knowledge and validating them
against specific criteria to determine their usefulness.

### Applications

KDD is applied in various domains such as:
- Market analysis and management
- Fraud detection and risk management
- Bioinformatics and healthcare
- Customer relationship management
- Social network analysis

### Tools and Technologies

Several tools and technologies facilitate the KDD process, including:
- Data processing tools like Apache Hadoop and Spark
- Data mining tools such as Weka, Orange, and RapidMiner
- Programming languages like Python and R with libraries for data analysis and machine learning

### Conclusion

KDD is a vital field that helps in making informed decisions by discovering hidden patterns and insights in large
datasets. It requires a combination of expertise in data handling, statistical analysis, and domain knowledge.

## SEMMA Methodology

![semma](https://github.com/Shamslux/DataEngineering/assets/79280485/5b802b48-1f4c-4f61-b946-7bb79e9353ab)
*Image obtained from the Internet*

### Overview

SEMMA, which stands for Sample, Explore, Modify, Model, and Assess, is a structured approach to data analysis,
particularly useful in the context of big data. Originating from SAS Institute Inc., it provides a comprehensive guide
for transforming large datasets into actionable insights.

### SEMMA Process

The SEMMA methodology involves five key steps:

**Sample**: In the context of big data, this step involves selecting a representative subset of data. This is crucial to
efficiently manage and analyze extensive datasets, ensuring the performance and scalability of the analysis.

**Explore**: This phase is about examining the data to uncover initial patterns, anomalies, or relationships.
Visualization tools and descriptive statistics play a vital role in this stage, providing insights into the nature and
quality of the data.

**Modify**: Here, data is prepared and cleaned. This step includes handling missing data, outlier treatment, variable
transformation, and feature engineering. The goal is to refine the dataset into a format suitable for modeling.

**Model**: In this stage, various statistical and machine learning models are applied to the prepared data. The choice
of models depends on the nature of the problem – whether it’s prediction, classification, clustering, etc.

**Assess**: The final step involves evaluating the model's performance using appropriate metrics. This could include
accuracy, precision, recall, or specific business KPIs. The assessment guides the refinement of the model and validates
its effectiveness in answering the research question or solving the problem at hand.

### Applications in Big Data

- Predictive analytics in customer behavior analysis
- Risk assessment in financial services
- Health data analysis for disease prediction
- Market segmentation in retail

### Tools and Technologies

SEMMA can be implemented using various tools:
- Data processing: SQL, Apache Spark
- Exploration and visualization: Python (Matplotlib, Seaborn), R
- Modeling: SAS, Python (scikit-learn), R
- Assessment: Model evaluation libraries in Python and R

### Conclusion

The SEMMA methodology is a systematic approach that guides data analysts and scientists through the process of
extracting meaningful insights from big data. Its structured nature ensures thoroughness and efficiency, making it an
essential practice in the field of data analytics.

## CRISP-DM Methodology

### Overview

CRISP-DM, which stands for Cross-Industry Standard Process for Data Mining, is a robust and well-established methodology
for guiding data mining projects. It is especially pertinent in the context of big data, offering a structured approach
to uncovering insights and building predictive models from large and complex datasets.

### CRISP-DM Process

![crispdm](https://github.com/Shamslux/DataEngineering/assets/79280485/879ca40f-1b74-4eda-8aa5-a80fd8ee5e20)
*Image obtained from the Internet*

The CRISP-DM methodology comprises six major phases:

**Business Understanding**: This initial phase focuses on understanding the project objectives and requirements from a
business perspective. It involves defining the problem, determining project objectives, and establishing a preliminary
plan to achieve these objectives.

**Data Understanding**: This step involves collecting initial data, understanding its properties, and assessing its
quality. Data understanding is crucial for big data projects to identify data sources and gauge the challenges in data
processing and analysis.

**Data Preparation**: In this phase, data is cleaned and transformed into a suitable format for analysis. For big data,
this step is particularly significant due to the volume and variety of data, which may require sophisticated processing
tools and techniques.

**Modeling**: This stage involves selecting and applying various modeling techniques to the prepared data. The choice of
models is guided by the project objectives and the nature of the data. It may include machine learning algorithms
suitable for handling big data.

**Evaluation**: Here, the model or models are thoroughly evaluated, and their performance is assessed against the
business objectives. The evaluation phase ensures that the model meets the desired criteria and provides valuable
insights.

**Deployment**: The final phase involves deploying the model into a real-world environment. For big data projects,
deployment can be complex and requires careful planning to integrate the model into existing systems and processes.

### Applications in Big Data

- Predictive maintenance in manufacturing
- Fraud detection in financial services
- Personalized marketing and customer segmentation
- Healthcare analytics for patient care optimization

### Tools and Technologies

CRISP-DM can be implemented using a range of tools:
- Data processing and preparation: Apache Hadoop, Spark, Python, R
- Modeling: Python (TensorFlow, scikit-learn), R, SAS
- Evaluation and deployment: Model monitoring and evaluation tools, integration with business intelligence platforms

### Conclusion

CRISP-DM provides a comprehensive framework for tackling big data analytics projects. Its structured approach, from
understanding the business problem to deploying a solution, makes it an invaluable methodology for data scientists and
analysts working in diverse sectors.

## Data Engineering Pipeline

### Data Engineering Team

The role of the data engineering team is to build the entire data pipeline, which involves data collection/extraction,
processing/preparation, and data storage. Thus, the data engineering team is responsible for this data integration that
takes raw data and prepares it for future data analysis.

### Data Extraction

Data can be extracted through various processes and routines. There are multiple possible data sources and types of data
that may require techniques such as SQL, API consumption, Crawling/Scraping, custom scripts (R, Python, Scala, Java).

<img src="https://github.com/Shamslux/DataEngineering/assets/79280485/8e27cbe8-0f5d-4630-b81c-549bef947828" alt="data_extraction" width="400">

*Image obtained from the course*

## Data Modeling

It is to create a model that explains the operational and behavioral characteristics of data in a specific system or
application. This model aims to facilitate understanding of the data and data design by representing its main
characteristics.

## Data Storage

There are several ways to think about data storage:

- Distributed file systems (e.g., HDFS)

- DBMS (SQL relational databases, NoSQL, or NewSQL)

- Polyglot persistence (having a Data Warehouse, a Data Lake, and so on, for each type of data a more appropriate
storage solution).

- Utilizing cloud resources (e.g., S3, Blob) and other cloud resources for greater scalability and distribution ease.

## Data Analysis

Allows the extraction of valuable information from data.

- Studies the principles, methods, and computational systems for extracting knowledge from data.

- Identifies the possibilities of converting raw data into knowledge.

- Aims to efficiently find patterns (knowledge) in (large) datasets (streams).

- Seeks to understand people's behavior.

- Seeks to identify new business opportunities.

Thus, analyzing data is about finding a pattern/knowledge within that data. Hence, there is this metaphor of data
mining, as an allusion to the real task of mining, seeking to find precious goods after excavations and analysis.

### Types of Data Analysis

- **Descriptive Analysis**: describes facts and events, seeking to understand what happened.

- **Diagnostic Analysis**: seeks to understand why that event occurred, how it happened, who was involved, etc.

- **Predictive Analysis**: seeks to understand what may happen based on what has already happened in the past.

- **Prescriptive Analysis**: tries to simulate situations, i.e., if a certain event occurs, what will be the impact on
the business?

### Conclusion

This overview of analysis is important because, as engineers, we will work on preparing data for the analysis team;
therefore, it is interesting to understand some of this perspective from the other side to better serve in our daily
work.

## Data Warehousing

A Data Warehouse (DW) is a subject-oriented, integrated database (you can standardize data regardless of its source),
containing historical data (a snapshot of data over a period of time) and is non-volatile (usually not updated, but
rather new entries are inserted to show the data's history).

It is a database that facilitates the execution of decision support queries (W. H. Inmon), providing a holistic view of
the business from its operations, displaying information at appropriate levels and various levels of detail.

The main goal of the DW is to optimize the processing of complex analytical queries.

### Data Mart

It is a sectoral view to address a specific subject (area) or different levels of summarization, meeting the information
needs of a particular user community (INMON, 1992).

![dw_data_marts](https://github.com/Shamslux/DataEngineering/assets/79280485/f2a284be-dbbf-4293-9b86-081ab347890d)

Data Marts are departmental subsets focused on selected subjects.

### Data Warehousing Process

It is the process of extracting data from transactional systems and transforming it into organized information in a
user-friendly format. In summary, data is extracted from OLTP environments, undergoes transformation (e.g., ETL), and is
sent, organized, to the DW. This way, we have transformed, cleaned, organized, and standardized data in the DW, within
an OLAP environment, i.e., an environment conducive to analytical analysis.

### ETL

ETL (Extraction, Transformation, and Loading) is a technique in which data is obtained from sources (e.g., databases in
OLTP environments), transformed, and loaded into the DW.

- **Extraction**: the process of collecting or acquiring data from available data sources. Note: It is not limited to
relational databases; it can be files (e.g., CSV) or APIs, etc.

- **Transformation**: the process of standardization, cleaning, enrichment, and combination of data.

- **Loading**: the process of loading or inserting data into the respective data repositories.

In general, the ETL process involves taking data from various sources, taking these data to an intermediate area (e.g.,
Staging Area, ODS) for transformation, and finally loading the properly transformed data into the DW.

### OLTP vs. OLAP

**OLTP**

- Its purpose is to control and perform fundamental business tasks.

- Operational, current data, reflects the present.

- They are the original source of data.

**OLAP**

- Its purpose is to assist in planning, problem-solving, and decision support.

- Consolidation data, historical data.

- It has data originating from various OLTP databases.

## OLAP Cube

The reason for using a cube is to convey the idea of multiple dimensions.

![cube](https://github.com/Shamslux/DataEngineering/assets/79280485/42811c2c-09c9-4e8e-bfce-d67819014c95)

*Image obtained from the Internet*

As seen in the image, we can understand that it's possible to cross-reference product information with time periods and
geographic locations where they were sold, for example.

In this way, we have a fact (the quantity of product sales, even though the quantified numbers are not visible in this
example image), being viewed from various perspectives (types of products, time periods, and sales locations).

## OLAP Architectures

- **ROLAP** (Relational On Line Analytical Processing): uses a relational database to store its data and process
queries.

- **MOLAP** (Multidimensional On Line Analytical Processing): uses dimensional database technology to store its data and
process queries.

- **HOLAP** (Hybrid On Line Analytical Processing): hybrid tools (ROLAP and MOLAP), combining the scalability of ROLAP
with the high performance of MOLAP.

- **DOLAP** (Desktop On Line Analytical Processing): queries originate on the desktop to the server, which returns a
macro-cube to be analyzed.

- **WOLAP** (Web On Line Analytical Processing): queries originate via a web browser to the server, which returns the
processed cube to be analyzed.

