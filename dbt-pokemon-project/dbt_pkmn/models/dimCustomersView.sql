SELECT *
FROM {{ source('pokemart', 'dimCustomers') }}
