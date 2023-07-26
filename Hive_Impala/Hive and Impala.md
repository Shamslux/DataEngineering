![RedHat](https://img.shields.io/badge/Red%20Hat-EE0000?style=for-the-badge&logo=redhat&logoColor=white)
![Cloudera](https://img.shields.io/badge/Cloudera-0000FF?style=for-the-badge&logo=cloudera&logoColor=white)
![Apache](https://img.shields.io/badge/Apache-D22128?style=for-the-badge&logo=Apache&logoColor=white)
[![Hive](https://img.shields.io/badge/-Hive-orange?logo=apache%20hive&style=for-the-badge&logoColor=white)](https://hive.apache.org/)
[![Impala](https://img.shields.io/badge/-Impala-black?logo=apache&style=for-the-badge)](https://impala.apache.org/)

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

# Script

The full file is saved in this project folder named as "hive_commands.sh". Here is the snippet of the same code and the images of its results while querying against tables:

```shell
# Create the HDFS directory to receive the files for the car rental company ("locacao" is the Portuguese word for car rental).
hdfs dfs -mkdir /user/cloudera/locacao

# The directory is changed to the Cloudera Downloads folder, where the files downloaded for the project are located. 
#Files are copied to the directory, namely all files of the CSV type.
cd /home/cloudera/Downloads

hdfs dfs -put *.csv /user/cloudera/locacao 

# Use Beeline which is a client to access Hive.
beeline

# Connect to Hive within the Beeline client.
!connect jdbc:hive2://

# Creating, showing and dropping a test database.
create database test;

show database test;

drop database test cascade;

# Creating the locacao (rental) database and using it.
create database locacao;

use locacao;

# Creating the first table in locacao database.

CREATE EXTERNAL TABLE CLIENTES (
	idcliente 		    int
	, cnh			    string
	, cpf			    string
	, validadecnh	    date
	, nome			    string
	, datacadastro	    date
	, datanascimento    date
	, telefone		    string
	, status		    string)

row format delimited fields terminated by ',' STORED AS TEXTFILE;

# "Inserting data" into the table CLIENTES.

LOAD DATA INPATH '/user/cloudera/locacao/clientes.csv' INTO TABLE CLIENTES;

# Querying against the table CLIENTES.

SELECT * FROM CLIENTES;
```

![select_all_against_clientes_result_on_cloudera](https://github.com/Shamslux/DataEngineering/assets/79280485/a3003f5d-2211-4c6e-8dfe-bc9b223960ae)

```shell
# Creating the cars table;

CREATE EXTERNAL TABLE VEICULOS (
	idveiculo           int
    , dataaquisicao     date
    , ano               int
    , modelo            string
    , placa             string
    , status            string
    , diaria            double)

row format delimited fields terminated by ',' STORED AS TEXTFILE;

# "Inserting data" into the table VEICULOS.

LOAD DATA INPATH '/user/cloudera/locacao/veiculos.csv' INTO TABLE VEICULOS;

# Querying against the table VEICULOS.

SELECT * FROM VEICULOS;
```
![select_all_against_veiculos_result_on_cloudera](https://github.com/Shamslux/DataEngineering/assets/79280485/c4bf8f6a-82e9-4b58-83bd-bef0aa8ec66a)

```shell
# Creating the car rental agents (dispatchers) table;

CREATE EXTERNAL TABLE DESPACHANTES (
	iddespachante		int
	, nome 				string
	, status 			string
	, filial			string)

row format delimited fields terminated by ',' STORED AS TEXTFILE;

# "Inserting data" into the table VEICULOS.

LOAD DATA INPATH '/user/cloudera/locacao/despachantes.csv' INTO TABLE DESPACHANTES;

# Querying against the table DESPACHANTES.

SELECT * FROM DESPACHANTES;
```
![select_all_against_despachantes_result_on_cloudera](https://github.com/Shamslux/DataEngineering/assets/79280485/518c8a85-6512-4da0-a7cc-0c6c0be51536)

```shell
CREATE EXTERNAL TABLE LOCACAO (
	idlocacao			int
	, idcliente			int
	, iddespachante		int
	, idveiculo			int
	, idveiculo			int
	, datalocacao		date
	, dataentrega		date
	, total				double)

row format delimited fields terminated by ',' STORED AS TEXTFILE;

# "Inserting data" into the table LOCACAO.

LOAD DATA INPATH '/user/cloudera/locacao/locacao.csv' INTO TABLE LOCACAO;

# Querying against the table LOCACAO.

SELECT * FROM LOCACAO;
```
![select_all_against_locacao_result_on_cloudera](https://github.com/Shamslux/DataEngineering/assets/79280485/9f767fca-1a3a-4852-90fd-72f17fd3f156)

# BI Methodology Overview

Just to briefly explain about the dimensional model. Analyzying this simple project made by Fernando Amaral, we can see a Star-Schema dimensional model with
3 dimensions and 1 fact table. Below we have an image to clearly illustrate the model:

![star_schema_locacao_model](https://github.com/Shamslux/DataEngineering/assets/79280485/5e945344-f598-423d-b6eb-4c2f5668f03c)

# Hive Metadata Commands

## Show Tables

```shell
# Exhibiting the database tables 

show tables;
```
![show_tables_result](https://github.com/Shamslux/DataEngineering/assets/79280485/0dac7012-2da9-46f0-99fc-4eab2330442d)

## Describing a table

```shell
# Describing the table structure

# describe + [table name]
describe clientes;
```
![describe_table_result](https://github.com/Shamslux/DataEngineering/assets/79280485/cc9c6f59-d176-4dbe-94b0-1ecaa1baae05)

## Describing a formatted table structure

```shell
# Describing the formatted table

# describe formatted + [table name]

describe formatted locacao;
```
![describe_formatted_table_result](https://github.com/Shamslux/DataEngineering/assets/79280485/f227a837-bfe9-4111-b90b-c85cffaa8b61)

## Describing a database

```shell
#describe database + [database name]

describe database locacao;
```
![describe_database_result](https://github.com/Shamslux/DataEngineering/assets/79280485/358bfbb0-48dd-4459-a159-b05f9f7bb95a)

## Accessing the Hive catalog

```shell
# Accessing the Hive catalog 

# On terminal (outside beeline), first type

mysql -u root -pcloudera

# After entering MySQL, we can enter metastore
show databases;
use metastore;
```

![entering_mysql](https://github.com/Shamslux/DataEngineering/assets/79280485/63b161e2-921b-4022-985e-5272f27f266e)

```shell
# Now we can exhibit the tables

show tables;
```

![show_tables_metastore](https://github.com/Shamslux/DataEngineering/assets/79280485/fe697035-4910-405f-a847-259ad1ec7768)

These tables store the Hive metadata!

## Checking databases on MySQL

```sql
select * from DBS;
```
![mysql_dbs_result](https://github.com/Shamslux/DataEngineering/assets/79280485/1ca7616a-c59d-4ced-ae5b-ae008b6103bf)

## Checking tables inside a MySQL database by its ID

```sql
select * from TBLS where DB_ID = 3;
```
![tables_inside_mysql_locacao](https://github.com/Shamslux/DataEngineering/assets/79280485/98a8949b-52bb-4981-b1b2-b47fc1276051)

## Querying to check columns of tables in the previous database query

```sql
select * from COLUMNS_V2 where CD_ID = 1;
```
![checking_columns_in_mysql](https://github.com/Shamslux/DataEngineering/assets/79280485/478f20bc-f566-40eb-9078-7dd5fb7dd4b5)

# HiveQL 

## Introduction

- When Facebook (Meta) was creating Hive, it was decided to choose a friendly language. As SQL is high used in data field, it was selected to be used as a base.
- HiveQL stands for Hive Query Language and, as mentioned above, is based on SQL.
- HiveQL follows a similar structure as MySQL.

## HiveQL Queries

### Basic Select

```sql
select	idveiculo
	, dataaquisicao
	, ano
	, modelo
	, placa
        , status
        , diaria
from    veiculos;
```

![hiveql_basic_select_result](https://github.com/Shamslux/DataEngineering/assets/79280485/7376647b-3e71-42cf-b5b3-172383b41052)

### Basic Select using Distinct

```sql
select distinct modelo 
from    veiculos;
```
![hiveql_basic_select_distinct_result](https://github.com/Shamslux/DataEngineering/assets/79280485/55cfeab6-3a7c-473f-9485-52d80d100f81)

### Filtering with Where

```sql
select  *
from    veiculos
where   status <> "Disponivel";
```
![hiveql_where_clause_result](https://github.com/Shamslux/DataEngineering/assets/79280485/da7fe025-7ddf-4ab8-9f60-5f86ce283cfd)

### Filtering with Where (2 conditions)

```sql
select  *
from    veiculos
where   status = "Disponivel"
and     diaria >= 1600;
```
![hiveql_where_two_conditions_result](https://github.com/Shamslux/DataEngineering/assets/79280485/bad9c44c-ac1e-4aa7-aef8-36811d1021a2)

### Using Order By

```sql
select  *
from    locacao
order by datalocacao;
```

![hiveql_order_by_result](https://github.com/Shamslux/DataEngineering/assets/79280485/81d33cff-bdab-48e1-be91-31d8db0df078)





