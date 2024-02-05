![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![ChatGPT](https://img.shields.io/badge/chatgpt-343434?style=for-the-badge&logo=openai&logoColor=white)

<div align="right">
  <img src="https://github.com/Shamslux/DataEngineering/assets/79280485/fffa0fdc-4cf8-4845-8e51-9cf7d9bb9900" alt="Badge" width="200">
</div>


# SQL Review Course with ChatGPT

I have a dear friend - who, by the way, helped me get into the Data field - who always reminds me that we should
practice SQL a lot. Currently, I have 2 years of experience in the field, always working with SQL.

However, it's always good to review the basic contents. With that in mind, and with a desire to test ChatGPT's ability
to generate interesting questions to aid human learning, I decided to request some questions from it to practice SQL.

The database I used is a personal database created for study purposes, created by me last year, to practice Business
Intelligence and Data Engineering projects. However, I prefer to review the basics and practice with some tools before
consolidating everything into a large skills demonstration project.

# Mini Project's Structure

This small project is based on the fictional dataset of a game store called "Skeam." They sell games from various
platforms, categories, etc., to users from around the world.

This training will aim to create 100 questions for junior, mid-level, and senior professional levels.

In addition to the folders with scripts and solutions, this document will also record the solutions with images (I will
update as time permits, so there may be a discrepancy between what is in the script and what is updated in this
document).

I will not share the database now, but I will share it when I create a more robust project in the future. Feel free to
adapt the questions used for your personal projects.

Some questions ended up repeating, probably, even though I asked ChatGPT to avoid this. In fact, the idea was to create
500 junior-level questions, but given the limited dataset, everything started to become uncomfortably repetitive, so I
decided it would be better to limit all questions to just 100 per professional hierarchical level.


# 100 Junior Questions Solutions

<div align="right">
  <img src="https://github.com/Shamslux/DataEngineering/assets/79280485/fa7d8997-be71-40a2-bd8f-899d306a4196" alt="Badge" width="150">
</div>

## 1. List all games from the tb_games table.

```sql
SELECT	nm_title 
FROM	tb_games;
```

![s1_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/42007bcd-2a05-4ce4-a942-190d57962de3)

## 2. Show the names and release years of games from the tb_games table.

```sql
SELECT	nm_title
		, nm_release_year 
FROM	tb_games;
```

![s2_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/0dfa032f-655f-4a2c-9660-b2e9d1846c11)

## 3. Find all games released in 2010.

```sql
SELECT	nm_title 
FROM	tb_games
WHERE	nm_release_year = '2010';
```

![s3_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/ffe62c0e-f9ab-406f-b979-d0744b1c4e64)

## 4. Select all customers from the tb_client table.

```sql
SELECT	nm_client
FROM	tb_client;
```
![s4_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/79f73c66-c262-444c-829f-5513b7fcae20)

## 4. Select all customers from the tb_client table.

```sql
SELECT	nm_client
FROM	tb_client
```

![s4_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/10b8f257-5d6d-406e-a1f6-0608573cc2d4)

## 5. List the names of customers and their countries from the tb_client table.

```sql
SELECT	nm_client 
        , nm_country 
FROM	tb_client;
```
![s5_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/c59bd459-3e1f-45a7-a7f8-7ee3889a3654)

## 6. Show the names and emails of customers born before 1990.

```sql
SELECT	nm_client 
		, txt_email 
FROM	tb_client
WHERE	EXTRACT(YEAR FROM dt_birthdate) < 1990;
```

![s6_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/fc935535-717b-4f8f-b903-cd68faf4616c)

## 7. Find all games in the 'Action' category.

```sql
SELECT	tg.nm_title 
FROM	tb_games	tg
JOIN	tb_category	tc
 ON tg.fk_category = tc.pk_category 
WHERE	tc.nm_category = 'Action';
```
![s7_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/fd5fa160-8c61-4948-9fc4-4c945cd31d84)

I apologize for the confusion earlier. Here are the SQL queries from 8 to 100 in the requested format:

## 8. List all games and their corresponding categories.

```sql
SELECT	tg.nm_title 
FROM	tb_games	tg
JOIN	tb_category	tc
 ON tg.fk_category = tc.pk_category 
WHERE	tc.nm_category = 'Action';
```

![s8_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/28f1a3f3-d021-4ed5-85ff-21b7989f0636)


## 9. Display all information about orders made in the tb_sales table.

```sql
SELECT	*
FROM	tb_sales;
```

![s9_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/fedf87bd-1b41-4a99-b550-70ee2d15eec8)


## 10. List game titles and their total sale prices from the tb_sales table.

```sql
SELECT	tg.nm_title 
		, ts.vl_total 
FROM	tb_sales ts 
JOIN	tb_games tg 
 ON ts.fk_game = tg.pk_game; 
```

![s10_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/ff36d767-483d-4bea-bd20-7b48f05cb635)


## 11. Find games published by "Nintendo".

```sql
SELECT	tg.nm_title 
FROM	tb_games tg
JOIN	tb_publisher tp 
 ON tg.fk_publisher = tp.pk_publisher 
WHERE	tp.nm_publisher = 'Nintendo';
```

![s10_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/06bf0f52-ad2f-4b30-a0bb-9c7d7d9b7f5c)


## 12. List all customers with gender 'F'.

```sql
SELECT	nm_client 
FROM	tb_client
WHERE	nm_gender = 'F';
```
![s12_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/1fb37246-abd5-4fa2-a050-92c317179c42)

**Note**: The script that I used to generate the fake data could not match a male name with male gender, 
so it is confused like that.


## 13. Show the total sales for each game.

```sql
SELECT	tg.nm_title 
		, SUM(ts.vl_total) AS vl_total_sold
FROM	tb_sales ts 
JOIN	tb_games tg 
 ON ts.fk_game = tg.pk_game 
GROUP BY tg.nm_title 
ORDER BY 2 DESC;
```

![s13_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/d66b6c74-45f8-4277-8496-2ac65c2c0629)


## 14. Find all orders made between 2015 and 2020.

```sql
SELECT	*
FROM	tb_sales
WHERE	EXTRACT(YEAR FROM dt_order_date) BETWEEN 2015 AND 2020;
```

![s14_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/42d72fe6-360f-4596-a4bb-d8c8e7a89088)


## 15. List details of CPUs from the 'Intel' brand.

```sql
SELECT	* 
FROM	tb_cpu
WHERE	nm_brand = 'Intel';
```
![s15_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/f3fefe7e-16a2-426c-a88e-b113789aa06f)


## 16. Show all GPU models from the 'Nvidia' brand.

```sql
SELECT	*
FROM	tb_gpu
WHERE	nm_brand = 'Nvidia';
```
![s16_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/5df7b2c0-a3ea-42eb-9f4f-a8becd6d10cf)

**17. Find games published by "Sony Computer Entertainment."**

```sql
SELECT tg.nm_title 
FROM tb_games tg 
JOIN tb_publisher tp 
 ON tg.fk_publisher = tp.pk_publisher 
WHERE tp.nm_publisher = 'Sony Computer Entertainment';
```

![s17_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/160ad609-a24d-4bf0-ad86-d17b01c8d65b)


**18. List the names of games released in the year 2000.**

```sql
SELECT nm_title 
FROM tb_games
WHERE nm_release_year = '2000';
```

![s18_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/ea352a66-dbda-4eef-b3bd-d32d1c17118c)

**19. Show all customers born after 1985.**

```sql
SELECT nm_client  
FROM tb_client
WHERE EXTRACT(YEAR FROM dt_birthdate) > 1985;
```

![s19_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/54c30ff9-732f-411b-a47f-88066293d9b2)


**20. List game titles and their platforms.**

```sql
SELECT tg.nm_title 
		, tp.nm_platform 
FROM tb_games tg 
JOIN tb_platform tp 
 ON tg.fk_platform = tp.pk_platform;
```
![s20_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/c639c6a8-b820-4cc0-a0e2-0eb6aee82ec3)


**21. Find all games with an 'E' rating for everyone.**

```sql
SELECT nm_title 
FROM tb_games tg 
JOIN tb_rating tr 
 ON tg.fk_rating = tr.pk_rating 
WHERE tr.nm_rating = 'E';
```
![s21_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/de144bc1-05ab-455d-8ae3-012d323a6d62)


**22. Show the names of customers and the games they purchased.**

```sql
SELECT tc.nm_client 
		, tc.txt_email 
		, tg.nm_title 
FROM tb_sales ts 
JOIN tb_client tc 
 ON ts.fk_client = tc.pk_client 
JOIN tb_games tg	
 ON ts.fk_game = tg.pk_game
ORDER BY 1;
```

![s22_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/de3d519d-143e-4467-8605-9ffb6bf793a1)



**23. List all sales made in the year 2013.**

```sql
SELECT *
FROM tb_sales
WHERE EXTRACT(YEAR FROM dt_order_date) = 2013;
```

![s23_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/8085a858-5604-4ad7-8d9e-65f0a23701cc)


**24. Show the names of games that do not have a defined rating.**

```sql
SELECT tg.nm_title
		, tr.nm_rating
		, CASE
			WHEN tr.nm_rating IS NULL THEN 'No rating defined'
			ELSE NULL 
		END AS "nm_rating_adjusted"
FROM tb_games tg 
JOIN tb_rating tr 
 ON tg.fk_rating = tr.pk_rating
WHERE tr.pk_rating = 2;
```
![s24_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/f47bd1c0-2781-41ea-86a9-0891c79c3381)


**25. Find the names and emails of customers who bought more than 3 games.**

```sql
SELECT tc.nm_client
		, tc. txt_email
		, a.total_games
FROM (SELECT fk_client 
             , count(*) AS total_games
	  	 FROM tb_sales
	  	 GROUP BY fk_client
      	 HAVING count(*) > 3
      	 ORDER BY 2 DESC) a
JOIN tb_client tc 
 ON a.fk_client = tc.pk_client
ORDER BY 3 DESC;
```

![s25_jr](https://github.com/Shamslux/DataEngineering/assets/79280485/78edfc96-f997-4020-a972-c0d388b74a9f)

