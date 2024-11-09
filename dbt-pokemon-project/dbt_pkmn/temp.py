import duckdb

# Conectar ao banco de dados DuckDB
conn = duckdb.connect('dev.duckdb')  # Ajuste o caminho conforme necessário

# Consultar todas as tabelas e views do banco de dados
result = conn.execute("""
    SELECT table_name, table_type 
    FROM information_schema.tables;
""").fetchall()

# Imprimir os resultados
print("Tabelas e views no banco de dados:")
if result:
    for row in result:
        print(f"Nome: {row[0]}, Tipo: {row[1]}")
else:
    print("Nenhuma tabela ou view encontrada.")

# Fechar a conexão
conn.close()
