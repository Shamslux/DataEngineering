# Hive and Impala - Basic Course Overview

This is a summary of the main points studied in the Hive and Impala course taught by instructor Fernando Amaral, 
a Brazilian university professor in the field of Data with extensive experience in Data Engineering and Data Science.

# A little about Hive

## What is Hive?

Hive is an open-source data warehousing and SQL-like query engine built on top of Apache Hadoop. 
It allows users to query and analyze large datasets stored in distributed file systems using a SQL-like language called HiveQL.
It supports data partitioning, bucketing, and indexing for efficient querying, and integrates with various tools and frameworks in the Hadoop ecosystem.

## How does it work in short?

Hive metadata resides, by default, in a MySQL database and processes data that resides within the HDFS system of the Hadoop environment.
Its processing engine is by default MapReduce, but it can be configured to run Tez or Spark.
Hive has a "schema on read" feature, that is, configuring the data metadata, since we are dealing with structured data (column name, data type, etc.)

## Hive tables

- Point to files in HDFS
- Files can be in different formats
- The same file can belong to different tables
- A file can be manipulated by another application
- Deleting a table deletes metadata not data (files)

![hive_multiple_tables_on_same_files_format_files_spark_acessing](https://github.com/Shamslux/DataEngineering/assets/79280485/9627b844-bd08-4ba7-ae3b-969da745f3e4)

As noted above, several formats are possible (in the image we have a CSV file and a Parquet file). 
Multiple tables interact with the same base file (tables contain the metadata and not the data itself) and other applications can interact with the files.

## Databases

- Set of tables defined in a schema
- Not a proprietary file like a DBMS
- The same file can be in different tables in different databases
- Default physical path at: /user/hive/warehouse

## Hive configs

- Active settings in the hive-site.xml file
- Default path at: /etc/hive/conf.dist/
- To change settings in the Hive shell (Beeline client):
- `set hive.default.fileformat = Orc` (in the session, using Beeline, changes the file format)

# Rental Car Overview Project 

![hive_project_overview](https://github.com/Shamslux/DataEngineering/assets/79280485/b4494b3b-3605-4cfa-8a45-77ce2c9bcb2e)

In the image above, we can see the design overview of the data warehouse using Hive. The project is a simple model of a car rental company.
This is the sample project created by instructor Fernando Amaral for this course.

  
