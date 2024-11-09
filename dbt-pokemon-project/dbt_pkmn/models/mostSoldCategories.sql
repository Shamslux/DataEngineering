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
