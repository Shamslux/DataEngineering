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
