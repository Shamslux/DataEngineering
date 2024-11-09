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