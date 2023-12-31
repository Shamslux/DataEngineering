CREATE TABLE SKEAM_SHOP.PROJECT_PARAMETERS (
	PK_PARAMETERS		INT 			PRIMARY KEY
	, NM_PROJECT		VARCHAR(255)		NOT NULL
	, NM_SUBPROJECT		VARCHAR(255) 		NOT NULL
	, NM_REFERENCE		VARCHAR(255)		NOT NULL
	, TXT_NOTE		VARCHAR(255)
	, NM_VALUE		VARCHAR(255) 	
);




INSERT INTO SKEAM_SHOP.PROJECT_PARAMETERS VALUES (1, 'Pipe', 'Skeam', 'DIM_CLIENTS - Number of days for ETL load', NULL, '90')
INSERT INTO SKEAM_SHOP.PROJECT_PARAMETERS VALUES (2, 'Pipe', 'Skeam', 'DIM_CLIENTS - Number of days for ETL load (business hours)', NULL, '7')
INSERT INTO SKEAM_SHOP.PROJECT_PARAMETERS VALUES (3, 'Pipe', 'Skeam', 'DIM_CLIENTS - Flag of full load', NULL, 'False')
INSERT INTO SKEAM_SHOP.PROJECT_PARAMETERS VALUES (4, 'Pipe', 'Skeam', 'DIM_CLIENTS - Flag loading taking place during Sunday', NULL, 'False')
INSERT INTO SKEAM_SHOP.PROJECT_PARAMETERS VALUES (5, 'Pipe', 'Skeam', 'DIM_CLIENTS - Start date for loading on Sundays', NULL, NULL)
INSERT INTO SKEAM_SHOP.PROJECT_PARAMETERS VALUES (6, 'Pipe', 'Skeam', 'DIM_CLIENTS - Full ELT load start date', NULL, '2013-01-01')
INSERT INTO SKEAM_SHOP.PROJECT_PARAMETERS VALUES (7, 'Pipe', 'Skeam', 'DIM_CLIENTS - Start date', NULL, '2022-01-01')
INSERT INTO SKEAM_SHOP.PROJECT_PARAMETERS VALUES (8, 'Pipe', 'Skeam', 'DIM_CLIENTS - Final date (if null, current date)', NULL, NULL)
INSERT INTO SKEAM_SHOP.PROJECT_PARAMETERS VALUES (9, 'Pipe', 'Skeam', 'DIM_CLIENTS - Email suject', NULL, 'Project Pipe - Skeam - ETL for dimension clients')
INSERT INTO SKEAM_SHOP.PROJECT_PARAMETERS VALUES (10, 'Pipe', 'Skeam', 'DIM_CLIENTS - Email suject', NULL, 'bi.team@emailadress.com')


SELECT	PK_PARAMETERS
	, NM_PROJECT
	, NM_SUBPROJECT
	, NM_REFERENCE
	, TXT_NOTE
	, NM_VALUE
FROM	SKEAM_STG.SKEAM_SHOP.PROJECT_PARAMETERS
WHERE	NM_PROJECT = 'Pipe'
AND	NM_SUBPROJECT = 'Skeam'
AND 	NM_REFERENCE LIKE '%DIM_CLIENTS%'
