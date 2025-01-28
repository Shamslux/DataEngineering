![Markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)

# The Analogy of the Driving Test

I don’t know how it works in other countries, but in Brazil, when I went to get my driver’s license, it was a terrifying experience. Most people failed, even after hours and hours of theoretical classes on traffic rules and hours of practical lessons supervised by qualified instructors.

By God’s grace, I passed my exam. It was a simple task: all I had to do was drive the car out of a parking spot, follow a straightforward route where the highest gear used was third or fourth, and park again. The test location was a calm area within the large campus of my public federal university at the time.

Once I started the test, I lost points for not looking out the window (the eternal debate about whether we should stick our heads out or not, even though no one actually does this in everyday traffic, relying solely on the rearview mirrors instead).

Later, I started working for a school company where, occasionally, I had to take on tasks as a driver—like going to the supermarket to buy supplies for the school pantry, taking administrative staff to places to resolve issues like buying parts or getting services, and things like taking the car for cleaning or refueling. I was trembling during the first days when I had to drive the car—I couldn’t even shift gears properly. But little by little, I gained real-world experience and managed to improve.

Today, I don’t own a car and don’t work with cars. Recently, I had to drive again and was able to handle everything necessary, despite struggling a bit with the car’s sensitivity (it was new, and I only had experience with much older cars) and driving carefully (which means slowly, compared to the frenzied drivers in this lawless traffic jungle we call Brazil, hehe).

But why am I talking about this? For two reasons:

- **Exams always make everyone nervous.** I was terrified, watching so many people fail, even though they had undergone the same training as I had and were not incompetent—they knew how to drive. 

- **Some might argue:** "Well, now that you have experience, the test would be easy!" No, I highly doubt that because tests are almost always unrealistic, no matter how simple they may seem. In my example, we’re talking about muscle memory, not the kind of memory we develop for things related to IT.

This brings me to why I absolutely hate technical interviews. Every interview is really just a fragment of a developer’s reality. I don’t have "muscle memory" for code. It’s not like when I stop training karate for a month and then return. In that case, it’s like "riding a bike"—my body knows what to do (especially if I let my brain go with the flow of movements instead of overthinking, which would make me freeze—that’s the so-called "empty mind").

If you’re looking at this repository to help you, take heart—everyone feels challenged by these interviews. I feel like the worst developer after failing them. To be fair, I have to admit that I can’t memorize code or explain cases in a few minutes, even simple ones. So, what’s the solution? Practice. I started with the "human" aspect of the interview—how to speak, behave, and structure answers. That’s life, junior! There’s no way around it. It’s one big performance of how you want to present yourself, even if it’s not entirely reflective of reality—which is the saddest part.

I remember being fired from a company, and my manager said, "Leave on a good note; don’t do anything foolish." While I understood the good intentions, I felt offended, as if I lacked character. Just because something bad happens in my life doesn’t mean I’ll abandon my convictions and what I believe is right, even if everything around me crumbles. Interviews are just a slice of reality—you can’t truly know someone except by working with them day to day.

That’s why I take comfort in the friendships I’ve built with my coworkers and the good work I’ve done. This helps ease the embarrassment of my poor performance in some technical interviews because they’re something I hate and am not good at.

So, join me in this repository to explore some case solutions I’ve memorized from a few interviews (not many, I confess—I’m new to the field, with almost three years of experience). Use this repository as a public tool for us to practice and rehearse possible scenarios.

**Note:** I understand that companies use public data for their tests, so I see no issue in sharing them here. Additionally, I won’t reveal which companies the tests are from. Some were private repositories of mine, but I’ll adapt them for this repository and create fictitious company names.

# Technical Cases - Tier 1 

**Tier 1** encompasses cases where the technical interview uses practical examples aimed at simulating day-to-day routines. These can be divided into cases where you are given a proposal to solve within a few days (e.g., 3 days) or cases where you need to solve the problem together with the interviewing manager. Since these represent different levels of difficulty, I will classify the first as **Tier 1A** and the second as **Tier 1S**, as they are more challenging.

## NexaTech Solutions - Tier 1 A

### Intro

This case was part of an interview I had with a large global company for the position of Big Data Engineer. There were three phases. The first was more personalized with HR, the second was the case study, and the third phase was with two managers. I succeeded in the technical interview, but after speaking with the managers, they decided to move forward with another candidate. I don’t feel that I performed poorly overall—it’s likely just the nature of competing with brilliant people out there in the world.

**Note:** Again, "NexaTech Solutions" may exist, but it is not the correct name for the company I am describing. All companies' names are generated by ChatGPT in a random prompt asking for a fictional company name.

### The Case

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![JSON](https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white)
![CSV](https://img.shields.io/badge/CSV-4EA94B?style=for-the-badge&logo=googlesheets&logoColor=white)
![Power BI](https://img.shields.io/badge/PowerBI-F2C811?style=for-the-badge&logo=Power%20BI&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![ChatGPT](https://img.shields.io/badge/chatgpt-343434?style=for-the-badge&logo=openai&logoColor=white)
![VSCode](https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)

### Data Challenge - COVID-19 Public Data

Hello! Welcome to the COVID-19 Data Challenge. This personal challenge was proposed by a company when I participated in
their job application process. I found the proposal fantastic and decided to start the project in my own GitHub
repository. I'm really excited and eager to begin this project because I found the case study to be a lot of fun!

### First Step - Loading tables in a local PostgreSQL DB

The first part of the challenge involves using R or Python to obtain data from a JSON file located at the URL:
https://opendata.ecdc.europa.eu/covid19/nationalcasedeath/json

This file should be retrieved using a programming language and then stored in a PostgreSQL database so that we can
transform the semi-structured data into structured data within the database.

As part of the first step, we also need to load a CSV file into a table in PostgreSQL.

### PostgreSQL on Docker

In this section, we will create the local PostgreSQL database to perform the first part of the challenge. The data
extracted from the JSON will be saved in a table in the PostgreSQL relational database. To do this, I have chosen to use
Docker infrastructure to streamline our project.

I have decided to create a Dockerfile with some basic configurations, essentially pulling the latest image from the
Docker Hub repository and configuring it with basic settings (e.g., local port, superuser password, etc.).

```dockerfile
# Use the official PostgreSQL image from Docker Hub
FROM postgres:latest

# Set the environment variable to accept connections from any host
ENV POSTGRES_HOST_AUTH_METHOD trust

# Specify the standard PostgreSQL port
EXPOSE 5432

# Set the password for the default superuser (change as needed)
ENV POSTGRES_PASSWORD mWAl62H0*u[+]

# Define the startup command
CMD ["postgres"]
```

### Running it on Windows terminal to Docker execute it

Now that we have the Dockerfile script, we will use the Windows terminal on my local machine to execute the command that
will be recognized by the installed Docker, creating the new container for our needs.

```console
REM Loading the image into Docker 
docker build -t img-covid-data-challenge-postgresql -f postgresql_image.dockerfile .

REM Excetuing our created image to create our container
docker run -d -p 5432:5432 --name cnt-covid-data-challenge-postgresql img-covid-data-challenge-postgresql
```

![container_running](https://github.com/Shamslux/COVID19DataChallenge/assets/79280485/cce7757c-06a1-4d68-94e6-79599c40393d)

With that done, we now have the container running properly, and we can proceed with the test connection.

### Basic connection test using Dbeaver

![dbeaver_connection_test_success](https://github.com/Shamslux/COVID19DataChallenge/assets/79280485/a8d6f50b-0c61-47f5-84e5-955b43d04938)

I personally like using DBeaver, and I used this tool to perform the connection test. Any future needs to work with the
SQL database and run SQL queries will be done using this user-friendly interface.

### Setting system environment variables for security

Even though the project may not require this level of security, as a best practice, I will store the database access
password in an environment variable to provide greater security in case the script ends up in a different environment
than the intended server.

![postgresql_security_var](https://github.com/Shamslux/COVID19DataChallenge/assets/79280485/07b3448b-8eb3-4adf-908a-9267408c9293)

### Python script to save the COVID-19 data into PostgreSQL

```python
import requests
import psycopg2
import json
import os

def get_safe_value(item, key, default_value=None):
    return item.get(key, default_value)

# URL of the JSON file
url = "https://opendata.ecdc.europa.eu/covid19/nationalcasedeath/json"

# Download the JSON data
response = requests.get(url)
data = response.json()

# Define your PostgreSQL connection parameters
db_params = {
    "dbname": "postgres",
    "user": "postgres",
    "password": os.environ.get("POSTGRES_PASSWORD"),
    "host": "localhost",
    "port": "5432",
}

# Connect to the PostgreSQL database
try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Define the table structure
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS covid19_data.tb_covid19_data (
            id SERIAL PRIMARY KEY,
            country VARCHAR(255),
            country_code VARCHAR(5),
            continent VARCHAR(255),
            population INT,
            indicator VARCHAR(255),
            year_week VARCHAR(255),
            weekly_count INT,
            rate_14_day FLOAT,
            cumulative_count INT,
            source VARCHAR(255),
            note VARCHAR(255)
        );
    """)

    # Insert the JSON data into the PostgreSQL table
    for item in data:
        country = get_safe_value(item, 'country', 'N/A')
        country_code = get_safe_value(item, 'country_code', 'N/A')
        continent = get_safe_value(item, 'continent', 'N/A')
        population = get_safe_value(item, 'population', None)
        indicator = get_safe_value(item, 'indicator', 'N/A')
        year_week = get_safe_value(item, 'year_week', 'N/A')
        weekly_count = get_safe_value(item, 'weekly_count', None)
        rate_14_day = get_safe_value(item, 'rate_14_day', None)
        cumulative_count = get_safe_value(item, 'cumulative_count', None)
        source = get_safe_value(item, 'source', 'N/A')
        note = get_safe_value(item, 'note', 'N/A')

        cursor.execute("""
            INSERT INTO covid19_data.tb_covid19_data (country, country_code, continent, population, indicator, year_week, weekly_count, rate_14_day, cumulative_count, source, note)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """, (country, country_code, continent, population, indicator, year_week, weekly_count, rate_14_day, cumulative_count, source, note))

    # Commit the transaction
    conn.commit()

    print("Data has been successfully saved to PostgreSQL.")

except Exception as e:
    print("Error:", e)

finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()
```

Above, we have the code used to save the data obtained from the JSON file into the "covid19_data.tb_covid19_data" table
within the default "postgres" database. Below is a screenshot of the query using DBeaver.

![query_result_covid](https://github.com/Shamslux/COVID19DataChallenge/assets/79280485/7db39e0f-4be1-4928-8b19-6d9c2c210dbe)

### Python script to load CSV file into PostgreSQL

```python
import psycopg2
import csv
import os

# Get the value of the DATA_CHALLENGE environment variable
data_challenge_path = os.getenv("DATA_CHALLENGE")

# Check if the environment variable is defined
if data_challenge_path is not None:
    # Build the full path to the CSV file using the environment variable
    csv_file_path = os.path.join(data_challenge_path, "/lake/raw_zone/countries_of_the_world.csv")
    print("Full path to the CSV file:", csv_file_path)
else:
    print("The DATA_CHALLENGE environment variable is not defined.")

# Open and read the CSV file from the local directory
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Skip the header row
    next(csv_reader)

    # Iterate through the rows and trim whitespace from each field
    data = []
    for row in csv_reader:
        trimmed_row = [value.strip() if value else None for value in row]
        # Replace commas with periods in the values
        for i in range(len(trimmed_row)):
            if trimmed_row[i] and ',' in trimmed_row[i]:
                trimmed_row[i] = trimmed_row[i].replace(',', '.')
        data.append(trimmed_row)

# Define your PostgreSQL connection parameters
db_params = {
    "dbname": "postgres",
    "user": "postgres",
    "password": os.environ.get("POSTGRES_PASSWORD"),
    "host": "localhost",
    "port": "5432",
}

# Connect to the PostgreSQL database
try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Define the table structure based on the CSV columns and data types
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS world_data.tb_world_countries (
            id SERIAL PRIMARY KEY,
            country VARCHAR(255) NULL,
            region VARCHAR(255) NULL,
            population NUMERIC NULL,
            area_sq_mi NUMERIC NULL,
            pop_density_per_sq_mi NUMERIC NULL,
            coastline_area_ratio NUMERIC NULL,
            net_migration NUMERIC NULL,
            infant_mortality_per_1000_births NUMERIC NULL,
            gdp_per_capita NUMERIC NULL,  
            literacy_pct NUMERIC NULL,
            phones_per_1000 NUMERIC NULL,
            arable_pct NUMERIC NULL,
            crops_pct NUMERIC NULL,
            other_pct NUMERIC NULL,
            climate NUMERIC NULL,
            birthrate NUMERIC NULL,
            deathrate NUMERIC NULL,
            agriculture NUMERIC NULL,
            industry NUMERIC NULL,
            service NUMERIC NULL
        );
    """)

    # Insert the data into the PostgreSQL table
    for row in data:
        cursor.execute("""
            INSERT INTO world_data.tb_world_countries 
            (country, region, population, area_sq_mi, pop_density_per_sq_mi, coastline_area_ratio, 
            net_migration, infant_mortality_per_1000_births, gdp_per_capita, literacy_pct, phones_per_1000, 
            arable_pct, crops_pct, other_pct, climate, birthrate, deathrate, agriculture, industry, service)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """, tuple(row))

    # Commit the transaction
    conn.commit()

    print("Data has been successfully loaded from CSV to PostgreSQL.")

except Exception as e:
    print("Error:", e)

finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()
```

The code above accesses our simulated Data Lake and retrieves the desired data, subsequently inserting it into the
relational database. Below, you can see the query in DBeaver displaying the successfully loaded data.

![csv_query_result](https://github.com/Shamslux/COVID19DataChallenge/assets/79280485/d2bf8065-26cf-4942-8b3b-f3236f316537)

### Final considerations - Exercise 1 (First step)

Therefore, the loading of tables from both the JSON data source and the CSV data source fulfills the first exercise proposed in the challenge document.

### Second Step - Creating an incremental data pipeline.

The second step of the challenge was to create a data pipeline that could daily fetch data from the URL with JSON
content and update the database. 

Initially, I planned for a more robust infrastructure using Jenkins and an ETL tool (Apache Hop). However, since I don't
have much expertise in infrastructure, I spent two days on this part and wasn't satisfied with the final result. So, I
adopted a simpler approach that still works effectively. The simplified infrastructure consists of a Python script to
update the data based on the "year_week" column and a Windows batch file that runs the Python script, associated with
the task scheduler on my Windows system.

Despite the days spent on it, it was a very valuable learning period, and my knowledge of Docker has improved even more
than what I had practiced in previous courses. In the future, I will calmly use this knowledge in more study projects.

### Python script for updating data

```python
import requests
import psycopg2
import json
import os

def get_safe_value(item, key, default_value=None):
    return item.get(key, default_value)

# URL of the JSON file
url = "https://opendata.ecdc.europa.eu/covid19/nationalcasedeath/json"

# Download the JSON data
response = requests.get(url)
data = response.json()

# Define your PostgreSQL connection parameters
db_params = {
    "dbname": "postgres",
    "user": "postgres",
    "password": os.environ.get("POSTGRES_PASSWORD"),
    "host": "localhost",
    "port": "5432",
}

# Connect to the PostgreSQL database
try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Find the maximum year_week value in the database
    cursor.execute("SELECT MAX(year_week) FROM covid19_data.tb_covid19_data;")
    max_db_year_week = cursor.fetchone()[0]

    # Insert only the new JSON data with a year_week greater than the maximum in the database
    for item in data:
        year_week = get_safe_value(item, 'year_week', 'N/A')
        
        # Compare the year_week from JSON with the maximum year_week in the database
        if year_week > max_db_year_week:
            country = get_safe_value(item, 'country', 'N/A')
            country_code = get_safe_value(item, 'country_code', 'N/A')
            continent = get_safe_value(item, 'continent', 'N/A')
            population = get_safe_value(item, 'population', None)
            indicator = get_safe_value(item, 'indicator', 'N/A')
            weekly_count = get_safe_value(item, 'weekly_count', None)
            rate_14_day = get_safe_value(item, 'rate_14_day', None)
            cumulative_count = get_safe_value(item, 'cumulative_count', None)
            source = get_safe_value(item, 'source', 'N/A')
            note = get_safe_value(item, 'note', 'N/A')

            cursor.execute("""
                INSERT INTO covid19_data.tb_covid19_data (country, country_code, continent, population, indicator, year_week, weekly_count, rate_14_day, cumulative_count, source, note)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """, (country, country_code, continent, population, indicator, year_week, weekly_count, rate_14_day, cumulative_count, source, note))

    # Commit the transaction
    conn.commit()

    print("New data has been successfully saved to PostgreSQL.")

except Exception as e:
    print("Error:", e)

finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()
```

The script above updates the table created in the database. It checks the last record in the "year_week" column and adds
only the new ones compared to what is already registered in the database. To simulate the operation, I obtained the most
recent data from the file and deleted the data for 2023-39 so that 2023-38 would be considered the most recent. After
that, I ran the script, and the result was the insertion of 62 rows for 2023-39 (if you count, you'll notice that each
"year_week" has 62 rows for each unique record).

![deleting_psql](https://github.com/Shamslux/COVID19DataChallenge/assets/79280485/61fecafc-bce2-4e1a-94c2-240791edb2a8)

Above, we can see the deletion in the table to ensure that the maximum value in the "year_week" column (as shown in the image below) remains as 2023-38.

![psql_2023_38](https://github.com/Shamslux/COVID19DataChallenge/assets/79280485/8957b924-2466-4399-877d-220a62714882)

Now the script is executed. I also take the opportunity to show the orchestration. A batch file was created to be executed by the orchestrator:

```console
python %DATA_CHALLENGE%\python\transUpdateCov19PSQLData.py
```

![win_scheduler](https://github.com/Shamslux/COVID19DataChallenge/assets/79280485/21356c7f-ffd3-482b-9fec-bbb572e6db6d)

![new_data_updated!](https://github.com/Shamslux/COVID19DataChallenge/assets/79280485/a3bdc849-83db-45bc-9bdb-e0b94cb0989b)

Finally, the data was successfully updated!

### Final considerations - Exercise 2 (Second step)

I consider that the request for creating a pipeline to update the table in the database has been fulfilled, and it runs
daily at 4 AM. I believe it may not have an ideal infrastructure, but I also think that creating a more robust
infrastructure would have been an extra step beyond the scope of the challenge question. Nevertheless, I hope to return
to projects like this in the future and create that infrastructure for the sheer pleasure of the challenge, in addition
to the wonderful DevOps knowledge that may come from it.

### Third Step - Creating a view with some requested data

The third exercise of the challenge requests the use of the global country data table along with the most recent
COVID-19 data. Now that our database is up to date with the latest incremental data load that I could obtain, I will
outline what the exercise requested and what I have done.

- **The latest number of COVID-19 cases**
- **The cumulative number of COVID-19 cases per 100,000 people for the last 14 days**
- **The date when this information was extracted or recorded**

### The SQL query built
```sql
SELECT wc.country
       , cd.population
       , cd.cumulative_count AS total_cases
       , (cd.rate_14_day * cd.population) / 100000 AS cumulative_number_14d_per_100k
       , CAST(
             MAKE_DATE(SUBSTRING(cd.year_week, 1, 4)::INT, 1, 1) 
             + INTERVAL '1 WEEK' * (SUBSTRING(cd.year_week, 6, 2)::INT - 1) 
             + INTERVAL '1 DAY' * (7 - EXTRACT(DOW FROM MAKE_DATE(SUBSTRING(cd.year_week, 1, 4)::INT, 1, 1))::INT)
         AS DATE) AS data
FROM world_data.tb_world_countries wc
INNER JOIN (
    SELECT country,
           year_week,
           rate_14_day,
           ROW_NUMBER() OVER (PARTITION BY country ORDER BY year_week DESC) as rn
    FROM covid19_data.tb_covid19_data
    WHERE "indicator" = 'cases'
    AND cumulative_count IS NOT NULL
) AS max_year_weeks
ON wc.country = max_year_weeks.country AND max_year_weeks.rn = 1
INNER JOIN covid19_data.tb_covid19_data cd
ON wc.country = cd.country AND max_year_weeks.year_week = cd.year_week
WHERE cd."indicator" = 'cases';
```

### The latest number of COVID-19 cases

To obtain the most recent number of COVID-19 cases for the countries in the list, the following steps were taken:

- The join between the two tables filtered which countries actually appeared in the COVID-19 data.

- The "year_week" column was used to obtain its maximum value, and the "cumulative_count" column was filtered by this
maximum value. This column already contains the updated cumulative data since the beginning of data collection.

- There is a filter to only select items that are cases and not deaths.

- Some countries returned null values, as it appears they have stopped updating their data (e.g., France, Germany,
etc.). For these cases, the query does the following: it scans the "year_week" and retrieves the first non-null value
for the most recent "year_week" (compared to the actually most recent one that did not have null) for these cases.

### The cumulative number of COVID-19 cases per 100,000 people for the last 14 days

To obtain this column, I did the following:

- I used the most recent data from the "rate_14_day" column using the same principles applied to obtain the maximum
value for "year_week" in the previous case.

- I used the data from the "population" column to calculate the rate per 100,000 inhabitants. Initially, I assumed that
the data from the world country table would be more up-to-date, but comparing the data from both tables and searching
for other recent data sources on the Internet, I realized that the data coming from the COVID-19 cases table was closer
to reality than the other table.

- Finally, the calculation was done based on the "rate_14_day" multiplied by the total population and divided by
100,000.

### The date when this information was extracted or recorded

The column with a date was created using the "year_week" column as a basis. In this case, it will bring the date
according to the most recent "year_week" that does not have a null value. If countries continued to send data, the most
recent "year_week" I have is 2023-39, which will give a base date of 2023-10-01 (I'm taking the last day of the
"year_week"). However, if the value came as null, the query will go through the data and find the most updated value
within the available data, which will result in the extracted date being different from the actual most recent one
(i.e., 2023-39).

### View creation

```sql
CREATE OR REPLACE VIEW covid19_data.covid19_view AS
SELECT 
    wc.country,
    cd.population,
    cd.cumulative_count AS total_cases,
    (cd.rate_14_day * cd.population) / 100000 AS cumulative_number_14d_per_100k,
    CAST(
        MAKE_DATE(SUBSTRING(cd.year_week, 1, 4)::INT, 1, 1) 
        + INTERVAL '1 WEEK' * (SUBSTRING(cd.year_week, 6, 2)::INT - 1) 
        + INTERVAL '1 DAY' * (7 - EXTRACT(DOW FROM MAKE_DATE(SUBSTRING(cd.year_week, 1, 4)::INT, 1, 1))::INT)
    AS DATE) AS data
FROM 
    world_data.tb_world_countries wc
INNER JOIN (
    SELECT 
        country,
        year_week,
        rate_14_day,
        ROW_NUMBER() OVER (PARTITION BY country ORDER BY year_week DESC) as rn
    FROM 
        covid19_data.tb_covid19_data
    WHERE 
        "indicator" = 'cases'
        AND cumulative_count IS NOT NULL
) AS max_year_weeks
ON 
    wc.country = max_year_weeks.country AND max_year_weeks.rn = 1
INNER JOIN 
    covid19_data.tb_covid19_data cd
ON 
    wc.country = cd.country AND max_year_weeks.year_week = cd.year_week
WHERE 
    cd."indicator" = 'cases';
```

The query above created the view, and below is a screenshot showing the final result.

![view](https://github.com/Shamslux/COVID19DataChallenge/assets/79280485/a4b07b47-23cd-4f97-bcec-3984b80e22f2)

### Final considerations - Exercise 23 (Third step)

I consider the exercise to be fulfilled. The two tables were related, and the desired columns were selected, providing
interesting information about the 29 listed countries.

### Fourth Step - Performing some requested queries

The fourth exercise requests approximately 6 SQL queries to obtain some information. Each one will be carefully
analyzed. However, I need to clarify something first, as it was a matter of interpretation.

The challenge asks for queries that refer to the date 07/31/2020, but the dataset does not have a precise date column.
It only has the "year_week" column, which is a string column in the format "year-week number." Therefore, if we consider
the week in which the desired date falls, we would have the "year_week" as 2020-31.

However, since the document requested the date with some precision, I assume the desire is indeed an adapted view for
the specified day. Therefore, I decided to use linear interpolation to arrive at a plausible result for what was
requested. For this purpose, the weeks 2020-30 and 2020-31 will be used to attempt to satisfy what was requested for the
specified day.

### 1 What is the country with the highest number of Covid-19 cases per 100 000 Habitants at 31/07/2020?
```sql
WITH week30 AS (
    SELECT 
        country, 
        cumulative_count * 100000.0 / population AS week30_rate,
        population
    FROM 
        covid19_data.tb_covid19_data
    WHERE 
        year_week = '2020-30'
),
week31 AS (
    SELECT 
        country, 
        cumulative_count * 100000.0 / population AS week31_rate,
        population
    FROM 
        covid19_data.tb_covid19_data
    WHERE 
        year_week = '2020-31'
)
SELECT 
    week30.country,
    week30.population,
    week30.week30_rate + 
        (DATE '2020-07-31' - DATE '2020-07-24') * 
        (week31.week31_rate - week30.week30_rate) / 
        (DATE '2020-07-31' - DATE '2020-07-17') AS estimated_rate_per_100k
FROM 
    week30
JOIN 
    week31 ON week30.country = week31.country
ORDER BY 
    estimated_rate_per_100k DESC;
```

The query above satisfied question number 1. As explained earlier, a plausible calculation was made to obtain an
estimate equivalent to the date 07/31/2020. The CTE (Common Table Expression) was used to retrieve data from the two
weeks and perform the final calculation in the outer select. Thus, we arrived at the answer that the country was
Luxembourg.

![query1](https://github.com/Shamslux/COVID19DataChallenge/assets/79280485/e25c09b2-6694-480a-a057-ef9a5d930a27)


### 2 What is the top 10 countries with the lowest number of Covid-19 cases per 100 000 Habitants at 31/07/2020?
```sql
WITH week30 AS (
    SELECT 
        country, 
        cumulative_count * 100000.0 / population AS week30_rate,
        population
    FROM 
        covid19_data.tb_covid19_data
    WHERE 
        year_week = '2020-30'
),
week31 AS (
    SELECT 
        country, 
        cumulative_count * 100000.0 / population AS week31_rate,
        population
    FROM 
        covid19_data.tb_covid19_data
    WHERE 
        year_week = '2020-31'
)
SELECT 
    week30.country,
    week30.population,
    week30.week30_rate + 
        (DATE '2020-07-31' - DATE '2020-07-24') * 
        (week31.week31_rate - week30.week30_rate) / 
        (DATE '2020-07-31' - DATE '2020-07-17') AS estimated_rate_per_100k
FROM 
    week30
JOIN 
    week31 ON week30.country = week31.country
ORDER BY 
    estimated_rate_per_100k ASC
LIMIT 10;
```

It was possible to leverage the logic of the first query and adapt it by reversing the ordering and using a limiting
clause.

![query2](https://github.com/Shamslux/COVID19DataChallenge/assets/79280485/557e8980-34d6-4341-9813-faf8164f8ff3)

### 3 What is the top 10 countries with the highest number of cases among the top 20 richest countries (by GDP per capita)?

```sql
WITH week30 AS (
    SELECT 
        cd.country, 
        cd.cumulative_count * 100000.0 / cd.population AS week30_rate,
        cd.population,
        wc.gdp_per_capita
    FROM 
        covid19_data.tb_covid19_data cd
    JOIN 
        world_data.tb_world_countries wc ON cd.country = wc.country  -- Joining on the country name
    WHERE 
        cd.year_week = '2020-30'
),
week31 AS (
    SELECT 
        c.country, 
        c.cumulative_count * 100000.0 / c.population AS week31_rate,
        c.population,
        wc.gdp_per_capita
    FROM 
        covid19_data.tb_covid19_data c
    JOIN 
        world_data.tb_world_countries wc ON c.country = wc.country  -- Joining on the country name
    WHERE 
        c.year_week = '2020-31'
),
richest_countries AS (
    SELECT 
        country,
        gdp_per_capita
    FROM 
        world_data.tb_world_countries
    ORDER BY 
        gdp_per_capita DESC
    LIMIT 20  -- Getting the top 20 richest countries
)
SELECT 
    week30.country,
    week30.population,
    week30.gdp_per_capita,
    week30.week30_rate + 
        (DATE '2020-07-31' - DATE '2020-07-24') * 
        (week31.week31_rate - week30.week30_rate) / 
        (DATE '2020-07-31' - DATE '2020-07-17') AS estimated_rate_per_100k
FROM 
    week30
JOIN 
    week31 ON week30.country = week31.country
JOIN 
    richest_countries ON week30.country = richest_countries.country  -- Filtering the richest countries
ORDER BY 
    estimated_rate_per_100k DESC
LIMIT 10;  -- Getting the top 10 countries with the highest number of cases
```
Still leveraging part of the previous logic, now the main difference is the use of a new temporary table to obtain GDP
data for countries, which is possible with the other table containing data on countries from around the world.

![query3](https://github.com/Shamslux/COVID19DataChallenge/assets/79280485/27274c8f-8692-470e-b6d9-eb9c02d79380)

### 4 List all the regions with the number of cases per million of inhabitants and display information on population density, for 31/07/2020
```sql
WITH week30 AS (
    SELECT 
        wc1.region,  -
        SUM(cd.cumulative_count) AS total_cases,
        SUM(cd.population) AS total_population,
        SUM(cd.population) / SUM(wc2.area_sq_mi) AS pop_density_per_sq_mi  -- Calculating population density
    FROM 
        covid19_data.tb_covid19_data cd
    JOIN 
        world_data.tb_world_countries wc1 ON cd.country = wc1.country  
    JOIN 
        world_data.tb_world_countries wc2 ON cd.country = wc2.country  
    WHERE 
        cd.year_week = '2020-30'
    GROUP BY 
        wc1.region  
),
week31 AS (
    SELECT 
        wc1.region,
        SUM(cd.cumulative_count) AS total_cases,
        SUM(cd.population) AS total_population
    FROM 
        covid19_data.tb_covid19_data cd
    JOIN 
        world_data.tb_world_countries wc1 ON cd.country = wc1.country  
    WHERE 
        cd.year_week = '2020-31'
    GROUP BY 
        wc1.region
)
SELECT 
    week30.region,
    week30.total_population,
    week30.pop_density_per_sq_mi,
    (week30.total_cases + 
        (DATE '2020-07-31' - DATE '2020-07-24') * 
        (week31.total_cases - week30.total_cases) / 
        (DATE '2020-07-31' - DATE '2020-07-17')) * 1000000 / week30.total_population AS cases_per_million  -- Calculating cases per million
FROM 
    week30
JOIN 
    week31 ON week30.region = week31.region
ORDER BY 
    cases_per_million DESC;
```

The main difference was using a linkage of countries and their regions to calculate the results. The final result can be
seen in the screenshot below.

![query4](https://github.com/Shamslux/COVID19DataChallenge/assets/79280485/c194db0c-0352-49bc-9dad-3cb20fce512d)

### 5 Query the data to find duplicated records
```sql
SELECT 
    year_week, 
    country, 
    COUNT(*) 
FROM 
    covid19_data.tb_covid19_data 
GROUP BY 
    year_week, 
    country 
HAVING 
    COUNT(*) > 1;
```

Well, I'm going to use the same logic that I used in the task of inserting new data. What were the columns I used? The
country and year_week columns, right? So, these two columns serve as a basic template for unique values. Of course, with
the query below, we will have a "duplicate" information, which actually occurs because of the "indicator" column. The
"indicator" column defines the category, such as cases or deaths. In general, we have 31 records for these countries per
year_week, resulting in 62 records due to the cases vs. deaths indicator.

I didn't quite understand what the issue with duplicates would be, as it doesn't seem to have duplicate values in the
present data. However, if it's just to simulate an analysis to ensure data integrity, then I chose to keep the two
columns I used as a basis to ensure this integrity.

![query5](https://github.com/Shamslux/COVID19DataChallenge/assets/79280485/e43ef09c-e3c2-4f41-ba28-0253931ce49f)

### 6 Analyze the performance of all the queries and describes what you see. Get improvements suggestions
```sql
-- Creating an index on the 'country' column
CREATE INDEX idx_country
ON covid19_data.tb_covid19_data (country);

-- Creating an index on the 'year_week' column
CREATE INDEX idx_year_week
ON covid19_data.tb_covid19_data (year_week);
```

A simple solution I thought of was to create indexes for the two columns I noticed are the most accessed, which are
"country" and "year_week." With the application of these indexes, there was a gain of 1ms. Of course, everything may
seem simple and insignificant, but because it's a training data model, if it were a massive volume of data, this gain
would certainly be very welcome.

![query6](https://github.com/Shamslux/COVID19DataChallenge/assets/79280485/e4684fcc-58e2-49ab-a747-759f62e33765)

### Fifth Step - Enhancing the data for further analysis

The fifth exercise requested that we think about enhancements for the existing dataset. Well, what I thought would be
interesting was to add a CSV containing COVID-19 vaccination data worldwide to the data lake and create the simple and
quick Python script below just to load the table into PostgreSQL.

```python
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import os

# Load CSV file
data = pd.read_csv("{REPLACE_ME}\\COVID19DataChallenge\\lake\\raw_zone\\country_vaccinations.csv")

# PostgreSQL connection parameters
db_params = {
    "dbname": "postgres",
    "user": "postgres",
    "password": os.environ.get("POSTGRES_PASSWORD"),
    "host": "localhost",
    "port": "5432",
}

# Create a connection to PostgreSQL
engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["dbname"]}')

# Create table or append data to existing table
data.to_sql('tb_covid19_vacc_data', engine, schema='covid19_data', if_exists='append', index=False)  # changed if_exists from 'replace' to 'append'

# Close the connection
engine.dispose()
```

![quick_csv_result_query](https://github.com/Shamslux/COVID19DataChallenge/assets/79280485/cc14ace1-6b68-4612-9caf-9f068951e576)

### Sixth Step - Analytics

Well, honestly, I need to confess that time is not on my side. I know I won't be able to respond adequately to the last
step, the exercise that seeks insights from the data used in this challenge. I say this because as I write, I'm heading
towards a moment where I have almost 1 hour left before the deadline for submitting this document, and there's still a
lot to document related to the reports.

So, my approach here will be more about presenting the basics of Data Viz, even though it may not bring deeper insights,
but at least simple and basic views, even to demonstrate my knowledge of data analysis and dashboard creation.

I chose to use Power BI to demonstrate this, and I know the dashboard looks very basic, even though I made an effort to
make it look elegant. Of course, the correct business intelligence methodology is not applied (there's no
well-structured cube with facts and dimensions, but only quick views that I created based on the datasets we used
throughout the project).

I'll leave a screenshot of the dashboard, and the file remains available in the project's appropriate folder
(analytics).

![pbi_dash](https://github.com/Shamslux/COVID19DataChallenge/assets/79280485/eb63e7c0-d7ba-42a7-ac9a-02fa59aa2f5b)

I also tried to analyze the following query:

```sql
SELECT
    to_char(a.date::date, 'YYYY-IW') AS year_week,
    a.iso_code,
    a.people_vaccinated,
    b.weekly_count
FROM
    covid19_data.tb_covid19_vacc_data a
JOIN
    covid19_data.tb_covid19_data b
ON
    to_char(a.date::date, 'YYYY-IW') = b.year_week AND a.iso_code = b.country_code
WHERE
    a.iso_code = 'ITA'
ORDER BY
    to_char(a.date::date, 'YYYY-IW'), a.iso_code;
```

![trying](https://github.com/Shamslux/COVID19DataChallenge/assets/79280485/8ef1ad54-bdd7-417c-9d1a-3c9936756292)

The idea was to find a way to analyze if, for example, in Italy, as people were vaccinated, the weekly case counts
decreased over time. It was evident that this was happening, but there were moments when cases would rise again. I don't
have the time now, but it would be interesting, in my view, to evaluate two aspects:

1. The overall validity of the vaccine (e.g., after 3 months, if a person didn't receive the second dose and lost
immunity, resulting in them contracting the disease).

2. The influence of variants.

Point 2 would be more challenging because we would need access to variant data, including the recording period and
location, to calculate their spread and deduce the timeframe in which they were active in a given country, in this case,
Italy, to explain the increase in cases even as the number of vaccinated individuals increased.

There are other questions I would like to analyze in detail as well, such as another dataset I have from Our World Data
that shows details about countries, such as handwashing facilities, the effect of lockdowns, etc. Certainly, this would
be interesting to compare with the COVID-19 and vaccination data we have.

### Final considerations

I acknowledge that I ended up spending a lot of time trying to develop a robust infrastructure, and it cost me precious
time. However, the project covered the entire data journey, ranging from data engineering to analytics. Even though I'm
well-versed in the entire process and have worked as an ETL developer, data analyst, BI analyst, and data engineer, I
decided to invest more time in the initial phase. This is because I aim to specialize more in data engineering rather
than analytics. It's a shame that I couldn't create a more robust infrastructure in time; it would have been great to
bring a better-organized architecture to this project.

Nevertheless, I found the challenge very enjoyable and challenging. It certainly contributed significantly to my
professional growth, given the number of research efforts I had to undertake to find solutions to various challenges and
difficulties that arose along the way.

Honestly, this challenge was one of the best selection process tests I've had the pleasure of taking. So, I can only
congratulate the NexaTech Solutions team and express my gratitude for allowing me to participate in this challenge. Thank you very
much.

**Note**: I basically only changed the name of the real company but reused the entire original project that was in my private repository. For context, it’s been about a year and a half since I went through this selection process.

## Raízen - Tier 1 A

**Raízen tech case is one that I can keep the public name of the company (the real company)**, because I've asked other staff and they told me it is okay to keep it public, so I have here an authorization. The case is similar to the previous
one and it was also very enjoyable (I prefer Tier 1 A cases).

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![LibreOffice](https://img.shields.io/badge/LibreOffice-18A303?style=for-the-badge&logo=LibreOffice&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![VSCode](https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)


### Part 1 - Downloading the file and converting it to XLSX

```python
# ------------------------------------------------------------------------------------------------------------------------------------------------
# ************************************************ Necessary Libraries ***************************************************************************
# ------------------------------------------------------------------------------------------------------------------------------------------------
import requests
import os
import win32com.client as win32
import smtplib
from email.message import EmailMessage

# ------------------------------------------------------------------------------------------------------------------------------------------------
# ************************************************ Python Functions ******************************************************************************
# ------------------------------------------------------------------------------------------------------------------------------------------------
def download_file(url, save_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # This will raise an HTTP error if the status code is not 200 OK
        
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
                
        return True

    except requests.RequestException as e:
        return False

def send_email(subject, body, to_email):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    from_email = 'youremail@gmail.com'  
    password = 'yourpassword' # Well, although just an example, if I would use it, I would create a env variable to preserve the password adding more security           

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)

def convert_xls_to_xlsx(path_to_xls, path_to_xlsx=None):
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    excel.DisplayAlerts = False
    
    wb = excel.Workbooks.Open(path_to_xls)

    if not path_to_xlsx:
        base, ext = os.path.splitext(path_to_xls)
        path_to_xlsx = base + '.xlsx'

    wb.SaveAs(path_to_xlsx, FileFormat=51)  # 51 representa o formato xlsx
    wb.Close()

    excel.Application.Quit()

# ------------------------------------------------------------------------------------------------------------------------------------------------
# **************************************************** Main Section ******************************************************************************
# ------------------------------------------------------------------------------------------------------------------------------------------------

RAIZEN_PATH = os.environ['RAIZEN_CHALLENGE_PATH']

url = 'https://github.com/raizen-analytics/data-engineering-test/raw/master/assets/vendas-combustiveis-m3.xls'
save_path = os.path.join(RAIZEN_PATH, 'docker', 'airflow', 'data', 'bronze_zone', 'vendas-combustiveis-m3.xls') 
new_save_path = os.path.join(RAIZEN_PATH, 'docker', 'airflow', 'data', 'bronze_zone', 'vendas-combustiveis-m3.xlsx') 


if download_file(url, save_path):
    print("File successfully downloaded!")
else:
    print("Failed to download the file.")
    # Send an email notifying about the issue
    subject = "Failed to download file"
    body = "The service to download the file is currently unavailable."
    send_email(subject, body, "recipient@email.com")  # I will not configure the email, just to show some error handling in this first phase


convert_xls_to_xlsx(save_path, new_save_path) 
```

The code above is executed on the host machine, which downloads the file from the internet and places it in the
directory created for the Airflow container. This 'data' directory contains 3 subfolders to simulate the layers of a
data lake (bronze, silver, and gold).

Due to time constraints and not being able to research another solution (I searched for various ways to convert the file
to reveal hidden tabs with cached data, which I could view using LibreOffice, but in the xlsx conversions, I couldn't
maintain these tabs), I decided to adopt the option of running the code on the host machine.

Additionally, my choice to run it on the host and not in the container was also motivated by the Python library
win32com.client, which relies on a Windows environment and Excel to be used as a backend. When using Pandas, the
structure didn't turn out as expected.

Later on, I will show that I can retrieve the cached data using features from the openpyxl library (which is why I
needed to convert to xlsx, as the xls file format is no longer supported by this library).

![file_downloaded_on_bronze_zone](https://github.com/Shamslux/RaizenChallenge/assets/79280485/4f428ab0-7312-4673-973a-43214865d54c)

Note: The code also handles error handling for sending an email in case the URL service is unavailable. It would also
be possible to use the Windows scheduler to schedule the execution of a batch file that would call the script on the
machine. This would be a way to automate and explore what I would have done 'in real life' if I needed to solve this
quickly, and then return to this project later to refine it with more time.

### Part 2 - Airflow pipeline 

```python
# ------------------------------------------------------------------------------------------------------------------------------------------------
# ************************************************ Necessary Libraries ***************************************************************************
# ------------------------------------------------------------------------------------------------------------------------------------------------
from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator
import pandas as pd
import numpy as np
from openpyxl import load_workbook
from openpyxl.pivot.fields import Missing
import os


# ------------------------------------------------------------------------------------------------------------------------------------------------
# ************************************************ Python Functions ******************************************************************************
# ------------------------------------------------------------------------------------------------------------------------------------------------
def checkFileExistence(**kwargs):
    filepath = "/opt/airflow/data/bronze/vendas-combustiveis-m3.xlsx"
    if os.path.exists(filepath):
        msg = True
    else:
        msg = False
    ti = kwargs['ti']
    ti.xcom_push(key='file_exists', value=msg)

def validatingReturn(**kwargs):
    ti = kwargs['ti']
    msg = ti.xcom_pull(task_ids='checkFileExistence', key='file_exists')
    if msg is True:
        return 'fileIsTrue'
    return 'email_alert'

def fileIsTrue():
    # Dictionary mapping month names to month numbers
    month_map = {
    'Jan': '01', 'Fev': '02', 'Mar': '03', 'Abr': '04', 'Mai': '05',
    'Jun': '06', 'Jul': '07', 'Ago': '08', 'Set': '09', 'Out': '10',
    'Nov': '11', 'Dez': '12'
                }
    # Mapping of state names to their respective UF
    state_to_uf = {
    'ACRE': 'AC',
    'ALAGOAS': 'AL',
    'AMAPÁ': 'AP',
    'AMAZONAS': 'AM',
    'BAHIA': 'BA',
    'CEARÁ': 'CE',
    'DISTRITO FEDERAL': 'DF',
    'ESPÍRITO SANTO': 'ES',
    'GOIÁS': 'GO',
    'MARANHÃO': 'MA',
    'MATO GROSSO': 'MT',
    'MATO GROSSO DO SUL': 'MS',
    'MINAS GERAIS': 'MG',
    'PARÁ': 'PA',
    'PARAÍBA': 'PB',
    'PARANÁ': 'PR',
    'PERNAMBUCO': 'PE',
    'PIAUÍ': 'PI',
    'RIO DE JANEIRO': 'RJ',
    'RIO GRANDE DO NORTE': 'RN',
    'RIO GRANDE DO SUL': 'RS',
    'RONDÔNIA': 'RO',
    'RORAIMA': 'RR',
    'SANTA CATARINA': 'SC',
    'SÃO PAULO': 'SP',
    'SERGIPE': 'SE',
    'TOCANTINS': 'TO'
                    }
    
    def process_dataframe(df):
        df_melted = df.melt(id_vars=['COMBUSTÍVEL', 'ANO', 'REGIÃO', 'ESTADO', 'UNIDADE'], 
                        value_vars=['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'], 
                        var_name='month_name', 
                        value_name='volume')
        df_melted['month'] = df_melted['month_name'].map(month_map)
        df_melted['year_month'] = pd.to_datetime(df_melted['ANO'].astype(int).astype(str) + '-' + df_melted['month'].astype(str) + '-01')
        df_melted.drop(columns=['month_name', 'month'], inplace=True)
        return df_melted
    
    file_path = r'/opt/airflow/data/bronze/vendas-combustiveis-m3.xlsx'
    diesel_parquet_path = r'/opt/airflow/data/bronze/diesel_data'
    derivated_parquet_path = r'/opt/airflow/data/bronze/derivated_data'

    workbook = load_workbook(file_path)
    worksheet = workbook['Plan1']

    # Identifying pivot tables in the document
    pivot_names = ['Tabela dinâmica1', 'Tabela dinâmica3']

    dataframes = {}  # Dictionary to store dataframes for each pivot table

    for pivot_name in pivot_names:
        pivot_table = [p for p in worksheet._pivots if p.name == pivot_name][0]

        fields_map = {}
        for field in pivot_table.cache.cacheFields:
            if field.sharedItems.count > 0:
                fields_map[field.name] = [f.v for f in field.sharedItems._fields]

        column_names = [field.name for field in pivot_table.cache.cacheFields]
        rows = []
        for record in pivot_table.cache.records.r:
            # Replace missing fields in the record by NaN
            record_values = [
                field.v if not isinstance(field, Missing) else np.nan for field in record._fields
            ]

            row_dict = {k: v for k, v in zip(column_names, record_values)}

            for key in fields_map:
                row_dict[key] = fields_map[key][row_dict[key]]

            rows.append(row_dict)

        df = pd.DataFrame.from_dict(rows)
    
        # Remove the "TOTAL" column if it exists
        if "TOTAL" in df.columns:
            df.drop("TOTAL", axis=1, inplace=True)
    
        dataframes[pivot_name] = df  # Store dataframe in the dictionary

    df_tabela_dinamica1 = dataframes['Tabela dinâmica1']
    df_tabela_dinamica3 = dataframes['Tabela dinâmica3']

    df_tabela_dinamica1_processed = process_dataframe(df_tabela_dinamica1)
    df_tabela_dinamica3_processed = process_dataframe(df_tabela_dinamica3)

    df_tabela_dinamica1_processed['uf'] = df_tabela_dinamica1_processed['ESTADO'].map(state_to_uf)
    df_tabela_dinamica3_processed['uf'] = df_tabela_dinamica3_processed['ESTADO'].map(state_to_uf)

    df_tabela_dinamica1_processed['product'] = df_tabela_dinamica1_processed['COMBUSTÍVEL']
    df_tabela_dinamica1_processed['unit'] = df_tabela_dinamica1_processed['UNIDADE']

    df_tabela_dinamica3_processed['product'] = df_tabela_dinamica3_processed['COMBUSTÍVEL']
    df_tabela_dinamica3_processed['unit'] = df_tabela_dinamica3_processed['UNIDADE']

    current_timestamp = datetime.now()

    df_tabela_dinamica1_processed['created_at'] = current_timestamp
    df_tabela_dinamica3_processed['created_at'] = current_timestamp


    selected_columns = ['year_month', 'uf', 'product', 'unit', 'volume', 'created_at']

    df_tabela_dinamica1_final = df_tabela_dinamica1_processed[selected_columns]
    df_tabela_dinamica3_final = df_tabela_dinamica3_processed[selected_columns]

    df_tabela_dinamica3_final.to_parquet(
        path=diesel_parquet_path,
        partition_cols=['year_month'],
        engine='pyarrow',  # Specifying pyarrow as the engine, though it should be the default
        index=False        # Avoid writing DataFrame index, which is default
    )

    df_tabela_dinamica1_final.to_parquet(
        path=derivated_parquet_path,
        partition_cols=['year_month'],
        engine='pyarrow',
        index=False
    )

# ------------------------------------------------------------------------------------------------------------------------------------------------
# **************************************************** DAG & Tasks *******************************************************************************
# ------------------------------------------------------------------------------------------------------------------------------------------------
with DAG('raizen_challenge_dag', start_date = datetime(2023,1,1),
         schedule_interval = '@monthly', catchup = False) as dag:

    checkFileExistence = PythonOperator(
        task_id = 'checkFileExistence',
        python_callable = checkFileExistence)
    
    validatingReturn = PythonOperator(
        task_id = 'validatingReturn',
        python_callable = validatingReturn)
    
    fileIsTrue = PythonOperator(
        task_id = 'fileIsTrue',
        python_callable = fileIsTrue)

    email_alert = EmailOperator(
        task_id='email_alert',
        to='company_data_team@company.com', 
        subject='File Not Found Alert',
        html_content='<p>The file was not found in the directory!</p>',
        dag=dag
    )

# ------------------------------------------------------------------------------------------------------------------------------------------------
# **************************************************** Tasks Order *******************************************************************************
# ------------------------------------------------------------------------------------------------------------------------------------------------

    checkFileExistence >> validatingReturn 
    validatingReturn >> [fileIsTrue, email_alert]
```

Above, we have the code for the DAG used in Airflow for the pipeline (well, the second part, as the file acquisition
and conversion started on the host machine), which will:

- Check if the file is in the correct directory.
- If it's not in the correct directory, an email will be sent to the responsible team.
- If it is in the correct directory, transformations are performed to prepare the data according to what was proposed in
the challenge.

![dag_error](https://github.com/Shamslux/RaizenChallenge/assets/79280485/fc5c372d-a13b-49f4-9fae-ce00f039ca2f)

Unfortunately, I couldn't use my current knowledge to successfully execute all tasks. Due to time constraints, I can
only say that I've solved the challenge using a Python script. However, I'll need to revisit this issue later to resolve
it by researching and studying more about Airflow.


### Appendix

### Docker

The docker compose and env files used:

```dockerfile
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

# Basic Airflow cluster configuration for CeleryExecutor with Redis and PostgreSQL.
#
# WARNING: This configuration is for local development. Do not use it in a production deployment.
#
# This configuration supports basic configuration using environment variables or an .env file
# The following variables are supported:
#
# AIRFLOW_IMAGE_NAME           - Docker image name used to run Airflow.
#                                Default: apache/airflow:2.5.1
# AIRFLOW_UID                  - User ID in Airflow containers
#                                Default: 50000
# AIRFLOW_PROJ_DIR             - Base path to which all the files will be volumed.
#                                Default: .
# Those configurations are useful mostly in case of standalone testing/running Airflow in test/try-out mode
#
# _AIRFLOW_WWW_USER_USERNAME   - Username for the administrator account (if requested).
#                                Default: airflow
# _AIRFLOW_WWW_USER_PASSWORD   - Password for the administrator account (if requested).
#                                Default: airflow
# _PIP_ADDITIONAL_REQUIREMENTS - Additional PIP requirements to add when starting all containers.
#                                Default: ''
#
# Feel free to modify this file to suit your needs.
---
version: '3'
x-airflow-common:
  &airflow-common
  # In order to add custom dependencies or upgrade provider packages you can use your extended image.
  # Comment the image line, place your Dockerfile in the directory where you placed the docker-compose.yaml
  # and uncomment the "build" line below, Then run `docker-compose build` to build the images.
  image: ${AIRFLOW_IMAGE_NAME:-apache/airflow:2.5.1}
  # build: .
  environment:
    &airflow-common-env
    AIRFLOW__CORE__EXECUTOR: CeleryExecutor
    AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
    # For backward compatibility, with Airflow <2.3
    AIRFLOW__CORE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
    AIRFLOW__CELERY__RESULT_BACKEND: db+postgresql://airflow:airflow@postgres/airflow
    AIRFLOW__CELERY__BROKER_URL: redis://:@redis:6379/0
    AIRFLOW__CORE__FERNET_KEY: ''
    AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION: 'true'
    AIRFLOW__CORE__LOAD_EXAMPLES: 'true'
    AIRFLOW__API__AUTH_BACKENDS: 'airflow.api.auth.backend.basic_auth,airflow.api.auth.backend.session'
    _PIP_ADDITIONAL_REQUIREMENTS: ${_PIP_ADDITIONAL_REQUIREMENTS:-}
    #PYTHONPATH: '$PYTHONPATH;/python_extended'
  volumes:
    - ${AIRFLOW_PROJ_DIR:-.}/dags:/opt/airflow/dags
    - ${AIRFLOW_PROJ_DIR:-.}/logs:/opt/airflow/logs
    - ${AIRFLOW_PROJ_DIR:-.}/plugins:/opt/airflow/plugins
    - ${AIRFLOW_PROJ_DIR:-.}/data:/opt/airflow/data
    #- ${AIRFLOW_PROJ_DIR:-.}/python:/python_extended Solution together with PYTHONPATH if PIP ADDITIONAL fails

  user: "${AIRFLOW_UID:-50000}:0"
  depends_on:
    &airflow-common-depends-on
    redis:
      condition: service_healthy
    postgres:
      condition: service_healthy

services:
  postgres:
    image: postgres:13
    environment:
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
      POSTGRES_DB: airflow
    volumes:
      - postgres-db-volume:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "airflow"]
      interval: 5s
      retries: 5
    restart: always

  redis:
    image: redis:latest
    expose:
      - 6379
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 30s
      retries: 50
    restart: always

  airflow-webserver:
    <<: *airflow-common
    command: webserver
    ports:
      - 8080:8080
    healthcheck:
      test: ["CMD", "curl", "--fail", "http://localhost:8080/health"]
      interval: 10s
      timeout: 10s
      retries: 5
    restart: always
    depends_on:
      <<: *airflow-common-depends-on
      airflow-init:
        condition: service_completed_successfully

  airflow-scheduler:
    <<: *airflow-common
    command: scheduler
    healthcheck:
      test: ["CMD-SHELL", 'airflow jobs check --job-type SchedulerJob --hostname "$${HOSTNAME}"']
      interval: 10s
      timeout: 10s
      retries: 5
    restart: always
    depends_on:
      <<: *airflow-common-depends-on
      airflow-init:
        condition: service_completed_successfully

  airflow-worker:
    <<: *airflow-common
    command: celery worker
    healthcheck:
      test:
        - "CMD-SHELL"
        - 'celery --app airflow.executors.celery_executor.app inspect ping -d "celery@$${HOSTNAME}"'
      interval: 10s
      timeout: 10s
      retries: 5
    environment:
      <<: *airflow-common-env
      # Required to handle warm shutdown of the celery workers properly
      # See https://airflow.apache.org/docs/docker-stack/entrypoint.html#signal-propagation
      DUMB_INIT_SETSID: "0"
    restart: always
    depends_on:
      <<: *airflow-common-depends-on
      airflow-init:
        condition: service_completed_successfully

  airflow-triggerer:
    <<: *airflow-common
    command: triggerer
    healthcheck:
      test: ["CMD-SHELL", 'airflow jobs check --job-type TriggererJob --hostname "$${HOSTNAME}"']
      interval: 10s
      timeout: 10s
      retries: 5
    restart: always
    depends_on:
      <<: *airflow-common-depends-on
      airflow-init:
        condition: service_completed_successfully

  airflow-init:
    <<: *airflow-common
    entrypoint: /bin/bash
    # yamllint disable rule:line-length
    command:
      - -c
      - |
        function ver() {
          printf "%04d%04d%04d%04d" $${1//./ }
        }
        airflow_version=$$(AIRFLOW__LOGGING__LOGGING_LEVEL=INFO && gosu airflow airflow version)
        airflow_version_comparable=$$(ver $${airflow_version})
        min_airflow_version=2.2.0
        min_airflow_version_comparable=$$(ver $${min_airflow_version})
        if (( airflow_version_comparable < min_airflow_version_comparable )); then
          echo
          echo -e "\033[1;31mERROR!!!: Too old Airflow version $${airflow_version}!\e[0m"
          echo "The minimum Airflow version supported: $${min_airflow_version}. Only use this or higher!"
          echo
          exit 1
        fi
        if [[ -z "${AIRFLOW_UID}" ]]; then
          echo
          echo -e "\033[1;33mWARNING!!!: AIRFLOW_UID not set!\e[0m"
          echo "If you are on Linux, you SHOULD follow the instructions below to set "
          echo "AIRFLOW_UID environment variable, otherwise files will be owned by root."
          echo "For other operating systems you can get rid of the warning with manually created .env file:"
          echo "    See: https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#setting-the-right-airflow-user"
          echo
        fi
        one_meg=1048576
        mem_available=$$(($$(getconf _PHYS_PAGES) * $$(getconf PAGE_SIZE) / one_meg))
        cpus_available=$$(grep -cE 'cpu[0-9]+' /proc/stat)
        disk_available=$$(df / | tail -1 | awk '{print $$4}')
        warning_resources="false"
        if (( mem_available < 4000 )) ; then
          echo
          echo -e "\033[1;33mWARNING!!!: Not enough memory available for Docker.\e[0m"
          echo "At least 4GB of memory required. You have $$(numfmt --to iec $$((mem_available * one_meg)))"
          echo
          warning_resources="true"
        fi
        if (( cpus_available < 2 )); then
          echo
          echo -e "\033[1;33mWARNING!!!: Not enough CPUS available for Docker.\e[0m"
          echo "At least 2 CPUs recommended. You have $${cpus_available}"
          echo
          warning_resources="true"
        fi
        if (( disk_available < one_meg * 10 )); then
          echo
          echo -e "\033[1;33mWARNING!!!: Not enough Disk space available for Docker.\e[0m"
          echo "At least 10 GBs recommended. You have $$(numfmt --to iec $$((disk_available * 1024 )))"
          echo
          warning_resources="true"
        fi
        if [[ $${warning_resources} == "true" ]]; then
          echo
          echo -e "\033[1;33mWARNING!!!: You have not enough resources to run Airflow (see above)!\e[0m"
          echo "Please follow the instructions to increase amount of resources available:"
          echo "   https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#before-you-begin"
          echo
        fi
        mkdir -p /sources/logs /sources/dags /sources/plugins
        chown -R "${AIRFLOW_UID}:0" /sources/{logs,dags,plugins}
        exec /entrypoint airflow version
    # yamllint enable rule:line-length
    environment:
      <<: *airflow-common-env
      _AIRFLOW_DB_UPGRADE: 'true'
      _AIRFLOW_WWW_USER_CREATE: 'true'
      _AIRFLOW_WWW_USER_USERNAME: ${_AIRFLOW_WWW_USER_USERNAME:-airflow}
      _AIRFLOW_WWW_USER_PASSWORD: ${_AIRFLOW_WWW_USER_PASSWORD:-airflow}
      _PIP_ADDITIONAL_REQUIREMENTS: ''
    user: "0:0"
    volumes:
      - ${AIRFLOW_PROJ_DIR:-.}:/sources

  airflow-cli:
    <<: *airflow-common
    profiles:
      - debug
    environment:
      <<: *airflow-common-env
      CONNECTION_CHECK_MAX_COUNT: "0"
    # Workaround for entrypoint issue. See: https://github.com/apache/airflow/issues/16252
    command:
      - bash
      - -c
      - airflow

  # You can enable flower by adding "--profile flower" option e.g. docker-compose --profile flower up
  # or by explicitly targeted on the command line e.g. docker-compose up flower.
  # See: https://docs.docker.com/compose/profiles/
  flower:
    <<: *airflow-common
    command: celery flower
    profiles:
      - flower
    ports:
      - 5555:5555
    healthcheck:
      test: ["CMD", "curl", "--fail", "http://localhost:5555/"]
      interval: 10s
      timeout: 10s
      retries: 5
    restart: always
    depends_on:
      <<: *airflow-common-depends-on
      airflow-init:
        condition: service_completed_successfully

volumes:
  postgres-db-volume:
```
```docker
AIRFLOW_IMAGE_NAME=apache/airflow:2.5.1
AIRFLOW_UID=50000
_PIP_ADDITIONAL_REQUIREMENTS=requests pandas numpy openpyxl os
```
 
### Python script

```python
# ------------------------------------------------------------------------------------------------------------------------------------------------
# ************************************************ Necessary Libraries ***************************************************************************
# ------------------------------------------------------------------------------------------------------------------------------------------------
import numpy as np
import pandas as pd
import os
from datetime import datetime
from openpyxl import load_workbook
from openpyxl.pivot.fields import Missing
# ------------------------------------------------------------------------------------------------------------------------------------------------
# ***************************************************** Extra ************************************************************************************
# ------------------------------------------------------------------------------------------------------------------------------------------------

month_map = {
    'Jan': '01', 'Fev': '02', 'Mar': '03', 'Abr': '04', 'Mai': '05',
    'Jun': '06', 'Jul': '07', 'Ago': '08', 'Set': '09', 'Out': '10',
    'Nov': '11', 'Dez': '12'
}

state_to_uf = {
    'ACRE': 'AC',
    'ALAGOAS': 'AL',
    'AMAPÁ': 'AP',
    'AMAZONAS': 'AM',
    'BAHIA': 'BA',
    'CEARÁ': 'CE',
    'DISTRITO FEDERAL': 'DF',
    'ESPÍRITO SANTO': 'ES',
    'GOIÁS': 'GO',
    'MARANHÃO': 'MA',
    'MATO GROSSO': 'MT',
    'MATO GROSSO DO SUL': 'MS',
    'MINAS GERAIS': 'MG',
    'PARÁ': 'PA',
    'PARAÍBA': 'PB',
    'PARANÁ': 'PR',
    'PERNAMBUCO': 'PE',
    'PIAUÍ': 'PI',
    'RIO DE JANEIRO': 'RJ',
    'RIO GRANDE DO NORTE': 'RN',
    'RIO GRANDE DO SUL': 'RS',
    'RONDÔNIA': 'RO',
    'RORAIMA': 'RR',
    'SANTA CATARINA': 'SC',
    'SÃO PAULO': 'SP',
    'SERGIPE': 'SE',
    'TOCANTINS': 'TO'
}
# ------------------------------------------------------------------------------------------------------------------------------------------------
# ************************************************ Python Functions ******************************************************************************
# ------------------------------------------------------------------------------------------------------------------------------------------------
def process_dataframe(df):
    df_melted = df.melt(id_vars=['COMBUSTÍVEL', 'ANO', 'REGIÃO', 'ESTADO', 'UNIDADE'], 
                        value_vars=['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'], 
                        var_name='month_name', 
                        value_name='volume')

    df_melted['month'] = df_melted['month_name'].map(month_map)

    df_melted['year_month'] = pd.to_datetime(df_melted['ANO'].astype(int).astype(str) + '-' + df_melted['month'].astype(str) + '-01')
    df_melted.drop(columns=['month_name', 'month'], inplace=True)

    return df_melted
# ------------------------------------------------------------------------------------------------------------------------------------------------
# **************************************************** Main Section ******************************************************************************
# ------------------------------------------------------------------------------------------------------------------------------------------------
RAIZEN_PATH = os.environ['RAIZEN_CHALLENGE_PATH']
file_path = os.path.join(RAIZEN_PATH, 'docker', 'airflow', 'data', 'bronze_zone', 'vendas-combustiveis-m3.xlsx')
diesel_parquet_path = os.path.join(RAIZEN_PATH, 'docker', 'airflow', 'data', 'silver_zone', 'diesel_data')
derivated_parquet_path = os.path.join(RAIZEN_PATH, 'docker', 'airflow', 'data', 'silver_zone', 'derivated_data')

workbook = load_workbook(file_path)
worksheet = workbook['Plan1']

pivot_names = ['Tabela dinâmica1', 'Tabela dinâmica3']

dataframes = {}  

for pivot_name in pivot_names:
    pivot_table = [p for p in worksheet._pivots if p.name == pivot_name][0]

    fields_map = {}
    for field in pivot_table.cache.cacheFields:
        if field.sharedItems.count > 0:
            fields_map[field.name] = [f.v for f in field.sharedItems._fields]

    column_names = [field.name for field in pivot_table.cache.cacheFields]
    rows = []
    for record in pivot_table.cache.records.r:
        # Replace missing fields in the record by NaN
        record_values = [
            field.v if not isinstance(field, Missing) else np.nan for field in record._fields
        ]

        row_dict = {k: v for k, v in zip(column_names, record_values)}

        for key in fields_map:
            row_dict[key] = fields_map[key][row_dict[key]]

        rows.append(row_dict)

    df = pd.DataFrame.from_dict(rows)
    
    if "TOTAL" in df.columns:
        df.drop("TOTAL", axis=1, inplace=True)
    
    dataframes[pivot_name] = df  # Store dataframe in the dictionary

df_tabela_dinamica1 = dataframes['Tabela dinâmica1']
df_tabela_dinamica3 = dataframes['Tabela dinâmica3']

df_tabela_dinamica1_processed = process_dataframe(df_tabela_dinamica1)
df_tabela_dinamica3_processed = process_dataframe(df_tabela_dinamica3)

df_tabela_dinamica1_processed['uf'] = df_tabela_dinamica1_processed['ESTADO'].map(state_to_uf)
df_tabela_dinamica3_processed['uf'] = df_tabela_dinamica3_processed['ESTADO'].map(state_to_uf)

df_tabela_dinamica1_processed['product'] = df_tabela_dinamica1_processed['COMBUSTÍVEL']
df_tabela_dinamica1_processed['unit'] = df_tabela_dinamica1_processed['UNIDADE']

df_tabela_dinamica3_processed['product'] = df_tabela_dinamica3_processed['COMBUSTÍVEL']
df_tabela_dinamica3_processed['unit'] = df_tabela_dinamica3_processed['UNIDADE']

current_timestamp = datetime.now()

df_tabela_dinamica1_processed['created_at'] = current_timestamp
df_tabela_dinamica3_processed['created_at'] = current_timestamp

selected_columns = ['year_month', 'uf', 'product', 'unit', 'volume', 'created_at']

df_tabela_dinamica1_final = df_tabela_dinamica1_processed[selected_columns]
df_tabela_dinamica3_final = df_tabela_dinamica3_processed[selected_columns]

df_tabela_dinamica3_final.to_parquet(
    path=diesel_parquet_path,
    partition_cols=['year_month'],
    engine='pyarrow',  # Specifying pyarrow as the engine, though it should be the default
    index=False        # Avoid writing DataFrame index, which is default
)

df_tabela_dinamica1_final.to_parquet(
    path=derivated_parquet_path,
    partition_cols=['year_month'],
    engine='pyarrow',
    index=False
)
```
The code above was used by me to test data processing in Visual Studio to meet the requirements of the challenge. It serves as the foundation for what I later incorporated into the DAG.

### Final Part

![parquet](https://github.com/Shamslux/RaizenChallenge/assets/79280485/1bd9795d-5b0a-4fbf-be0b-c442ed77e4fb)

The image above displays Parquet files partitioned by "year_month." There are two folders, one for derivative fuels data and another for diesel data.

![fuel_d](https://github.com/Shamslux/RaizenChallenge/assets/79280485/ab056efe-0eb7-4be6-b595-3bca9ff6a875)

The image above is a test demonstrating that the total extracted data matches what we have in the source tab. Only the
"TOTAL" column was removed because it's a snippet from the main code where I later perform melting of the DataFrame to
unpivot the months.

![check_fuel](https://github.com/Shamslux/RaizenChallenge/assets/79280485/f902acf5-a9eb-469c-b286-42e4e036cdbf)

The previous images were shown to display the number of rows in the derivative fuels data. Below are the images for
diesel.

![diesel](https://github.com/Shamslux/RaizenChallenge/assets/79280485/384b9d1f-dc8b-4455-8b3d-d4aaf7525d08)

![check_diesel](https://github.com/Shamslux/RaizenChallenge/assets/79280485/44a63d25-1f0a-49c4-af41-29b63bb28c8c)











