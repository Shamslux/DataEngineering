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