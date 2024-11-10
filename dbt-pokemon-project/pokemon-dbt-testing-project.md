![dbt](https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white)
![duckdb](https://img.shields.io/badge/Duckdb-000000?style=for-the-badge&logo=Duckdb&logoColor=yellow)
![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![chatgpt](https://img.shields.io/badge/ChatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white)

# Installing dbt

## Step-by-Step Guide

1. Install Python on your machine.
2. Install VSCode.
3. Install the VSCode extension called "Power User for dbt Core." See the image below:

![power_user_dbt_vscode](https://github.com/user-attachments/assets/f4a9db01-da5b-40af-b899-afce91772c9b)

4. Create a local folder in your terminal using: `mkdir dbt_local`. 
5. Inside this new directory, use the command: `python -m venv dbt_venv`
6. Now, `dbt_venv` will have some folders, including one called `bin`. Inside `bin`, there are several files, such as `activate`.
7. We need to activate the virtual environment. Based on what was described in step 6, use the command: `source dbt_venv/bin/activate`. This will activate the environment, and you’ll see `(dbt_venv)` appear in the terminal command line.

> **Hint**: There might be an issue during the virtual environment creation. I encountered this myself, and `activate` did not exist. If this happens, carefully repeat the steps, deleting the previous directories using the command: `rm -rf dbt_local`.

## Integration with VSCode Extension Installed

1. Notice that the blue bar in VSCode (at the bottom) will indicate that dbt Core is not installed.
2. Click on this message, and a dialog box will appear at the top. See the image below:

![extension_tutorial_1](https://github.com/user-attachments/assets/13955c45-6063-4add-b821-444f5b4be85a)

3. Select "Setup Extension."
4. Now choose the Python interpreter, as shown in the image below:

![extension_tutorial_2](https://github.com/user-attachments/assets/29535db5-624a-46b7-8015-b2eee3b79130)

5. In the new box that opens, select the path to `dbt_venv` (inside the `bin` folder, choose the `python3` file). After this, the blue bar will look like this:

![extension_tutorial_3](https://github.com/user-attachments/assets/acf20a35-b365-4f25-a421-4df42cc078b2)

# Project Overview

<div align="left">
  <img src="https://github.com/user-attachments/assets/e87be0da-b897-420e-ad9a-65fc24d53bcf" alt="Badge" width="500">
</div>

This is a personal project I created to practice using dbt. In my company, we recently started using the tool, and I picked up some tips from coworkers 
and by watching free courses online. Since I always like to create a basic project to get hands-on with tools I work with, I decided to create a little 
project called PokéMart.

The simulation in this educational project will involve using data from the PokéMart OLAP database to create some basic analytical views, just to test 
the fundamentals of dbt (e.g., using CTEs for some data processing, utilizing documentation features, and exploring lineage capabilities).

# Models

Below are the model codes I created for this project.

![models_path](https://github.com/user-attachments/assets/97a01a6c-7ded-49c4-9f21-774d8b286825)

Here is how I configured the `sources` file:

```yml
version: 2

sources:
  - name: pokemart
    schema: main
    tables:
      - name: dimCustomers
      - name: dimProducts
      - name: dimProdCategories
      - name: dimTime
      - name: factSales
```

## dimCustomersView.sql

```sql
SELECT *
FROM {{ source('pokemart', 'dimCustomers') }}
```

## dimProductsView.sql

```sql
SELECT *
FROM {{ source('pokemart', 'dimProducts') }}
```
## dimProdCategoriesView.sql

```sql
SELECT *
FROM {{ source('pokemart', 'dimProdCategories') }}
```
## dimTimeView.sql

```sql
SELECT *
FROM {{ source('pokemart', 'dimTime') }}
```

## factSalesView.sql

```sql
SELECT *
FROM {{ source('pokemart', 'factSales') }}
```
## salesConsolidated.sql

```sql
WITH sales_consolidated AS (
    SELECT
        fs.saleSK,  
        p.productName,
        pc.categoryName,
        c.customerName,
        t.saleDate,
        fs.quantity,
        fs.totalPrice
    FROM
        {{ ref('factSalesView') }} fs
    JOIN
        {{ ref('dimProductsView') }} p ON fs.productSK = p.productSK  
    JOIN
        {{ ref('dimProdCategoriesView') }} pc ON p.categorySK = pc.categorySK  
    JOIN
        {{ ref('dimCustomersView') }} c ON fs.customerSK = c.customerSK  
    JOIN
        {{ ref('dimTimeView') }} t ON fs.saleDate = t.timeSK  
)

SELECT sc.saleSK    
       , sc.productName
       , sc.categoryName
       , sc.customerName
       , CAST(sc.saleDate AS DATE) AS saleDate
       , sc.quantity
       , sc.totalPrice
FROM sales_consolidated sc
```

## monthlySales.sql

```sql
WITH 
monthly_sales AS (
    SELECT 
        EXTRACT(YEAR FROM saleDate) AS year,
        EXTRACT(MONTH FROM saleDate) AS month,
        SUM(totalPrice) AS monthlyTotal
    FROM 
        {{ ref('salesConsolidated') }}
    GROUP BY 
        year, month
    ORDER BY 
        year, month
)

SELECT 
    year,
    month,
    monthlyTotal,
    SUM(monthlyTotal) OVER (ORDER BY year, month) AS accumulatedSales
FROM 
    monthly_sales
ORDER BY 
    year, month
```

## mostQuantitySold.sql

```sql
SELECT 
    productName,
    SUM(quantity) AS totalQuantity
FROM 
    {{ ref('salesConsolidated') }}
GROUP BY 
    productName
ORDER BY 
    totalQuantity DESC
```

## mostSoldCategories.sql

```sql
SELECT 
    categoryName,
    SUM(totalPrice) AS totalSalesValue,
    SUM(quantity) AS totalQuantitySold
FROM 
    {{ ref('salesConsolidated') }}
GROUP BY 
    categoryName
ORDER BY 
    totalSalesValue DESC
```

## mostSoldProducts.sql

```sql
WITH 
most_sold_products AS(
SELECT 
    productName,
    SUM(totalPrice) AS totalRevenue
FROM 
    {{ ref('salesConsolidated') }}
GROUP BY 
    productName
ORDER BY 
    totalRevenue DESC
)

SELECT * FROM most_sold_products
```

## topBuyers.sql

```sql
SELECT 
    customerName,
    SUM(totalPrice) AS totalSpent,
    COUNT(DISTINCT saleSK) AS totalPurchases
FROM 
    {{ ref('salesConsolidated') }}
GROUP BY 
    customerName
ORDER BY 
    totalSpent DESC
```

# Data Lineage

![lineage](https://github.com/user-attachments/assets/aa253e8b-3210-4c95-a094-efd775860d84)

# Query Results

## dimCustomers

![query_dim_customers](https://github.com/user-attachments/assets/36fa4102-846b-4701-821c-ad440b6eb730)

## dimProducts

![query_dim_products](https://github.com/user-attachments/assets/bbf59225-6e2c-4c1d-be52-b986bdfb677f)

## dimProductCategory

![query_dim_product_cateogry](https://github.com/user-attachments/assets/cb3f2fa8-0a89-4924-9f45-776e27923c9d)

## dimTime

![query_dim_time](https://github.com/user-attachments/assets/340d2e04-2290-4833-b930-716ebe46f915)

## factSales

![query_fact_sales](https://github.com/user-attachments/assets/face9a12-66de-4a08-bbfa-91821fcaab1d)

## monthlySales

![query_monthly_sales](https://github.com/user-attachments/assets/7ef0d60b-d018-4722-8fa9-9814bebeb553)

## mostQuantitySold

![query_most_quantity_sold](https://github.com/user-attachments/assets/b1ae3602-9a03-483b-8f0c-6c5893d8b84d)

## mostSoldCategories

![query_most_sold_categories](https://github.com/user-attachments/assets/46e68921-7158-41dc-8bd0-b3cdd6d7f0cf)

## mostSoldProducts

![query_most_sold_products](https://github.com/user-attachments/assets/575a82e8-28d9-4109-ad70-ac4ea17f9799)

## topBuyers

![query_top_buyers](https://github.com/user-attachments/assets/eb49286a-0e55-4f9e-85ac-781f82bced1c)

# Documenting

![documentation](https://github.com/user-attachments/assets/b3d63f67-09c4-4626-b7f5-ce00f2200ea3)

I documented only one model for educational purposes. The extension I use in VSCode makes documentation creation easier 
(or you can edit it directly in the `sources`). If you have an API key for the AI used, you can use it to automatically 
describe and document the project. Since I don’t use this AI, I documented it manually, but it’s an interesting integration.










