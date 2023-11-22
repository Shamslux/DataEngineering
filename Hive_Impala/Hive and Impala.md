![RedHat](https://img.shields.io/badge/Red%20Hat-EE0000?style=for-the-badge&logo=redhat&logoColor=white)
![Cloudera](https://img.shields.io/badge/Cloudera-0000FF?style=for-the-badge&logo=cloudera&logoColor=white)
![Apache](https://img.shields.io/badge/Apache-D22128?style=for-the-badge&logo=Apache&logoColor=white)
[![Hive](https://img.shields.io/badge/-Hive-orange?logo=apache%20hive&style=for-the-badge&logoColor=white)](https://hive.apache.org/)
[![Impala](https://img.shields.io/badge/-Impala-black?logo=apache&style=for-the-badge)](https://impala.apache.org/)
![SQOOP](https://img.shields.io/badge/Apache_SQOOP-00C300?logo=apache&logoColor=white&style=for-the-badge)
# Hive and Impala - Basic Course Overview

This is a summary of the main points studied in the Hive and Impala course taught by instructor Fernando Amaral, 
a Brazilian university professor in the field of Data with extensive experience in Data Engineering and Data Science.

# A little about Hive

## What is Hive (first, as for a 5 years old child understand it!)

Okay, imagine Hive is like a big, busy beehive where lots of little bees live and work together. But instead of bees, it's actually a special place in a computer where information is kept and organized.

In this computer hive, there are different rooms for storing things, just like how we have different drawers and shelves at home. These rooms are called "tables," and each table holds specific types of information, like numbers or words.

Now, to get things done in the hive, we have a friendly bee called the "Queen Bee." The Queen Bee tells all the other bees what to do and how to organize the information in the hive. She's really good at keeping everything in order.

But the cool thing about this hive is that you can ask the Queen Bee questions, and she'll tell you the answers by looking through all the information in the tables. You just have to ask nicely in a special language called "SQL," and she'll give you the information you need.

So, Hive is like a computer beehive where information is stored, organized into tables, and the Queen Bee helps you find what you're looking for when you ask her nicely. It's like a smart and helpful computer bee kingdom!

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

### Using Limit

```sql
select  *
from    veiculos
limit 5;
```

![hiveql_limit_result](https://github.com/Shamslux/DataEngineering/assets/79280485/9537bc1f-54b4-4b7b-aeea-c771135ad4a9)

### Using Order By + Limit

```sql
select  *
from    veiculos
order by dataaquisicao
limit 5;
```

![hiveql_order_by_limit_result](https://github.com/Shamslux/DataEngineering/assets/79280485/a7b3323f-eca5-40bf-9011-8157e958bff2)


### Using Max() Function

```sql
select  max(total)
from    locacao;
```

![hiveql_max_total_from_locacao](https://github.com/Shamslux/DataEngineering/assets/79280485/9a9df5d2-8be0-4d28-b7b5-22e1ae601617)

- This was the max value found in the total column of the table "locacao" (the highest value for one unique transaction registered).

### Using Like

```sql
select	*
from	veiculos
where	modelo like '%T8%';
```

![hiveql_like](https://github.com/Shamslux/DataEngineering/assets/79280485/7cc8006b-d8e9-4315-9ba5-323a54828204)

### Using In

```sql
select	*
from	despachantes
where	filial in ('Santa Maria', 'Novo Hamburgo')
```

![hiveql_in_result](https://github.com/Shamslux/DataEngineering/assets/79280485/27facc98-41e2-494b-bd6a-fac027e24d3d)

### Using Between

```sql
select	*
from	veiculos
where	diaria between 1400 and 1800;
```

![hiveql_between_result](https://github.com/Shamslux/DataEngineering/assets/79280485/90d7cc06-9410-4855-85f5-227880c750b5)

### Basic Join Sample

```sql
select	loc.idlocacao
		, loc.idcliente
		, loc.iddespachante
		, vec.modelo
		, loc.datalocacao
		, loc.dataentrega
		, loc.total
from	locacao loc
join	veiculos vec
on loc.idveiculo = vec.idveiculo;
```

![hiveql_join_result](https://github.com/Shamslux/DataEngineering/assets/79280485/822c1502-2199-4ada-b81a-0af208ce6a85)

### Using Sum

```sql
select	vec.modelo
	, sum(loc.total)
from	locacao loc
join	veiculos vec
on loc.idveiculo = vec.idveiculo
group by vec.modelo;
```

![hiveql_sum_result](https://github.com/Shamslux/DataEngineering/assets/79280485/9a3663e9-a8df-424b-a1f0-f22784523257)

## Using sum() again with dispatchers' table

```sql
select	vec.modelo
	, desp.nome
	, sum(loc.total)
from	locacao loc
join	veiculos vec
on loc.idveiculo = vec.idveiculo
join despachantes desp
on loc.iddespachante = desp.iddespachante
group by vec.modelo, desp.nome;
```
![hiveql_sum_result_2](https://github.com/Shamslux/DataEngineering/assets/79280485/ac191583-1764-4778-ab97-410a31d4c4a0)

## Using having with sum()


```sql
select	vec.modelo
	, desp.nome
	, sum(loc.total)
from	locacao loc
join	veiculos vec
on loc.idveiculo = vec.idveiculo
join despachantes desp
on loc.iddespachante = desp.iddespachante
group by vec.modelo, desp.nome
having sum(loc.total) > 10000;
```
![hiveql_sum_w_having_result](https://github.com/Shamslux/DataEngineering/assets/79280485/b5df9f48-0b98-4b08-8311-c414d437c9d9)

## Using functions

```sql
select	vec.modelo
	, desp.nome
	, sum(loc.total)
from	locacao loc
join	veiculos vec
on loc.idveiculo = vec.idveiculo
join despachantes desp
on loc.iddespachante = desp.iddespachante
where month(loc.datalocacao) = 2
and year(loc.datalocacao) = 2019
group by vec.modelo, desp.nome
```

![hiveql_functions](https://github.com/Shamslux/DataEngineering/assets/79280485/66bfc4fd-be66-4f44-96c8-5a657aec554d)

## Queries for Data Ingestion

**Creating a new table from another table in HiveQL**

```sql
create table locacao2 as select * from locacao where iddespachante = 2;
```
![locacao2_result](https://github.com/Shamslux/DataEngineering/assets/79280485/86277447-a153-43ae-b837-16b7d951cb0f)

**Ingesting data from one database into another**

```sql
create database teste;

create table teste.locacao2 as select * from locacao where iddespachante = 2;

select * from teste.locacao2;
```
The above processes starts and we have this result on terminal:

![teste.locacao2_processing](https://github.com/Shamslux/DataEngineering/assets/79280485/12ec3f32-3517-4d64-a3a6-c4f6fe5eb6d8)

Then, we get the table, in another database, with the data from the current database (locacao):

![teste.locacao2_final_result](https://github.com/Shamslux/DataEngineering/assets/79280485/17dbddab-d47c-4ed4-a51a-9868cd7ebeea)

# Data Ingestion with SQOOP

Here will appear a mini project in SQOOP. The scope of the project will be to use the data from the example database that comes by default in MySQL ("retail_db"). The data from this database will be used to simulate what would happen in real life, that is, to use SQOOP to migrate structured data from a relational database to the distributed environment of HDFS.

## Connecting to the MySQL database

Using the terminal in the Cloudera machine, we are going to access the database system using the below command:

```shell
mysql -u root -pcloudera
```
After connecting to the MySQL database management system (DBMS), we can use an SQL command to connect to the desired database.

```sql
use retail_db;
```

Now, we will use an SQL query to count the number of records in a table. In this case, we will do this for the table called "order_items." This step is important because we need to keep the tables synchronized; that is, we need to later verify if we were able to correctly transfer the right amount of data to HDFS via SQOOP.

```sql
select count(*) from order_items;
```

![order_items_counting_mysql](https://github.com/Shamslux/DataEngineering/assets/79280485/24e372ea-55e4-45ad-9bdf-215323eb1fb1)

## Using SQOOP to import all tables from MySQL's retail_db

```shell
# Accessing MySQL with SQOOP and listing the databases

sqoop list-databases --connect jdbc:mysql://localhost/ --username root --password cloudera
```
![sqoop_showing_all_databases](https://github.com/Shamslux/DataEngineering/assets/79280485/8f772eab-e36d-4122-8ecd-de464f21bf0f)

```shell
# Now showing the existing tables in retail_db

sqoop list-tables --connect jdbc:mysql://localhost/retail_db --username root --password cloudera
```
![sqoop_list_all_tables_retail_db](https://github.com/Shamslux/DataEngineering/assets/79280485/d20f7b74-8eff-44d1-816e-bbbe6b893cba)

```shell
# Creating the retail_db database in Hive

create database retail_db;
```
![creating_retail_db_hive](https://github.com/Shamslux/DataEngineering/assets/79280485/a52c657e-d88c-4748-b5a7-26b1a03f1fb9)

```shell
# Using now SQOOP to import all tables from retail_db (MySQL)
# to retail_db (Hive)

sqoop import-all-tables --connect jdbc:mysql://localhost/retail_db --username root --password cloudera --hive-import --hive-overwrite --hive-database retail_db --create-hive-table --m 1;
```

```sql
-- Comparing the count from order_items in Hive with the one in MySQL
select count(*) from retail_db.order_items;
```
![order_items_count_hive](https://github.com/Shamslux/DataEngineering/assets/79280485/3fdb218b-0881-4547-af33-959e6b126aa3)

We could see that the values for this table are balanced. Of course, it would be correct to check each table (there is also a way to import only the desired table, without all of them). The next step now will be to perform a simulation of an incremental load.

## Incremental Load using SQOOP

Firstly, let's update the "categories" table in the "retail_db" of MySQL. After this update, we will import the updated data with a new SQOOP command. The new command will be able to detect the changes and only bring that alteration into Hive.

```sql
--Inserting a new data into categories table
insert into categories values (59, 8, "Test");
```
![categories_mysql_new_line](https://github.com/Shamslux/DataEngineering/assets/79280485/47490ab0-48b8-4f60-a425-3a5b304c5be0)

Let's run the SQOOP command for this incremental load:

```shell
sqoop import --connect jdbc:mysql://localhost/retail_db --username root --password cloudera --hive-import --hive-database retail_db --check-column category_id --incremental append --last-value 58 --table categories
```

Let's check if the new entry has been reflected in Hive after the SQOOP command:

```sql
select * from retail_db.categories;
```

![categories_hive_new_line_result](https://github.com/Shamslux/DataEngineering/assets/79280485/bf0f722b-6f7f-49a7-a385-fc67249f2ae2)

The image above shows that the procedure that imported the new data (item 59, which appears as a test) was successful.

# Saving in disk using HDFS

It is possible to save Hive queries in the HDFS system. Let's see here some commands (the default and a conversion into a desired format).

```shell
# Saving using HDFS

insert overwrite directory '/user/cloudera/locacao2' select * from locacao.locacao;
```
![hdfs_insert_locacao2_default](https://github.com/Shamslux/DataEngineering/assets/79280485/15fdf492-a62f-46b5-a6a1-8c1a070d263f)

## Default method

![default_list](https://github.com/Shamslux/DataEngineering/assets/79280485/b10efa10-33ac-4b63-9ec6-bd233f33ed40)

By default, HDFS saves the Hive query in the desired directory. It can create multiple serialized JSON files as needed, depending on the data size. Since everything is very small and simple in our example for educational purposes, only one file has been created. The serialized JSON is not readable (i.e., if we use a -cat, it won't be correctly readable). To address this, let's try some conversions of the file into other formats.

## Saving as CSV format

```shell
# Saving as CSV

insert overwrite directory '/user/cloudera/locacao2' 
row format delimited fields terminated by ','
select * from locacao.locacao;
```

![csv_list](https://github.com/Shamslux/DataEngineering/assets/79280485/3ba2a2a6-15e4-4909-baba-013dcc29a7fe)

Now we can access the file using -cat. Note: If you want to save it locally, outside of HDFS, it's also possible; just pass the 'local' parameter and change the directory to a local directory.

![csv_hdfs_cat](https://github.com/Shamslux/DataEngineering/assets/79280485/10133724-f17d-4984-acf4-d2acc3d75403)

## Saving as Parquet format

```shell
# Saving as Parquet

insert overwrite directory '/user/cloudera/locacao2' 
row format delimited fields terminated by ','
stored as parquet
select * from teste.locacao3;
```
Note: To save as Parquet, I needed to create a third table called "locacao" in the test database. This table was created with "cast()" on date columns. An error was occurring, stating that Parquet was not accepting the date format, so I had to convert it. I recommend doing the same if you're trying to reproduce what I'm doing in the repository, although I don't know which version of the Cloudera machine you will be using.

![parquet_hdfs_result](https://github.com/Shamslux/DataEngineering/assets/79280485/16c2edb8-5f30-47e1-9f22-ac905ccebc88)

Although it's not readable using -cat, I still included a screenshot of the terminal just to show that the file was indeed saved correctly as Parquet, as can be seen highlighted by the red rectangle.

# Partitioning and Bucketing

## Partitions

- Divide tables horizontally based on logical and physical partitions.

- A logical partition is a folder in HDFS.

   - For example, it's common to divide files by date, categories, or a region to keep everything logically organized. Note: in the course, the instructor will provide an example of partitioning using vehicle categories.

- The goal of partitioning is query optimization, as the partition is physically separate.
    - For example, when partitioning by vehicles, querying a specific model is more optimized.

- There are no benefits for simple queries.

## Bucketing

- Partitions vary with the data!
   - This leads to a potential problem: thousands or millions of partitions!

- Bucketing doesn't change with the data.
    - It divides physically in a balanced way into buckets.
    - If there are 300 partitions and 50 different data, for example, 250 will remain empty.
    - Great for tables that operate in joins.

## Resuming Partitions and Buckets

In summary, partitioning is a technique that organizes data based on specific column values to facilitate the filtering of relevant data in queries, while bucketing is a technique that divides data into uniform buckets to enhance parallelism and data distribution in files. Both techniques can be used to optimize query performance in Hive, depending on the specific requirements of your use case.

## Creating a partitioned table

```sql
-- Creating table for partitioning

create table locacao.locacaoanalitico (
	cliente string, 
	despachante string, 
	datalocacao date,
	total double
	) 
partitioned by (veiculo string);
```
![creating_locacaoanalitico](https://github.com/Shamslux/DataEngineering/assets/79280485/ed0dd547-cc1b-48ec-8cfc-2c68e32b77df)

## Preparing environment for partitioning and bucketing

```shell
set hive.exec.dynamic.partition.mode;
set hive.exec.dynamic.partition.mode=nonstrict;
```

## Inserting data into the new column with partitioning

```sql
insert overwrite table locacao.locacaoanalitico partition (veiculo)
select cli.nome
	   , des.nome
	   , loc.datalocacao
	   , loc.total
	   , veic.modelo
from locacao loc
join despachantes des 
on (loc.iddespachante = des.iddespachante)
join clientes cli 
on (loc.idcliente = cli.idcliente)
join veiculos veic
on (loc.idveiculo = veic.idveiculo);
```

## Checking files partitionated using HDFS

```shell
hdfs dfs -ls /user/hive/warehouse/locacao.db/locacaoanalitico
```

![partitions_hdfs_result](https://github.com/Shamslux/DataEngineering/assets/79280485/55288251-a7da-4db9-ae69-47872fab4943)

## Creating a table for bucketing

```sql
create table locacaoanalitico2 (
	cliente string,
	despachante string,
	datalocacao date,
	total double,
	veiculo string
)
clustered by (veiculo) into 4 buckets;
```

## Inserting into locacaoanalitico2 (bucketing)

```sql
insert overwrite table locacao.locacaoanalitico2
select cli.nome
	   , des.nome
	   , loc.datalocacao
	   , loc.total
	   , veic.modelo
from locacao loc
join despachantes des 
on (loc.iddespachante = des.iddespachante)
join clientes cli 
on (loc.idcliente = cli.idcliente)
join veiculos veic
on (loc.idveiculo = veic.idveiculo);
```
# Temporary tables
- A temporary table only exists while the system session is in progress, so when the session ends, it is deleted.
  
-  A temporary table can be a good resource to be used for data transformation from one structure to another.

# Views

- Allows more complex queries to be made easier for non-technical users (e.g., instead of a query with multiple joins, a non-technical user can access a view that already has the code ready and, from there, simply use a simple query against that view).

**Note: Of course, views in relational databases go beyond that, but this was the simple explanation given by the instructor for the course in question.**

## Creating a temporary table

```sql
create temporary table temp_des as select * from despachantes;
```

## Checking data from the temp table

```sql
select * from temp_des;
```
![temp_des_result](https://github.com/Shamslux/DataEngineering/assets/79280485/1580530d-3d3f-42d3-933b-dffa4611934d)

## Disconnecting from hive

```shell
!q
```

## Re-entering into Hive through Beeline

```shell
beeline

!connect jdbc:hive2://
```

When a user exits the Hive session, the temporary tables created in that session are deleted. This means that if a user tries to query a temporary table in a new session, an error will be returned.

![temp_des_error](https://github.com/Shamslux/DataEngineering/assets/79280485/1a153d92-e93c-42e4-80d0-07c92ff202cd)

## Creating a view

```sql
create view if not exists locacaoview as
select cli.nome as cliente
	   , des.nome as despachante
	   , loc.datalocacao as data
	   , loc.total as total
	   , veic.modelo as veiculo
from locacao loc
join despachantes des 
on (loc.iddespachante = des.iddespachante)
join clientes cli 
on (loc.idcliente = cli.idcliente)
join veiculos veic
on (loc.idveiculo = veic.idveiculo);
```

## Querying against the view created

```sql
select * from locacaoview;
```

![view_result](https://github.com/Shamslux/DataEngineering/assets/79280485/e30269a2-a491-49fc-852e-826d006779fd)

# ORC

ORC stands for Optimized Row Columnar, a file format that is becoming the standard for structured data in this ecosystem.

Some features of ORC are:

- It is a compressed binary format;
- It is columnar-oriented;
- It can be a file with up to 75% smaller size reduction;
- It is optimized for analysis;
- It is becoming the standard in Hadoop Data Lakes.

![ocr_amaral_explanation_line_column](https://github.com/Shamslux/DataEngineering/assets/79280485/5a1d13a3-47f0-4ef3-8112-0223b6feb203)

In the image above, we can see how there is a greater tendency for data repetition in the columns, so data compression will work better because it is column-oriented and not row-oriented.

In row-oriented relational databases, even if your query selects a few columns, it will first load all the data, since they are physically in the same file.

In the case of columnar orientation, each column is stored independently on disk, which gives an advantage when querying, so if two columns are selected, only those two will be loaded.

To enable Hive to handle ORC format, you need to use appropriate settings. These settings are done at the server level or at the table level.

By default, Hive saves files in text file format.

The default compression is ZLIB, but it can be changed to NONE, ZLIB, and SNAPPY.

Indexes are created by default in ORC files, but this setting can also be changed to deny index creation.

## Creating table configured for ORC format file

```sql
create external table clientes_orc (
	idcliente int,
	cnh string,
	cpf string,
	validadecnh date,
	nome string,
	datacadastro date,
	datanascimento date,
	telefone string,
	status string
)
stored as orc;
```

The query above will create an external table that will be configured to be stored as ORC.

# Support for transactions in Hive.

- Hive operates on HDFS, which means that updating data requires involvement of multiple nodes.

- By default, Hive does not support UPDATE and DELETE operations, partly due to the nature of Data Warehousing where these actions are not commonly performed routinely.

- It is possible to change the transaction settings in Hive.

- In order for a table to accept UPDATE and DELETE transactions, the following requirements must be met:

    - Manageable (cannot be external)
    - Part of the cluster
    - Stored in ORC format
    - Possesses transactional property

## Checking how is Hive support for transactions

```shell
set hive.support.concurrency;
```
![hive_support_concurrency_result](https://github.com/Shamslux/DataEngineering/assets/79280485/13ae00e1-5c75-408c-85a6-dca9289c21c2)

## Editing Hive settings for give support to transactions

```shell
sudo gedit /etc/hive/conf.dist/hive-site.xml
```
## Inserting this below information in the tag <configuration>

```xml
<property>
		<name>hive.support.concurrency</name>
		<value>true</value></property>
<property>
		<name>hive.txn.manager</name>
		<value>org.apache.hadoop.hive.ql.lockmgr.DbTxnManager</value>
</property><property>
		<name>hive.compactor.initiator.on</name>
		<value>true</value>
</property>
<property>
		<name>hive.compactor.worker.threads</name>
		<value>1</value>
</property>
```
![property_result](https://github.com/Shamslux/DataEngineering/assets/79280485/a0ae1e67-ec14-4d2f-8091-81f8742d6a43)

## Stopping Hive service (for re-initialization)
```shell
sudo service hive-server2 stop
```
## Starting Hive service (for re-initialization)
```
sudo service hive-server2 start
```
## Quitting Beeline
```shell
!q
```
## Checking how is Hive support for transactions (again)
```shell
set hive.support.concurrency;
```

![hive_support_concurrency_new_result](https://github.com/Shamslux/DataEngineering/assets/79280485/c78c1d2f-45bb-4962-b6c5-ca0f00867648)

Now we are able to perform transactions involving UPDATE and DELETE, which were not natively supported by Hive before.

# Other optimization techniques

We will look at 3 more optimization techniques, namely:

- Vectorization
- Cost-Based Optimization
- Engine (Spark)

## Vectorization

Vectorization reduces the use of CPU in queries, making query execution faster. By default, MapReduce processes one line
at a time, but with vectorization, it processes 1024 lines in blocks.

For vectorization to work, the format must be ORC, and the configuration parameter must be used (see further in the
document).

Here, a test involving a join of two tables in ORC format will be performed. Since the data is very small, just for
testing purposes, little difference will be observed. However, it should be kept in mind that this optimization becomes
significant when dealing with a massive volume of data in real-world scenarios.

### Creating new table locacao_orc
```sql
create external table locacao_orc (
	idlocacao int, 
	idcliente int,
	iddespachante int,
	idveiculo int,
	datalocacao date,
	dataentrega date,
	total double
) stored as orc;
```

### Inserting data into the new locacao_orc table
```sql
insert overwrite table locacao_orc  select * from locacao;
```
### Preparing query with join to test query speed
```sql
select loc.datalocacao,
	   loc.total,
	   cli.nome
from locacao_orc loc
join clientes_orc cli
 on (loc.idcliente = cli.idcliente);
```
![result_before_vectorization](https://github.com/Shamslux/DataEngineering/assets/79280485/ceab6ba9-13bd-49d1-917b-a3216a39761c)

The image above shows the result of the query without vectorization enabled. Below, we will start the process of
changing the parameter to activate vectorization and then execute the same query again to check the decrease in time.

### Checking if vectorization is enabled or not

```shell
set hive.vectorized.execution.enabled;
```

![checking_vectorization_enabled_or_not](https://github.com/Shamslux/DataEngineering/assets/79280485/e036ee39-3768-479d-a013-96ae83130086)

### Changing vectorization to "enabled" for testing
```shell
set hive.vectorized.execution.enabled = true;
```

![vectorization_now_enabled](https://github.com/Shamslux/DataEngineering/assets/79280485/33352869-aaaa-4817-9e05-1789a60c4ed3)

![query_after_vectorization](https://github.com/Shamslux/DataEngineering/assets/79280485/e85228da-1aee-4c2e-9251-3735e7642f1a)

As mentioned initially, the change would not be very significant because we are using a small database for testing
purposes. However, when we consider real-world scenarios dealing with Big Data, this difference can be crucial for
handling data efficiently.

## Cost Base Otimization

CBO is a way to collect statistics to improve the performance of queries.

To use it, you need to adjust parameters and, if tables have already been created, you need to force the collection of
these statistics by passing specific commands.

However, it is important to be aware of the trade-off when using this feature, as it can generate a significant overhead
from data collection after activation. This should be taken into account in the advantages and disadvantages for the use
case.

### Query for getting a sum, this query will be used for the CBO performance test
```sql
select sum(total) from locacao_orc;
```
![before_cbo](https://github.com/Shamslux/DataEngineering/assets/79280485/a185a37a-761f-4b99-95d1-4ecee082e3a5)

The image above is the query executed before the CBO parameters were activated.

### Adjusting the parameters
```shell
set hive.cbo.enable=true;
set hive.compute.query.using.stats=true;
set hive.stats.fetch.column.stats=true;
set hive.stats.fetch.partition=true;
```

![after_cbo](https://github.com/Shamslux/DataEngineering/assets/79280485/39e92f0f-ef62-4d3f-804a-d013d9cc6630)

Now we can see that, after changing the parameters, we have a faster query result. Again, note that we had a not so high
difference because it is a small amount of test and study data, but in real-world scenarios this would make a bigger
difference.

## Engine (Spark)

The default engine for Hive is MapReduce. The advantage of this engine is its ability to handle large volumes of data,
however, there is a high latency, because its process is in batch, divided into mapping, shuffle and execution.

Tez (needs to be installed in this Cloudera version, it will not be used) and Spark are other possible engines.

Spark was not made for Hive, but can be used in Hive. It is an important tool in the Hadoop ecosystem. It is capable of
processing data in real time, is compatible with MapReduce, processes data in memory, on disk, or in a hybrid way
(memory and disk), can run in a cluster, and is fully Open Source.

Spark can be used by updating parameters to run it in a query or adjusting on the server (which makes Spark always
used).

### Reusing the previous query for testing

Using again this query for testing
```sql
select loc.datalocacao,
	   loc.total,
	   cli.nome
from locacao_orc loc
join clientes_orc cli
 on (loc.idcliente = cli.idcliente);
```

![result_mr](https://github.com/Shamslux/DataEngineering/assets/79280485/bf797ae2-0c11-45ba-81c1-2dbb4b6c0dac)


### Changing the engine for this query

 set hive.execution.engine=spark;

 ![result_spark](https://github.com/Shamslux/DataEngineering/assets/79280485/b406176f-0665-47c8-aadd-01ccabc3b5a1)

It is possible to see that there was a good optimization of the query time using the Spark engine.

 




