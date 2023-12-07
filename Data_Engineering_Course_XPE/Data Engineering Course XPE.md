![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Airflow](https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white)
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

## Dimensional Modeling

Dimensional modeling is one of the most commonly used and crucial techniques and knowledge for designing a Data
Warehouse. Its objective is to present data in a standardized and intuitive model that allows users to understand it
while ensuring high-performance access (Ralph Kimball).

In general, the physical model is implemented in relational database management systems (RDBMS), and the modeling
approach is such that information is related in a way that is metaphorically represented as a cube.

![cube_dim](https://github.com/Shamslux/DataEngineering/assets/79280485/c7718ea1-6b8b-4898-90ad-f7a053297aa2)

*Image from the Internet (Microsoft Learn)*

### Dimensional View

The dimensional view allows us to visualize the measure (the fact) through a categorized perspective. For example, in
the image above that we used as a model, we can see the values (measures, such as information on sent packages) and the
dimensions that enable different perspectives on these values (we see 3 dimensions: route, source, and time).

### Elements of Dimensional Modeling

- **Facts**: Subjects or facts
- **Dimensions**: Variables or analytical dimensions
- **Measures**: Analytical values related to the subject according to the dimensions

### Fact

The fact is any business subject that you want to analyze. It reflects the evolution of the business in an
organization's day-to-day operations. It is an event worthy of analysis and control within the organization.

Examples:

- For a retail company, sales are an interesting subject (a fact) for analysis.

- For a police department, crimes are a subject (a fact) of interest for analysis.

### Dimensions

These are the variables that influence a fact, representing different "points of view" for analyzing an event.

Examples:

- It could be WHO performed the event, WHERE the event occurred, WHEN the event occurred, and so on.

- In the example of a retail company, it can analyze WHO was the top-selling salesperson, WHERE most sales occurred
(in which store, for example), and WHEN it had the highest number of sales (e.g., in which quarter).

- In the example of a police department, WHO could be a previously registered criminal who is committing thefts again,
WHERE could be a region with a higher number of crimes, and WHEN could be which months showed higher crime rates.

### Time

Since a Data Warehouse deals with historical data, time is ALWAYS an extremely important dimension! There is no analysis
without a time dimension!

### Measures

Measures are associated with a specific fact or subject.

Examples:

- For analyzing a retail company's sales, measures can include: total sales value, profit, total quantity of products
sold, or total quantity by product type, etc.

- For a police department, measures can include: total number of registered crimes, total number of crimes by serviced
regions, etc.

### Granularity in a Data Warehouse

We refer to granularity as the level of detail or summary contained in the data units within the fact under analysis.

For example, going back to the retail company example, if we have a model for greater detail (lower granularity), we
could have something like daily/hourly sales and monthly revenue; if we have a model for less detail (higher
granularity), we could have something like monthly sales and annual revenue.

In summary, the greater the granularity, the lower the level of detail, whereas the lower the granularity, the higher
the level of detail.

The choice of modeling (whether it will have higher or lower granularity) will depend on the business rules and the
desire to analyze the business.

### Components of the Dimensional Model

The components of the dimensional model are: the fact, the dimensions, and the measures (typically, the dimensions and
the fact).

Using the image below, let's take the example of a retail company:

![wh-questions-dim-fact](https://github.com/Shamslux/DataEngineering/assets/79280485/ea8e90c6-fb9b-4a85-980b-595d1414b6bc)

Above, we can see how each question asked about the subject (the fact) translates into dimensions that provide these
answers.

### Star Schema

It is a representation model named for the fact that the connections between the fact and dimensions resemble the shape
of a star. Despite representing a five-pointed star, the number of dimensions is not restricted to this number; the
model is used for didactic purposes. We can have fewer or more dimensions depending on the case.

![star-schema](https://github.com/Shamslux/DataEngineering/assets/79280485/2dab2ba8-87b7-407c-9caa-411c32aca9b6)

In the image, we can see a 1-to-N relationship, meaning that for each item in the dimension, we have N values in the
fact (e.g., a product X may have multiple sales occurrences).

![mer-star-schema](https://github.com/Shamslux/DataEngineering/assets/79280485/fdc153b3-0d16-4555-9715-b47b2af7db18)

In the conceptual model, we can observe the star schema applied above.

**Personal Note¹**: It's interesting to note that the fact contains all the SKs (Surrogate Keys) of the dimensions, and a
composite key is created to ensure integrity.

**Personal Note²**: Up to this point, the instructor hadn't mentioned the use of SKs (I will adjust this if I see them
discussing it in the application). As this might be a general training course in a boot camp (at this point, if it turns
out they won't explain it, I recommend following the instructions of instructor Felipe Mafra, from whom I initially
learned Business Intelligence), they might create IDs directly, but in real life, IDs will come from OLTP (Online
Transaction Processing) and will be transformed into our NKs (Natural Keys), and the SK (Surrogate Key) will be required
to maintain the integrity of the NKs. For example, an NK may undergo an update in some other column, and a new SK must
be generated to keep the history of the same NK at another historical moment.

Therefore, in real life, we always use SKs and always check if the composite key in the fact is intact, without any
duplication errors occurring (the database itself will alert us if there is any error).

### Snowflake Schema

The snowflake schema is represented by a snowflake shape because it starts to have multiple sub-dimensions linked to
each other. In the image below, we can see the "region" dimension with two sub-dimensions: "states" and "cities."

![snowflake-schema](https://github.com/Shamslux/DataEngineering/assets/79280485/0b7c2e6d-7ea4-416c-be4a-6dc5b506327a)

This model is a way to increase granularity (in the case of the star schema, we would have "states" and "cities" as
columns in the "region" dimension).

**Personal Note³**: It's worth noting that the star schema is faster due to having fewer joins, while the snowflake schema
is slower due to having more joins. However, the choice of each model should be made through a proper analysis of the
business. In general, whenever possible, it's a good practice to adopt the star schema for performance reasons.

### Steps of Dimensional Modeling

- **Step 1**: Understand the analysis requirements.

- **Step 2**: Identify the facts/subjects that need to be analyzed.

- **Step 3**: Identify which metrics support the analysis of the fact.

- **Step 4**: Define the level of detail for the analysis (granularity).

- **Step 5**: Identify the variables or dimensions of analysis.

### Dimensional Modeling Practice

Here, the professor chose to use MySQL Workbench to create a project for measuring the total book publication sales more
quickly. I made some adjustments to the project, such as:

- I adjusted the fact to book sales, and the publishers became a sub-dimension of books. Personally, I found it strange
that the professor left a book dimension and another for publishers, considering there is a relationship between them.
Therefore, just as the professor chose to adopt a snowflake model in the case of locations (instead of using a region
dimension, she preferred to separate into cities and states), I chose to create the relationship between books and
publishers in the snowflake model.

- Without access to the database, I randomly created some data to be inserted to enrich the project.

- I recall that we had to answer a questionnaire later, involving some queries to obtain the answers. I won't share the
questions, which again follow a more academic format, but I will use the tasks that requested the queries and present
the SQL solutions and the answers to what was requested.

- I chose to use PostgreSQL because I already have a personal container of it in use for other projects.

I will provide the SQL code I used to create tables, constraints, generate data, or manually insert data for this
adapted course project.

```sql
--***************************************************************************************--
--*********************************	TABLES   *********************************--
--***************************************************************************************--

CREATE TABLE "dimPublishers" (
    "skPublisher" INT NOT NULL,
    "nkPublisher" INT NOT NULL,
    "nmPublisher" VARCHAR(150) NOT NULL
);

CREATE TABLE "dimCities" (
    "skCity" INT NOT NULL,
    "nkCity" INT NOT NULL,
    "fk_skState" INT NOT NULL,
    "nmCity" VARCHAR(100) NOT NULL
);

CREATE TABLE "dimStates" (
    "skState" INT NOT NULL,
    "nkState" INT NOT NULL,
    "nmState" VARCHAR(50) NOT NULL,
    "nmUF" CHAR(2) NOT NULL
);

CREATE TABLE "dimTime" (
    "skTime" INT NOT NULL,
    "date" DATE,
    "numDay" VARCHAR(2),
    "nmDay" VARCHAR(20),
    "numMonth" VARCHAR(2),
    "nmMonth" VARCHAR(20),
    "numQuarter" INTEGER,
    "nmQuarter" VARCHAR(20),
    "numYear" INTEGER,
    "flgWeekend" VARCHAR(3),
    "nameSeason" VARCHAR(20)
);

CREATE TABLE "dimBooks" (
    "skBook" INT NOT NULL,
    "nkBook" INT NOT NULL,
    "fk_skPublisher" INT NOT NULL,
    "nmBook" VARCHAR(255) NOT NULL,
    "nmOriginalLanguage" VARCHAR(50) NOT NULL,
    "nmGenre" VARCHAR(25) NOT NULL,
    "nmAuthor" VARCHAR(255) NOT NULL,
    "nmCountryofOrigin" VARCHAR(200) NOT NULL
);

CREATE TABLE "fatBookSales" (
    "fk_skBook" INT NOT NULL,
    "fk_skCity" INT NOT NULL,
    "fk_skTime" INT NOT NULL,
    "qtBooksSold" INT NOT NULL,
    "vlBookSales" NUMERIC(10, 2) NOT NULL
);
--***************************************************************************************--
--*********************************	CONSTRAINTS - PKs   *********************************--
--***************************************************************************************--

ALTER TABLE "dimPublishers" ADD CONSTRAINT skPublisher 
PRIMARY KEY ("skPublisher");

ALTER TABLE "dimCities" ADD CONSTRAINT pk_dimCities 
PRIMARY KEY ("skCity");

ALTER TABLE "dimStates" ADD CONSTRAINT pk_dimStates 
PRIMARY KEY ("skState");

ALTER TABLE "dimTime" ADD CONSTRAINT pk_dimTime 
PRIMARY KEY ("skTime");

ALTER TABLE "dimBooks" ADD CONSTRAINT pk_dimBooks 
PRIMARY KEY ("skBook");

ALTER TABLE "fatBookSales" ADD CONSTRAINT pk_fatBookSales
PRIMARY KEY ("fk_skBook", "fk_skCity", "fk_skTime");

--***************************************************************************************--
--*********************************	CONSTRAINTS - FKs   *********************************--
--***************************************************************************************--

ALTER TABLE "dimCities" ADD CONSTRAINT dimCitiesfk_skState
FOREIGN KEY ("fk_skState") REFERENCES dw_bookstore.book_sales."dimStates" ("skState");

ALTER TABLE "dimBooks" ADD CONSTRAINT dimBooksfk_skPublisher
FOREIGN KEY ("fk_skPublisher") REFERENCES dw_bookstore.book_sales."dimPublishers" ("skPublisher");

ALTER TABLE "fatBookSales" ADD CONSTRAINT fatBookSalesfk_skBook
FOREIGN KEY ("fk_skBook") REFERENCES dw_bookstore.book_sales."dimBooks" ("skBook");

ALTER TABLE "fatBookSales" ADD CONSTRAINT fatBookSalesfk_skCity
FOREIGN KEY ("fk_skCity") REFERENCES dw_bookstore.book_sales."dimCities" ("skCity");

ALTER TABLE "fatBookSales" ADD CONSTRAINT fatBookSalesfk_skTime
FOREIGN KEY ("fk_skTime") REFERENCES dw_bookstore.book_sales."dimTime" ("skTime");


--***************************************************************************************--
--*********************************	TIME DIMENSION SCRIPT   *****************************--
--***************************************************************************************--

-- Inserting data from January to December 2023
CREATE SEQUENCE dimtime_sktime_seq START 1;
 
INSERT INTO "dimTime" (
    "skTime",
    "date",
    "numDay",
    "nmDay",
    "numMonth",
    "nmMonth",
    "numQuarter",
    "nmQuarter",
    "numYear",
    "flgWeekend",
    "nameSeason"
)
SELECT
    NEXTVAL('dimtime_skTime_seq'), -- Generate a sequential value for skTime
    date,
    LPAD(EXTRACT(DAY FROM date)::TEXT, 2, '0'), -- Day
    TO_CHAR(date, 'Day'), -- Day name
    LPAD(EXTRACT(MONTH FROM date)::TEXT, 2, '0'), -- Month
    TO_CHAR(date, 'Month'), -- Month name
    EXTRACT(QUARTER FROM date), -- Quarter
    CASE
        WHEN EXTRACT(QUARTER FROM date) = 1 THEN 'First'
        WHEN EXTRACT(QUARTER FROM date) = 2 THEN 'Second'
        WHEN EXTRACT(QUARTER FROM date) = 3 THEN 'Third'
        WHEN EXTRACT(QUARTER FROM date) = 4 THEN 'Fourth'
    END, -- Quarter name
    EXTRACT(YEAR FROM date), -- Year
    CASE
        WHEN EXTRACT(ISODOW FROM date) IN (6, 7) THEN 'Yes' -- Weekend
        ELSE 'No'
    END, -- Weekend or not
    CASE
        WHEN date BETWEEN '2023-03-21' AND '2023-06-20' THEN 'Autumn'
        WHEN date BETWEEN '2023-06-21' AND '2023-09-22' THEN 'Winter'
        WHEN date BETWEEN '2023-09-23' AND '2023-12-20' THEN 'Spring'
        ELSE 'Summer'
    END -- Season (configured for the Southern Hemisphere)
FROM generate_series('2023-01-01'::date, '2023-12-31'::date, '1 day'::interval) AS date;

--***************************************************************************************--
--*********************************	MANUAL INSERT FOR TRAINING   ************************--
--***************************************************************************************--

--  dimPublishers
INSERT INTO "dimPublishers" ("skPublisher", "nkPublisher", "nmPublisher")
VALUES
    (1, 1, 'Sapphire Books'),
    (2, 2, 'Lionheart Publishers'),
    (3, 3, 'BlueSky Publishing'),
    (4, 4, 'Golden Pen Press'),
    (5, 5, 'SilverLeaf Books'),
    (6, 6, 'RedRose Publishing'),
    (7, 7, 'Emerald Publications'),
    (8, 8, 'Sunset Publishing'),
    (9, 9, 'Crimson Ink'),
    (10, 10, 'OceanView Press');

-- dimBooks
INSERT INTO "dimBooks" ("skBook", "nkBook", "fk_skPublisher", "nmBook", "nmOriginalLanguage", "nmGenre", "nmAuthor", "nmCountryofOrigin")
VALUES
    (1, 1, 7, 'To Kill a Mockingbird', 'English', 'Fiction', 'Harper Lee', 'USA'),
    (2, 2, 4, '1984', 'English', 'Dystopian', 'George Orwell', 'UK'),
    (3, 3, 3, 'Pride and Prejudice', 'English', 'Classic', 'Jane Austen', 'UK'),
    (4, 4, 5, 'The Great Gatsby', 'English', 'Fiction', 'F. Scott Fitzgerald', 'USA'),
    (5, 5, 8, 'Moby-Dick', 'English', 'Adventure', 'Herman Melville', 'USA'),
    (6, 6, 2, 'The Catcher in the Rye', 'English', 'Fiction', 'J.D. Salinger', 'USA'),
    (7, 7, 9, 'War and Peace', 'Russian', 'Historical Fiction', 'Leo Tolstoy', 'Russia'),
    (8, 8, 6, 'The Hobbit', 'English', 'Fantasy', 'J.R.R. Tolkien', 'UK'),
    (9, 9, 10, 'Brave New World', 'English', 'Dystopian', 'Aldous Huxley', 'UK'),
    (10, 10, 1, 'The Lord of the Rings', 'English', 'Fantasy', 'J.R.R. Tolkien', 'UK'),
    (11, 11, 2, 'The Alchemist', 'Portuguese', 'Fiction', 'Paulo Coelho', 'Brazil'),
    (12, 12, 3, 'Crime and Punishment', 'Russian', 'Psychological Fiction', 'Fyodor Dostoevsky', 'Russia'),
    (13, 13, 4, 'The Odyssey', 'Greek', 'Epic Poetry', 'Homer', 'Greece'),
    (14, 14, 5, 'Frankenstein', 'English', 'Gothic Fiction', 'Mary Shelley', 'UK'),
    (15, 15, 6, 'The Adventures of Sherlock Holmes', 'English', 'Mystery', 'Arthur Conan Doyle', 'UK'),
    (16, 16, 7, 'The Road', 'English', 'Post-Apocalyptic', 'Cormac McCarthy', 'USA'),
    (17, 17, 8, 'To the Lighthouse', 'English', 'Modernist', 'Virginia Woolf', 'UK'),
    (18, 18, 9, 'The Grapes of Wrath', 'English', 'Fiction', 'John Steinbeck', 'USA'),
    (19, 19, 10, 'One Hundred Years of Solitude', 'Spanish', 'Magical Realism', 'Gabriel García Márquez', 'Colombia'),
    (20, 20, 1, 'The Hunger Games', 'English', 'Dystopian', 'Suzanne Collins', 'USA'),
    (21, 21, 2, 'The Road Not Taken', 'English', 'Poetry', 'Robert Frost', 'USA'),
    (22, 22, 3, 'The Shining', 'English', 'Horror', 'Stephen King', 'USA'),
    (23, 23, 4, 'The Picture of Dorian Gray', 'English', 'Gothic Fiction', 'Oscar Wilde', 'UK'),
    (24, 24, 5, 'The Martian', 'English', 'Science Fiction', 'Andy Weir', 'USA'),
    (25, 25, 6, 'The Little Prince', 'French', 'Childrens Literature', 'Antoine de Saint-Exupéry', 'France'),
    (26, 26, 7, 'The Girl with the Dragon Tattoo', 'Swedish', 'Mystery', 'Stieg Larsson', 'Sweden'),
    (27, 27, 8, 'The Book Thief', 'English', 'Historical Fiction', 'Markus Zusak', 'Australia'),
    (28, 28, 9, 'Dune', 'English', 'Science Fiction', 'Frank Herbert', 'USA'),
    (29, 29, 10, 'Alices Adventures in Wonderland', 'English', 'Fantasy', 'Lewis Carroll', 'UK'),
    (30, 30, 1, 'The Wind in the Willows', 'English', 'Childrens Literature', 'Kenneth Grahame', 'UK'),
    (31, 31, 2, 'The Count of Monte Cristo', 'French', 'Adventure', 'Alexandre Dumas', 'France'),
    (32, 32, 3, 'The Silent Patient', 'English', 'Psychological Thriller', 'Alex Michaelides', 'UK'),
    (33, 33, 4, 'The Secret Garden', 'English', 'Childrens Literature', 'Frances Hodgson Burnett', 'UK'),
    (34, 34, 5, 'The Kite Runner', 'English', 'Drama', 'Khaled Hosseini', 'Afghanistan'),
    (35, 35, 6, 'The Road Less Traveled', 'English', 'Self-Help', 'M. Scott Peck', 'USA'),
    (36, 36, 7, 'The Bell Jar', 'English', 'Autobiographical Fiction', 'Sylvia Plath', 'USA'),
    (37, 37, 8, 'The Scarlet Letter', 'English', 'Historical Fiction', 'Nathaniel Hawthorne', 'USA'),
    (38, 38, 9, 'A Tale of Two Cities', 'English', 'Historical Fiction', 'Charles Dickens', 'UK'),
    (39, 39, 10, 'The Brothers Karamazov', 'Russian', 'Philosophical Fiction', 'Fyodor Dostoevsky', 'Russia'),
    (40, 40, 1, 'The Hitchhikers Guide to the Galaxy', 'English', 'Science Fiction', 'Douglas Adams', 'UK'),
    (41, 41, 2, 'The Sun Also Rises', 'English', 'Modernist', 'Ernest Hemingway', 'USA'),
    (42, 42, 3, 'The Da Vinci Code', 'English', 'Mystery', 'Dan Brown', 'USA'),
    (43, 43, 4, 'The Color Purple', 'English', 'Epistolary Fiction', 'Alice Walker', 'USA'),
    (44, 44, 5, 'The Hobbit', 'English', 'Fantasy', 'J.R.R. Tolkien', 'UK'),
    (45, 45, 6, 'The Old Man and the Sea', 'English', 'Fiction', 'Ernest Hemingway', 'USA'),
    (46, 46, 7, 'The Name of the Wind', 'English', 'Fantasy', 'Patrick Rothfuss', 'USA'),
    (47, 47, 8, 'The Hound of the Baskervilles', 'English', 'Mystery', 'Arthur Conan Doyle', 'UK'),
    (48, 48, 9, 'The Road to Serfdom', 'English', 'Political Philosophy', 'Friedrich Hayek', 'Austria'),
    (49, 49, 10, 'The Night Circus', 'English', 'Fantasy', 'Erin Morgenstern', 'USA'),
    (50, 50, 1, 'The Handmaids Tale', 'English', 'Dystopian', 'Margaret Atwood', 'Canada');


--dimStates 
INSERT INTO "dimStates" ("skState", "nkState", "nmState", "nmUF")
VALUES
    (1, 1, 'São Paulo', 'SP'),
    (2, 2, 'Rio de Janeiro', 'RJ'),
    (3, 3, 'Minas Gerais', 'MG'),
    (4, 4, 'Espírito Santo', 'ES'),
    (5, 5, 'Paraná', 'PR'),
    (6, 6, 'Santa Catarina', 'SC'),
    (7, 7, 'Rio Grande do Sul', 'RS');

--dimCities
INSERT INTO "dimCities" ("skCity", "nkCity", "fk_skState", "nmCity")
VALUES
    (1, 1, 1, 'São Paulo'),
    (2, 2, 2, 'Rio de Janeiro'),
    (3, 3, 3, 'Belo Horizonte'),
    (4, 4, 4, 'Vitória'),
    (5, 5, 5, 'Curitiba'),
    (6, 6, 6, 'Florianópolis'),
    (7, 7, 7, 'Porto Alegre'),
    (8, 8, 1, 'Campinas'),
    (9, 9, 2, 'Niterói'),
    (10, 10, 3, 'Juiz de Fora');
   
-- 5k random data into fatBookSales without duplicate foreign keys
DO $$
DECLARE
    i INT := 1;
    unique_records INT := 0;
BEGIN
    WHILE unique_records < 5000 LOOP
        BEGIN
            INSERT INTO "fatBookSales" ("fk_skBook", "fk_skCity", "fk_skTime", "qtBooksSold", "vlBookSales")
            VALUES (
                floor(random() * 50) + 1,     -- fk_skBook (foreign key to dimBooks)
                floor(random() * 10) + 1,     -- fk_skCity (foreign key to dimCities)
                floor(random() * 365) + 1,    -- fk_skTime (foreign key to dimTime)
                floor(random() * 100),         -- qtBooksSold (quantity sold)
                (random() * 1000)::numeric(10, 2)  -- vlBookSales (sales value)
            );
            unique_records := unique_records + 1;
        EXCEPTION
            WHEN unique_violation THEN
                -- Handle duplicates (ignore or retry)
                CONTINUE;
        END;
        i := i + 1;
    END LOOP;
END $$;
```

### Answered Questions

**Note**: When I retrieved the challenge document from the first module, I noticed that it asked to create the entire project, but I couldn't find the questions to be answered, except for the test I had already completed, which had few SQL query questions, with many others being theoretical aspects of what we had seen.

Because of this, I created 8 questions adapted to what I had also adapted from the final project of the first module. Many things are quite simple, I know, but the project itself is very basic, educational stuff.

Anyway, if I have time, I will try to create a data visualization in Power BI (outside the scope of the original course, just for practice).

Well, below are the codes and comments with the questions.

```sql
-- Question 1 - Which authors appear more than once in the book dimension?
SELECT "nmAuthor", COUNT(*) AS "TotalBooks"
FROM "dimBooks"?
GROUP BY "nmAuthor"
HAVING COUNT(*) > 1;
```
![q1-m1](https://github.com/Shamslux/DataEngineering/assets/79280485/7a219802-6877-4674-8bd1-73c32be0d4c1)

```sql
-- Question 2 - What are the genres with the highest number of books? Create a rank for these genres.
SELECT
    "nmGenre",
    COUNT(*) AS "TotalBooks",
    DENSE_RANK() OVER (ORDER BY COUNT(*) DESC) AS "GenreRank"
FROM
    "dimBooks" db
GROUP BY
    "nmGenre"
ORDER BY
    "GenreRank";
```
![q2-m1](https://github.com/Shamslux/DataEngineering/assets/79280485/93c27325-7ae8-4f11-8e13-2c564a7d1f9e)

```sql
-- Question 3 - Which original languages have the most literary works in the catalog?
SELECT "nmOriginalLanguage", count(*) AS "TotalBooks"
FROM "dimBooks"
GROUP BY "nmOriginalLanguage"
ORDER BY count(*) DESC;
```
![q3-m1](https://github.com/Shamslux/DataEngineering/assets/79280485/0a7a8a7f-3f9e-4013-8845-63a8ba02c499)

```sql
-- Question 4 - What is the total sales value of the bookstore?
SELECT SUM("vlBookSales") AS "SalesTotal"
FROM "fatBookSales";
```

![q4-m1](https://github.com/Shamslux/DataEngineering/assets/79280485/02aa9894-b469-43e8-b271-8d280a1ba634)

```sql
-- Question 5 - Which books generated the most sales for the bookstore?
SELECT db."nmBook", SUM(fbs."qtBooksSold") AS "TotalValue"
FROM "fatBookSales" fbs
JOIN "dimBooks" db
 ON fbs."fk_skBook" = db."skBook"
GROUP BY db."nmBook"
ORDER BY SUM(fbs."qtBooksSold") DESC;
```

![q5-m1](https://github.com/Shamslux/DataEngineering/assets/79280485/017334ef-1212-4605-9d7b-4779fb225d20)

```sql
-- Question 6 - Which quarters had the highest sales for the bookstore?
SELECT
    dt."nmQuarter",
    SUM(fbs."vlBookSales") AS "TotalSales"
FROM
    "fatBookSales" fbs
JOIN
    "dimTime" dt ON fbs."fk_skTime" = dt."skTime"
GROUP BY
    dt."nmQuarter"
ORDER BY
    "TotalSales" DESC;
```

![q6-m1](https://github.com/Shamslux/DataEngineering/assets/79280485/e82994f3-9772-47d3-bf63-3524a0ee096b)

```sql
-- Question 7 - Which countries have the most books in the bookstore's catalog?
SELECT "nmCountryofOrigin" AS "Country",
       COUNT(*) AS "TotalBooks"
FROM "dimBooks"
GROUP BY "nmCountryofOrigin"
ORDER BY "TotalBooks" DESC;
```

![q7-m1](https://github.com/Shamslux/DataEngineering/assets/79280485/b51581ee-84b1-4fd1-b944-f6048ffca1b8)

```sql
-- Question 8 - Which Brazilian macroregion had the highest quantity of books purchased (quantity, not sales)?
SELECT
    CASE
        WHEN ds."nmUF" IN ('RS', 'SC', 'PR') THEN 'South'
        WHEN ds."nmUF" IN ('SP', 'RJ', 'MG', 'ES') THEN 'Southeast'
        WHEN ds."nmUF" IN ('BA', 'SE', 'AL', 'PE', 'PB', 'RN', 'CE', 'PI', 'MA') THEN 'Northeast'
        WHEN ds."nmUF" IN ('AM', 'RR', 'AP', 'PA', 'TO', 'RO', 'AC') THEN 'North'
        WHEN ds."nmUF" IN ('GO', 'DF', 'MT', 'MS') THEN 'Central-West'
        ELSE 'Other'
    END AS "MacroRegion",
    SUM(fbs."qtBooksSold") AS "TotalQuantityBooks"
FROM
    "fatBookSales" fbs
JOIN
    "dimCities" dc ON fbs."fk_skCity" = dc."skCity"
JOIN
    "dimStates" ds ON dc."fk_skState" = ds."skState"
GROUP BY
    "MacroRegion"
ORDER BY
    "TotalQuantityBooks" DESC;
```
![q8-m1](https://github.com/Shamslux/DataEngineering/assets/79280485/29687a9c-2c62-4031-a0b4-d5449617a4b7)

## OLAP Operations

### Drill Down vs. Drill (Roll) Up

These operations allow you to increase or decrease the level of detail when analyzing a cube.

In this context, performing a "drill down" would, for example, involve switching from viewing sales by country (e.g.,
Brazil) to viewing sales by states, which means increasing the level of detail (decreasing granularity).

"Drill Up" or "Roll Up" is the opposite; you were analyzing, for example, cities, and you increased granularity
(decreased the level of detail) by grouping cities by their respective states.

The image below also helps illustrate this concept using a geographical example on both a macro and micro scale.

![drill-down-roll-up](https://github.com/Shamslux/DataEngineering/assets/79280485/6c2635d2-4b0e-48d3-ad76-f75b89a88ae2)

### Slice

It is the analysis of just one slice of the cube, restricting the values of one dimension, but without reducing the
cardinality of the cube.

![slice](https://github.com/Shamslux/DataEngineering/assets/79280485/deb12001-16a2-4dd5-b508-56f581b42b40)

### Dice

It reduces the dimensions of a cube by eliminating one or more parts of the dimensions by selecting ranges of values.

![dice](https://github.com/Shamslux/DataEngineering/assets/79280485/b246c3d7-01fe-4d44-8cc0-86552314a8a9)


