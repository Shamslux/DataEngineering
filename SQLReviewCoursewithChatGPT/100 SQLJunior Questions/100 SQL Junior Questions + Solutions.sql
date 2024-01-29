-- 1. List all games from the tb_games table.

SELECT	nm_title 
FROM	tb_games;

-- 2. Show the names and release years of games from the tb_games table.

SELECT	nm_title
		, nm_release_year 
FROM	tb_games;

-- 3. Find all games released in 2010.

SELECT	nm_title 
FROM	tb_games
WHERE	nm_release_year = '2010';

-- 4. Select all customers from the tb_client table.

SELECT	nm_client
FROM	tb_client;

-- 5. List the names of customers and their countries from the tb_client table.

SELECT	nm_client 
		, nm_country 
FROM	tb_client;

-- 6. Show the names and emails of customers born before 1990.

SELECT	nm_client 
		, txt_email 
FROM	tb_client
WHERE	EXTRACT(YEAR FROM dt_birthdate) < 1990;

-- 7. Find all games in the 'Action' category.

SELECT	tg.nm_title 
FROM	tb_games	tg
JOIN	tb_category	tc
 ON tg.fk_category = tc.pk_category 
WHERE	tc.nm_category = 'Action';

-- 8. List all games and their corresponding categories.

SELECT	tg.nm_title 
		, tc.nm_category 
FROM	tb_games	tg
JOIN	tb_category	tc
 ON tg.fk_category = tc.pk_category;

-- 9. Display all information about orders made in the tb_sales table.

SELECT	*
FROM	tb_sales;

-- 10. List game titles and their total sale prices from the tb_sales table.

SELECT	tg.nm_title 
		, ts.vl_total 
FROM	tb_sales ts 
JOIN	tb_games tg 
 ON ts.fk_game = tg.pk_game; 


-- 11. Find games published by "Nintendo".

SELECT	tg.nm_title 
FROM	tb_games tg
JOIN	tb_publisher tp 
 ON tg.fk_publisher = tp.pk_publisher 
WHERE	tp.nm_publisher = 'Nintendo';

-- 12. List all customers with gender 'F'.

SELECT	nm_client 
FROM	tb_client
WHERE	nm_gender = 'F';

-- 13. Show the total sales for each game.

SELECT	tg.nm_title 
		, SUM(ts.vl_total) AS vl_total_sold
FROM	tb_sales ts 
JOIN	tb_games tg 
 ON ts.fk_game = tg.pk_game 
GROUP BY tg.nm_title 
ORDER BY 2 DESC;

-- 14. Find all orders made between 2015 and 2020.

SELECT	*
FROM	tb_sales
WHERE	EXTRACT(YEAR FROM dt_order_date) BETWEEN 2015 AND 2020;

-- 15. List details of CPUs from the 'Intel' brand.

SELECT	* 
FROM	tb_cpu
WHERE	nm_brand = 'Intel';

-- 16. Show all GPU models from the 'Nvidia' brand.

SELECT	*
FROM	tb_gpu
WHERE	nm_brand = 'Nvidia';

-- 17. Find games released by "Sony Computer Entertainment".

SELECT	tg.nm_title 
FROM	tb_games tg 
JOIN	tb_publisher tp 
 ON tg.fk_publisher = tp.pk_publisher 
WHERE	tp.nm_publisher = 'Sony Computer Entertainment';

-- 18. List the names of games released in the year 2000.

SELECT	nm_title 
FROM	tb_games
WHERE	nm_release_year = '2000';

-- 19. Show all customers born after 1985.

SELECT	nm_client  
FROM	tb_client
WHERE	EXTRACT(YEAR FROM dt_birthdate) > 1985; 

-- 20. List game titles and their platforms.

SELECT	tg.nm_title 
		, tp.nm_platform 
FROM	tb_games tg 
JOIN	tb_platform tp 
 ON tg.fk_platform = tp.pk_platform;

-- 21. Find all games with an 'E' rating for everyone.

SELECT	nm_title 
FROM	tb_games tg 
JOIN	tb_rating tr 
 ON tg.fk_rating = tr.pk_rating 
WHERE tr.nm_rating = 'E';

-- 22. Show the names of customers and the games they purchased.

SELECT	ts.pk_order 
		, ts.dt_order_date 
		, ts.vl_total 
		, tc.nm_client 
		, tg.nm_title 
FROM	tb_sales ts
JOIN	tb_client tc 
 ON ts.fk_client = tc.pk_client 
JOIN	tb_games tg
 ON ts.fk_game = tg.pk_game
ORDER BY 1;

-- 23. List all sales made in the year 2013.

SELECT	*
FROM	tb_sales
WHERE	EXTRACT(YEAR FROM dt_order_date) = 2013;

-- 24. Show the names of games that do not have a defined rating.

SELECT	tg.nm_title
		, tr.nm_rating
		, CASE
			WHEN tr.nm_rating IS NULL THEN 'No rating defined'
			ELSE NULL 
		END	AS "nm_rating_adjusted"
FROM	tb_games tg 
JOIN	tb_rating tr 
 ON tg.fk_rating = tr.pk_rating
WHERE	tr.pk_rating = 2;

-- 25. Find the names and emails of customers who bought more than 3 games.

SELECT	tc.nm_client
		, tc. txt_email
		, a.total_games
FROM	(SELECT	fk_client 
				, count(*) AS total_games
	  	 FROM	tb_sales
	  	 GROUP BY fk_client
      	 HAVING count(*) > 3
      	 ORDER BY 2 DESC) a
JOIN	tb_client tc 
 ON a.fk_client = tc.pk_client
ORDER BY 3 DESC;

-- 26. List all games for the 'PS4' platform.

SELECT	tg.nm_title 
		, tp.nm_platform 
FROM	tb_games tg 
JOIN	tb_platform tp 
 ON tg.fk_platform = tp.pk_platform 
WHERE tp.nm_platform = 'PS4';

-- 27. Show details of orders totaling more than $100.

SELECT	*
FROM	tb_sales ts 
WHERE	vl_total > 100;

-- 28. Find games published before 1995.

SELECT	nm_title 
		, nm_release_year 
FROM	tb_games
WHERE	nm_release_year < '1995'
ORDER BY 2 ASC;

-- 29. List all games in the 'Racing' category.

SELECT	tg.nm_title 
		, tc.nm_category 
FROM	tb_games tg 
JOIN	tb_category tc 
 ON tg.fk_category = tc.pk_category 
WHERE	TC.nm_category = 'Racing'
ORDER BY 1;

-- 30. Show the name and email of each customer along with the name of the game they bought.

SELECT	tc.nm_client 
		, tc.txt_email 
		, tg.nm_title 
FROM	tb_sales ts 
JOIN	tb_client tc 
 ON ts.fk_client = tc.pk_client 
JOIN	tb_games tg 	
 ON ts.fk_game = tg.pk_game
ORDER BY 1;

-- 31. Find the total sales for each game category.

SELECT	tc.nm_category 
		, COUNT(ts.*) AS "total_sales"
FROM	tb_sales ts 
JOIN	tb_games tg 
 ON ts.fk_game = tg.pk_game 
JOIN	tb_category tc 
 ON tg.fk_category = tc.pk_category
GROUP BY tc.nm_category 
ORDER BY 2 DESC;

-- 32. List games purchased by customers from Spain.

SELECT	tc.nm_client 
		, tc.nm_country 
		, tg.nm_title 
FROM	tb_sales ts 
JOIN	tb_client tc 
 ON ts.fk_client = tc.pk_client 
JOIN	tb_games tg 
 ON ts.fk_game = tg.pk_game 
WHERE	tc.nm_country = 'Spain';

-- 33. Show details of CPUs with more than 4 cores.
-- This question was a little bit tricky since there is no column for cores, so I need to adapt using the model names
-- It is not a perfect solution, but the question should not exist for this dataset since we don't have a perfect control
-- of it with a proper column for core number.

CREATE TEMP TABLE patterns (pattern varchar(250));
INSERT INTO patterns VALUES
    ('%i7%'),
    ('%i5%'),
    ('%i9%'),
    ('%Ryzen 5%'),
    ('%Ryzen 7%'),
    ('%Ryzen 9%'),
    ('%Xeon%'),
    ('%Threadripper%'),
    ('%EPYC%');

SELECT	tc.*
FROM	tb_cpu tc
WHERE EXISTS (
    SELECT 1
    FROM patterns p
    WHERE tc.nm_model LIKE p.pattern
);

/* I did some research and I found this more professional and less verbose method. I wanted to try it
 * to settle this into my mind for the next challenge similiar to this one. However, if someone would
 * need a more real junior solution, probably the best way would be using the OR clause with LIKE.
 * SELECT *
FROM tb_cpu
WHERE 
    nm_model LIKE '%i7%'
    OR nm_model LIKE '%i5%'
    OR nm_model LIKE '%i9%'
    OR nm_model LIKE '%Ryzen 5%'
    OR nm_model LIKE '%Ryzen 7%'
    OR nm_model LIKE '%Ryzen 9%'
    OR nm_model LIKE '%Xeon%'
    OR nm_model LIKE '%Threadripper%'
    OR nm_model LIKE '%EPYC%';

 */

-- 34. Find all games with an 'M' rating for mature audiences.

SELECT	tg.nm_title	
		, tr.nm_rating 
FROM	tb_games tg 
JOIN	tb_rating tr 
 ON tg.fk_rating = tr.pk_rating
WHERE	tr.nm_rating = 'M';

-- 35. List sales made by customers from Canada.

SELECT	ts.pk_order 
		, ts.dt_order_date 
		, ts.vl_total 
		, tc.nm_client
		, ts.fk_game 
FROM	tb_sales ts 
JOIN	tb_client tc 
 ON ts.fk_client = tc.pk_client
WHERE tc.nm_country = 'Canada';

-- 36. Show the names of games that were purchased in 2022.

SELECT	tg.nm_title  
FROM	tb_sales ts 
JOIN	tb_games tg 
 ON ts.fk_game = tg.pk_game 
WHERE EXTRACT(YEAR FROM ts.dt_order_date) = 2022;

-- 37. Find customers who haven't made any purchases.

SELECT	pk_client  
FROM	tb_client
WHERE NOT EXISTS (SELECT fk_client
				  FROM	tb_sales);
				 
-- 38. List all games and their respective publishers.				 
				 
-- 39. Show details of GPUs from the 'AMD' brand.

SELECT	*
FROM	tb_gpu
WHERE	nm_brand = 'AMD';

-- 40. Find all games with 'Mario' in the title.

SELECT	nm_title 
FROM	tb_games
WHERE	nm_title LIKE '%Mario%';

-- 41. List games with more than 5 sales.

SELECT	a.nm_title
		, a.qt_sales
FROM	(SELECT	tg.nm_title 
				, count(ts.*) AS qt_sales 
		FROM	tb_sales ts 
		JOIN	tb_games tg 
 		 ON ts.fk_game = tg.pk_game
		GROUP BY tg.nm_title
		HAVING count(ts.*) > 5
		ORDER BY 2 DESC) a
ORDER BY 2 ASC;

-- 42. Show the names of customers who bought games in the 'Adventure' category.

SELECT	tc2.nm_client 
		, tg.nm_title 
		, tc.nm_category 
FROM	tb_sales ts 
JOIN	tb_games tg 
 ON ts.fk_game = tg.pk_game 
JOIN	tb_category tc 
 ON tg.fk_category = tc.pk_category
JOIN	tb_client tc2 
 ON ts.fk_client = tc2.pk_client 
WHERE	tc.nm_category = 'Adventure'

-- 43. Find games with a 'T' rating for teenagers.

SELECT	tg.nm_title 
		, tr.nm_rating 
FROM	tb_games tg 
JOIN	tb_rating tr 
 ON tg.fk_rating = tr.pk_rating 
WHERE tr.nm_rating = 'T';

-- 44. List details of sales made in the last month.

SELECT	*
FROM	tb_sales
WHERE DATE_TRUNC('month', dt_order_date) = (SELECT	MAX(DATE_TRUNC('month', dt_order_date)) 
											FROM	tb_sales);
										
-- 45. Show the names of games published by 'Capcom'.

SELECT	tg.nm_title 
		, tp.nm_publisher 
FROM	tb_games tg 
JOIN	tb_publisher tp 
 ON tg.fk_publisher = tp.pk_publisher 
WHERE tp.nm_publisher = 'Capcom';

-- 46. Find all customers who bought games on the 'X360' platform.

SELECT	ts.pk_order 
		, ts.dt_order_date 
		, ts.vl_total 
		, tc.nm_client 
		, tg.nm_title 
		, tp.nm_platform 
FROM	tb_sales ts 
JOIN	tb_games tg 
 ON ts.fk_game = tg.pk_game 
JOIN	tb_client tc 
 ON ts.fk_client = tc.pk_client 
JOIN	tb_platform tp 
 ON tg.fk_platform = tp.pk_platform 
WHERE tp.nm_platform = 'X360';

-- 47. List games that were purchased more than once.

SELECT	tg.nm_title
		, COUNT(ts.fk_game) AS total_sales
FROM	tb_games tg 
JOIN	tb_sales ts 
 ON tg.pk_game = ts.fk_game
GROUP BY tg.nm_title 
HAVING  COUNT(ts.fk_game) > 2
ORDER BY 2;

-- 48. Show details of customers with the last name 'Smith'.

SELECT	nm_client 
FROM	tb_client
WHERE	nm_client LIKE '%Smith';

-- 49. Find games in the 'Strategy' category released after 2010.

SELECT	tg.nm_title 
		, tc.nm_category 
		, tg.nm_release_year 
FROM	tb_games tg 
JOIN	tb_category tc 
 ON tg.fk_category = tc.pk_category 
WHERE	tc.nm_category = 'Strategy'
AND tg.nm_release_year > '2010'
ORDER BY 3;

-- 50. List all games and their respective sale prices.

SELECT	tg.nm_title 
		, ts.vl_total 
FROM	tb_sales ts 
JOIN	tb_games tg 
 ON ts.fk_game = tg.pk_game;

-- 51. List all customers born in the 1980s decade.

SELECT	nm_client 
		, dt_birthdate 
FROM	tb_client 
WHERE	EXTRACT(YEAR FROM dt_birthdate) BETWEEN 1980 AND 1989
ORDER BY 2;

-- 52. Show the total number of games available in the tb_games table.

SELECT	COUNT(*)
FROM	tb_games;

-- 53. Find the names of all games published by 'Ubisoft'.

SELECT	tg.nm_title 
		, tp.nm_publisher 
FROM	tb_games tg 
JOIN	tb_publisher tp 
 ON tg.fk_publisher = tp.pk_publisher
WHERE tp.nm_publisher = 'Ubisoft';

-- 54. List games available for the 'PlayStation 3' platform.

SELECT	tg.nm_title 
		, tp.nm_platform 
FROM	tb_games tg 
JOIN	tb_platform tp 
 ON tg.fk_platform = tp.pk_platform 
WHERE tp.nm_platform = 'PS3';

-- 55. Show all orders with a total value less than $50.

SELECT	*
FROM	tb_sales
WHERE	vl_total < 50
ORDER BY 3;

-- 56. Find customers with 'John' as part of their name.

SELECT	* 
FROM	tb_client
WHERE nm_client LIKE '%John%';

-- 57. List games in the 'Role-Playing' category.

SELECT	tg.nm_title 
		, tg.nm_release_year 
		, tc.nm_category 
FROM	tb_games tg 
JOIN	tb_category tc 
 ON tg.fk_category = tc.pk_category 
WHERE tc.nm_category = 'Role-Playing';

-- 58. Show all orders made by customers from Brazil.

SELECT	ts.pk_order 
		, ts.dt_order_date 
		, tc.nm_client 
		, tc.nm_country 
		, ts.vl_total 
FROM	tb_sales ts 
JOIN	tb_client tc 
 ON ts.fk_client = tc.pk_client 
WHERE tc.nm_country = 'Brazil';

-- 59. Find games rated as 'AO' (Adults Only).

SELECT	tg.nm_title 
		, tr.nm_rating 
FROM	tb_games tg 
JOIN	tb_rating tr 
 ON tg.fk_rating = tr.pk_rating 
WHERE tr.nm_rating = 'AO';

-- 60. List all customers and their respective countries.

SELECT	nm_client 
		, nm_country 
FROM	tb_client;

-- 61. Show details of customers whose emails end with '.com'.

SELECT	*
FROM tb_client
WHERE txt_email LIKE '%.com';

-- 62. Find all games with the word 'Battle' in the title.

SELECT	*
FROM	tb_games
WHERE	nm_title LIKE '%Battle%';

-- 63. List games and their respective rating classifications.

SELECT	tg.nm_title 
		, tr.nm_rating 
FROM	tb_games tg 
JOIN	tb_rating tr 
 ON tg.fk_rating = tr.pk_rating;

-- 64. Show details of all GPUs in the tb_gpu table.

SELECT	*
FROM tb_gpu;

-- 65. Find customers who placed orders totaling exactly $100.

SELECT	ts.pk_order 
		, ts.dt_order_date 
		, tc.nm_client 
		, ts.vl_total 
FROM	tb_sales ts 
JOIN	tb_client tc 
 ON ts.fk_client = tc.pk_client 
WHERE ts.vl_total = 100;

-- 66. List games that were purchased in the year 2018.

SELECT	ts.pk_order 
		, ts.dt_order_date 
		, tg.nm_title 
FROM	tb_sales ts 
JOIN	tb_games tg 
 ON ts.fk_game = tg.pk_game 
WHERE EXTRACT(YEAR FROM ts.dt_order_date) = 2018;

-- 67. Show details of games with more than 4 words in the title.

SELECT	* 
FROM	tb_games
WHERE CHAR_LENGTH(nm_title) > 4;

-- 68. Find all customers with the last name 'Silva'.

SELECT	* 
FROM	tb_client
WHERE nm_client LIKE '%Silva';

-- 69. List games that were published after the year 2000.

SELECT	*
FROM	tb_games
WHERE nm_release_year > '2000'
ORDER BY 3;

-- 70. Show all orders placed in the first half of 2019.

SELECT	*
FROM	tb_sales
WHERE	EXTRACT(MONTH FROM dt_order_date) IN (1, 2, 3, 4, 5, 6);

-- 71. Find games available for the 'Xbox 360' platform.

SELECT	tg.nm_title 
		, tp.nm_platform 
FROM	tb_games tg 
JOIN	tb_platform tp 
 ON tg.fk_platform = tp.pk_platform 
WHERE tp.nm_platform = 'X360';

-- 72. List all publishers with more than 10 games in the tb_games table.

SELECT	tp.nm_publisher 
		, COUNT(tg.*) AS total_games
FROM	tb_games tg 
JOIN	tb_publisher tp 
 ON tg.fk_publisher = tp.pk_publisher 
GROUP BY tp.nm_publisher 
HAVING COUNT(tg.*) > 10
ORDER BY 2;

-- 73. Show details of customers who bought games in the 'Shooter' category.

SELECT	tc2.nm_client 
		, tc2.nm_gender 
		, tc2.dt_birthdate 
		, tc2.nm_username 
		, tc2.nm_country 
		, tc3.nm_model 
		, tg2.nm_model 
		, tg.nm_title 
		, tc.nm_category 
FROM	tb_sales ts 
JOIN	tb_games tg 
 ON ts.fk_game = tg.pk_game 
JOIN	tb_category tc 
 ON tg.fk_category = tc.pk_category 
JOIN	tb_client tc2 
 ON ts.fk_client = tc2.pk_client 
JOIN 	tb_cpu tc3 
 ON tc2.fk_cpu = tc3.pk_cpu 
JOIN 	tb_gpu tg2 
 ON tc2.fk_gpu = tg2.pk_gpu 
WHERE tc.nm_category = 'Shooter';

-- 74. Find all games with a title that starts with 'Super'.

SELECT	* 
FROM	tb_games
WHERE nm_title LIKE 'Super%';

-- 75. List games and their respective sale prices ordered from most expensive to cheapest.

SELECT	tg.nm_title 
		, ts.vl_total 
FROM	tb_sales ts 
JOIN	tb_games tg 
 ON ts.fk_game = tg.pk_game 
ORDER BY 2 DESC;

-- 76. Show details of CPUs that belong to the 'AMD' brand.

SELECT	*
FROM	tb_gpu
WHERE nm_brand = 'AMD';

-- 77. Find all customers who haven't purchased any games.

SELECT	* 
FROM	tb_client tc
LEFT JOIN tb_sales ts 
 ON tc.pk_client = ts.fk_client 
WHERE ts.fk_client IS NULL;

-- 78. List games that were purchased more than 10 times.

SELECT	tg.nm_title	
		, COUNT(ts.*) AS total_sales
FROM	tb_sales ts 
JOIN	tb_games tg 
 ON ts.fk_game = tg.pk_game 
GROUP BY tg.nm_title 
HAVING COUNT(ts.*) > 10
ORDER BY 2;

-- 79. Show details of orders placed in the last year.

SELECT	*
FROM	tb_sales 
WHERE	DATE_TRUNC('year', dt_order_date) = (SELECT DATE_TRUNC('year', MAX( dt_order_date)) FROM tb_sales);

-- 80. Find games in the 'Sports' category released before 2005.

SELECT	tg.nm_title 
		, tc.nm_category 
		, tg.nm_release_year 
FROM	tb_games tg 
JOIN	tb_category tc 
 ON tg.fk_category = tc.pk_category 
WHERE tg.nm_release_year = '2005'
AND tc.nm_category = 'Sports';

-- 81. List all games available for 'PC'.

SELECT	tg.nm_title 
		, tp.nm_platform 
FROM	tb_games tg 
JOIN	tb_platform tp 
 ON tg.fk_platform = tp.pk_platform 
WHERE tp.nm_platform = 'PC';

-- 82. Show details of orders with a total value between $50 and $100.

SELECT	*
FROM	tb_sales ts 
WHERE vl_total BETWEEN 50 AND 100;

-- 83. Find customers who purchased games on their birthday.

SELECT	tc.nm_client 
		, tc.dt_birthdate 
		, ts.dt_order_date 
FROM	tb_sales ts 
JOIN	tb_client tc 
 ON ts.fk_client = tc.pk_client 
WHERE CONCAT(DATE_PART('MONTH', ts.dt_order_date),  DATE_PART('DAY', ts.dt_order_date)) = 
CONCAT(DATE_PART('MONTH', tc.dt_birthdate),  DATE_PART('DAY', tc.dt_birthdate));

-- 84. List games and their respective platforms and publishers.

SELECT	tg.nm_title 
		, tp.nm_platform 
		, tp2.nm_publisher 
FROM	tb_games tg 
JOIN	tb_platform tp 
 ON tg.fk_platform = tp.pk_platform 
JOIN	tb_publisher tp2 
 ON tg.fk_publisher = tp2.pk_publisher;

-- 85. Show details of customers who purchased the game 'Mario Kart 8'.

SELECT	ts.pk_order 
		, ts.dt_order_date 
		, ts.vl_total 
		, tc.nm_client 
		, tc.nm_gender 
		, tc.nm_country 
		, tg.nm_title 
FROM	tb_sales ts 
JOIN	tb_games tg 
 ON ts.fk_game = tg.pk_game 
JOIN	tb_client tc 
 ON ts.fk_client = tc.pk_client 
WHERE tg.nm_title LIKE 'Mario Kart 8%';

-- 86. Find all games with a rating of 'E10+'.

SELECT	tg.nm_title 
		, tr.nm_rating 
FROM	tb_games tg 
JOIN	tb_rating tr 
 ON tg.fk_rating = tr.pk_rating 
WHERE tr.nm_rating = 'E10+';

-- 87. List games that were purchased more than once by the same customer.

SELECT	tc.nm_client
		, tg.nm_title
		, COUNT(ts.fk_client) AS qty_purchases 
FROM	tb_sales ts 
JOIN	tb_games tg 
 ON ts.fk_game = tg.pk_game 
JOIN	tb_client tc 
 ON ts.fk_client = tc.pk_client 
GROUP BY tc.nm_client 
	     , tg.nm_title 
HAVING COUNT(ts.fk_client) > 1;

-- 88. Show all customers who placed orders in 2020.

SELECT	ts.pk_order 
		, ts.dt_order_date 
		, tc.nm_client 
FROM	tb_sales ts 
JOIN	tb_client tc 
 ON ts.fk_client = tc.pk_client 
WHERE DATE_PART('YEAR', ts.dt_order_date) = 2020;

-- 89. Find games with 'War' in the title.

SELECT	nm_title  
FROM	tb_games
WHERE nm_title ILIKE '% War %';

-- 90. List all games for the 'SNES' platform.

SELECT	tg.nm_title 
		, tp.nm_platform 
FROM	tb_games tg 
JOIN	tb_platform tp 
 ON tg.fk_platform = tp.pk_platform
WHERE tp.nm_platform = 'SNES';

-- 91. Show details of GPUs with more than 4GB of memory.
-- Again I had to adapt this technique to solve a similar question like previously.
CREATE TEMP TABLE patterns (pattern varchar(250));
INSERT INTO patterns VALUES
    ('%6GB%'),
    ('%8GB%'),
    ('%12GB%'),
    ('%24GB%'),
    ('%32GB%');
   
SELECT tg.* 
FROM	tb_gpu tg
WHERE EXISTS (
	SELECT	1
	FROM	patterns p
	WHERE tg.nm_model LIKE p.pattern);

DROP TABLE patterns;

-- 92. Find games in the 'Adventure' category released in 2014.

SELECT	tg.nm_title 
		, tc.nm_category 
		, tg.nm_release_year 
FROM	tb_games tg 
JOIN	tb_category tc 
 ON tg.fk_category = tc.pk_category 
WHERE tc.nm_category = 'Adventure'
AND tg.nm_release_year = '2014';

-- 93. List customers whose email contains 'gmail'.

SELECT	nm_client 
		, txt_email 
FROM	tb_client
WHERE txt_email LIKE '%gmail%';

-- 94. Find games for the 'PlayStation 4' platform released in 2016.

SELECT	tg.nm_title 
		, tp.nm_platform  
FROM	tb_games tg
JOIN	tb_platform tp 
 ON tg.fk_platform = tp.pk_platform 
WHERE tp.nm_platform = 'PS4'
AND tg.nm_release_year = '2016';

-- 95. Show the names of all games with fewer than 15 characters.

SELECT	nm_title 
FROM	tb_games
WHERE CHAR_LENGTH(nm_title) = 15;

-- 96. Find all games in the 'Misc' category and their respective release dates.

SELECT	tg.nm_title 
		, tc.nm_category 
		, tg.nm_release_year 
FROM	tb_games tg 
JOIN	tb_category tc 
 ON tg.fk_category = tc.pk_category 
WHERE tc.nm_category = 'Misc';

-- 97. Show games and their respective release years ordered from most recent to oldest.

SELECT	nm_title 
		, nm_release_year 
FROM	tb_games
WHERE nm_release_year <> 'N/A'
ORDER BY 2 DESC;

-- 98. Show the games published in the year 2005.

SELECT	nm_title 
		, nm_release_year 
FROM	tb_games
WHERE nm_release_year = '2005';

-- 99. Find all the 'Action' category games available on the 'PS2' platform.

SELECT	tg.nm_title 
		, tc.nm_category 
		, tp.nm_platform 
FROM	tb_games tg 
JOIN	tb_platform tp 
 ON tg.fk_platform = tp.pk_platform 
JOIN	tb_category tc 
 ON tg.fk_category = tc.pk_category 
WHERE tp.nm_platform = 'PS2'
AND tc.nm_category = 'Action';

-- 100. List the details of orders made by customers from the United Kingdom

SELECT	ts.pk_order 
		, ts.dt_order_date 
		, tc.nm_client 
		, tc.nm_country 
		, ts.fk_game 
		, ts.vl_total 
FROM	tb_sales ts 
JOIN	tb_client tc 
 ON ts.fk_client = tc.pk_client 
WHERE tc.nm_country = 'United Kingdom';











