SELECT *
FROM {{ source('pokemart', 'dimTime') }}
