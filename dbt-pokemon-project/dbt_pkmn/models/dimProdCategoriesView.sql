SELECT *
FROM {{ source('pokemart', 'dimProdCategories') }}
