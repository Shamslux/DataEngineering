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
