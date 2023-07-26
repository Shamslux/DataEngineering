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