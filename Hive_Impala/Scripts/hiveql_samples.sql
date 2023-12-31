-- HiveQL Queries

-- Basic Select

select	idveiculo
		, dataaquisicao
		, ano
		, modelo
		, placa
        , status
        , diaria
from    veiculos;

-- Basic Select using Disctinct

select distinct modelo 
from    veiculos;

-- Using filter with Where clause

select  *
from    veiculos
where   status <> "Disponivel";

-- Using Where with Two Conditions

select  *
from    veiculos
where   status = "Disponivel"
and     diaria >= 1600;

-- Using Order By

select  *
from    locacao
order by datalocacao;

-- Using Limit

select  *
from    veiculos
limit 5;

-- Using Order By and Limit

select  *
from    veiculos
order by dataaquisicao
limit 5;

-- Using Max() function

select  max(total)
from    locacao;

-- Using Sum() function

select  sum(total)
from    locacao;

-- Using Count() function

select  count(*)
from    locacao;

-- Using Avg() function

select  avg(total)
from    locacao;

-- Using LIKE

select	*
from	veiculos
where	modelo like 'BMW%';

select	*
from	veiculos
where	modelo like '%T8%';

-- Using IN

select	*
from	despachantes
where	filial in ('Santa Maria', 'Novo Hamburgo');

select	*
from	despachantes
where	filial not in ('Santa Maria', 'Novo Hamburgo');

-- Using Between

select	*
from	veiculos
where	diaria between 1400 and 1800;

-- Using basic Join

select	loc.idlocacao
		, loc.idcliente
		, loc.iddespachante
		, vec.modelo
		, loc.datalocacao
		, loc.dataentrega
		, loc.total
from	locacao loc
join	veiculos vec
on loc.idveiculo = vec.idveiculo;

-- Using sum()

select	vec.modelo
		, sum(loc.total)
from	locacao loc
join	veiculos vec
on loc.idveiculo = vec.idveiculo
group by vec.modelo;

-- Using sum() again with dispatchers' table

select	vec.modelo
		, desp.nome
		, sum(loc.total)
from	locacao loc
join	veiculos vec
on loc.idveiculo = vec.idveiculo
join despachantes desp
on loc.iddespachante = desp.iddespachante
group by vec.modelo, desp.nome;

-- Using having with sum()

select	vec.modelo
		, desp.nome
		, sum(loc.total)
from	locacao loc
join	veiculos vec
on loc.idveiculo = vec.idveiculo
join despachantes desp
on loc.iddespachante = desp.iddespachante
group by vec.modelo, desp.nome
having sum(loc.total) > 10000;

-- Using functions

select	vec.modelo
		, desp.nome
		, sum(loc.total)
from	locacao loc
join	veiculos vec
on loc.idveiculo = vec.idveiculo
join despachantes desp
on loc.iddespachante = desp.iddespachante
where month(loc.datalocacao) = 2
and year(loc.datalocacao) = 2019
group by vec.modelo, desp.nome
