########################################################################################################################################################################################
#**************************************************************************************************************************************************************************************#
# Code created by Shamslux
# October, 27th 2024
# This code belongs to a personal study project to practice a little with dbt, since it is begining to be used at my current company. :)
########################################################################################################################################################################################

########################################################################################################################################################################################
#******************************************************************************* IMPORTS **********************************************************************************************#
########################################################################################################################################################################################
import duckdb
import pandas as pd

########################################################################################################################################################################################
#******************************************************************************* FUNCTIONS ********************************************************************************************#
########################################################################################################################################################################################
def print_with_border(message):
    border = '*' * (len(message) + 4)
    print(border)
    print(f'* {message} *')
    print(border)
    
########################################################################################################################################################################################
#******************************************************************************* CODE *************************************************************************************************#
########################################################################################################################################################################################
try:
    conn = duckdb.connect('dev.duckdb')
    print_with_border('Connected to DuckDB')
except Exception as e:
    print(f"Error connecting to DuckDB: {e}")
    raise


try:
    print_with_border('Creating dimTime on duckdb')
    conn.execute('''
    CREATE TABLE dimTime (
        timeSK INT PRIMARY KEY,
        saleDate DATE,
        year INT,
        month INT,
        day INT,
        day_of_week VARCHAR(10) -- Nome do dia da semana
    );
    ''')
except Exception as e:
    print(f"Error creating dimTime: {e}")
    conn.close()
    raise


time_data = []
for date in pd.date_range(start='2024-04-01', end='2024-10-01', freq='D'):
    time_data.append((int(date.strftime('%Y%m%d')), date, date.year, date.month, date.day, date.strftime('%A')))


try:
    print_with_border('Inserting data into dimTime on duckdb')
    insert_query = '''
    INSERT INTO dimTime (timeSK, saleDate, year, month, day, day_of_week) VALUES
    '''
    insert_values = ', '.join([f'({time[0]}, DATE \'{time[1].date()}\', {time[2]}, {time[3]}, {time[4]}, \'{time[5]}\')' for time in time_data])

    conn.execute(insert_query + insert_values)
except Exception as e:
    print(f"Error inserting data into dimTime: {e}")


print_with_border('Closing connection to duckdb')
conn.close()
