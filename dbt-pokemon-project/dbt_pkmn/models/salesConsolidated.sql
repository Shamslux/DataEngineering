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
