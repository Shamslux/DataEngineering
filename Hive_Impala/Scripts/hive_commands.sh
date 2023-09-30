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

# Creating the car rental agents (dispatchers) table;

CREATE EXTERNAL TABLE DESPACHANTES (
	iddespachante		int
	, nome 				string
	, status 			string
	, filial			string)

row format delimited fields terminated by ',' STORED AS TEXTFILE;

# "Inserting data" into the table DESPACHANTES.

LOAD DATA INPATH '/user/cloudera/locacao/despachantes.csv' INTO TABLE DESPACHANTES;

# Querying against the table DESPACHANTES.

SELECT * FROM DESPACHANTES;

# Creating the rental table;

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

# Metadata Commands

# Exhibiting the database tables 

show tables;

# Describing the table structure

# describe + [table name]
describe clientes;

# Describing the formatted table

# describe formatted + [table name]

describe formatted locacao;

# Describing databases

#describe database + [database name]

describe database locacao;

# Accessing the Hive catalog 

# On terminal (outside beeline), first type

mysql -u root -pcloudera

# After entering MySQL, we can enter metastore
show databases;
use metastore;

# Now we can exhibit the tables

show tables;

# Cheking databases on MySQL

select * from DBS;

# Checking tables inside a MySQL database by its ID

select * from TBLS where DB_ID = 3;

# Querying to check columns of tables in the previous database query

select * from COLUMNS_V2 where CD_ID = 1;

# Creating a new table from another table in HiveQL

create table locacao2 as select * from locacao where iddespachante = 2;

# Ingesting data from one database into another

create database teste;

create table teste.locacao2 as select * from locacao where iddespachante = 2;

select * from teste.locacao2;
#############################################################################
############################# SQOOP MINI PROJECT ############################
#############################################################################

# Firstly, loging into MySQL

mysql -u root -pcloudera

# Connecting to the sample database that will be used
# for this mini project

use retail_db;

# Couting the Orders' table (as an example)

select count(*) from order_items;

# Accessing MySQL with SQOOP and listing the databases

sqoop list-databases --connect jdbc:mysql://localhost/ --username root --password cloudera

# Now showing the existing tables in retail_db

sqoop list-tables --connect jdbc:mysql://localhost/retail_db --username root --password cloudera

# Creating the retail_db database in Hive

create database retail_db;

# Using now SQOOP to import all tables from retail_db (MySQL)
# to retail_db (Hive)

sqoop import-all-tables --connect jdbc:mysql://localhost/retail_db --username root --password cloudera --hive-import --hive-overwrite --hive-database retail_db --create-hive-table --m 1

# Comparing the count from order_items in Hive with the one in MySQL

select count(*) from retail_db.order_items;

# Inserting a new data into categories table

insert into categories values (59, 8, "Test");

# Using the SQOOP command to incremental load

sqoop import --connect jdbc:mysql://localhost/retail_db --username root --password cloudera --hive-import --hive-database retail_db --check-column category_id --incremental append --last-value 58 --table categories 

# Checking if new line appeared in Hive

select * from retail_db.categories;

# Saving using HDFS

insert overwrite directory '/user/cloudera/locacao2' select * from locacao.locacao;

# Checking the created file in HDFS

hdfs dfs -ls /user/cloudera/locacao2

# Saving as CSV

insert overwrite directory '/user/cloudera/locacao2' 
row format delimited fields terminated by ','
select * from locacao.locacao;

# Saving as Parquet

insert overwrite directory '/user/cloudera/locacao2' 
row format delimited fields terminated by ','
stored as parquet
select * from teste.locacao3;

# Changing the default to work with partitioning and bucketing

set hive.exec.dynamic.partition.mode;
set hive.exec.dynamic.partition.mode=nonstrict;

# Creating table for partitioning

create table locacao.locacaoanalitico (
	cliente string, 
	despachante string, 
	datalocacao date,
	total double
	) 
partitioned by (veiculo string);

# Inserting data into the new column with partitioning

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

# Checking files partitionated using HDFS

hdfs dfs -ls /user/hive/warehouse/locacao.db/locacaoanalitico