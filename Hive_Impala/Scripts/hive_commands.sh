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


