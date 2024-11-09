SELECT 
    productName,
    SUM(quantity) AS totalQuantity
FROM 
    {{ ref('salesConsolidated') }}
GROUP BY 
    productName
ORDER BY 
    totalQuantity DESC
