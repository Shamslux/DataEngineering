import duckdb

# Conectar ao banco de dados DuckDB
conn = duckdb.connect('dev.duckdb')

# Função para exibir dados de uma tabela
def display_table_data(table_name):
    print(f'\nData from {table_name}:')
    results = conn.execute(f'SELECT * FROM {table_name};').fetchall()
    for row in results:
        print(row)

# Exibir dados de dimCustomers
display_table_data('dimCustomers')

# Exibir dados de dimProducts
display_table_data('dimProducts')

# Exibir dados de dimProdCategories
display_table_data('dimProdCategories')

# Exibir os dados da dimTime
display_table_data('dimTime')

# Exibir os dados da factSales
display_table_data('factSales')

# Fechar a conexão
conn.close()

