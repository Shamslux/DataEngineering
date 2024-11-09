SELECT *
FROM {{ source('pokemart', 'dimProducts') }}
