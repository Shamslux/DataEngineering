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
import time
########################################################################################################################################################################################
#******************************************************************************* FUNCTIONS ********************************************************************************************#
########################################################################################################################################################################################

def print_with_border(message):
    border = '*' * (len(message) + 4)
    print(border)
    print(f'* {message} *')
    print(border)

def connect_to_duckdb(retries=3, delay=2):
    for attempt in range(retries):
        try:
            conn = duckdb.connect('dev.duckdb')
            print_with_border('Connected to DuckDB')
            return conn
        except Exception as e:
            print(f"Connection failed: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
    raise Exception("Failed to connect to DuckDB after multiple attempts.")

########################################################################################################################################################################################
#******************************************************************************* CODE *************************************************************************************************#
########################################################################################################################################################################################
print_with_border('Connecting to duckdb')
conn = connect_to_duckdb()

#dimCustomers
try:
    print_with_border('Creating dimCustomers on duckdb')
    conn.execute('''
    CREATE TABLE dimCustomers (
        customerSK INT PRIMARY KEY,
        customerName VARCHAR(50),
        customerType VARCHAR(20)
    );
    ''')
except Exception as e:
    print_with_border(f"Error creating dimCustomers: {e}")

# Inserting data into dimCustomers
try:
    print_with_border('Inserting data into dimCustomers on duckdb')
    conn.execute('''
    INSERT INTO dimCustomers (customerSK, customerName, customerType) VALUES
    (1, 'Red', 'Trainer'),
    (2, 'Green', 'Trainer'),
    (3, 'Brock', 'Gym Leader'),
    (4, 'Misty', 'Gym Leader'),
    (5, 'Gary', 'Trainer'),
    (6, 'Tracey', 'Trainer'),
    (7, 'Professor Oak', 'Professor'),
    (8, 'Team Rocket Jessie', 'Villain'),
    (9, 'Team Rocket James', 'Villain'),
    (10, 'Ash Ketchum', 'Trainer'),
    (11, 'May', 'Trainer'),
    (12, 'Dawn', 'Trainer'),
    (13, 'Cynthia', 'Champion'),
    (14, 'Professor Elm', 'Professor'),
    (15, 'Hilda', 'Trainer'),
    (16, 'N', 'Trainer'),
    (17, 'Iris', 'Trainer'),
    (18, 'Serena', 'Trainer'),
    (19, 'Clemont', 'Gym Leader'),
    (20, 'Korrina', 'Gym Leader'),
    (21, 'Roxie', 'Gym Leader'),
    (22, 'Hilda', 'Trainer'),
    (23, 'Lysandre', 'Villain'),
    (24, 'Wallace', 'Champion'),
    (25, 'Diantha', 'Champion'),
    (26, 'Professor Sycamore', 'Professor'),
    (27, 'Mallow', 'Trainer'),
    (28, 'Lillie', 'Trainer'),
    (29, 'Kukui', 'Professor'),
    (30, 'Gladion', 'Trainer'),
    (31, 'Sabrina', 'Gym Leader'),
    (32, 'Giovanni', 'Villain'),
    (33, 'Flannery', 'Gym Leader'),
    (34, 'Erika', 'Gym Leader'),
    (35, 'Whitney', 'Gym Leader'),
    (36, 'Clair', 'Gym Leader'),
    (37, 'Roxanne', 'Gym Leader'),
    (38, 'Maylene', 'Gym Leader'),
    (39, 'Candice', 'Gym Leader'),
    (40, 'Skyla', 'Gym Leader'),
    (41, 'Blaine', 'Gym Leader'),
    (42, 'Janine', 'Gym Leader'),
    (43, 'Falkner', 'Gym Leader'),
    (44, 'Burgundy', 'Trainer'),
    (45, 'Cynthia', 'Champion'),
    (46, 'Sierra', 'Trainer'),
    (47, 'Hilda', 'Trainer'),
    (48, 'Alain', 'Trainer'),
    (49, 'Charon', 'Villain'),
    (50, 'Lyra', 'Trainer');
    ''')
except Exception as e:
    print_with_border(f"Error inserting data into dimCustomers: {e}")


# dimProducts
try:
    print_with_border('Creating dimProducts on duckdb')
    conn.execute('''
    CREATE TABLE dimProducts (
        productSK INT PRIMARY KEY,
        productNK VARCHAR(50) UNIQUE,
        productName VARCHAR(50),
        categorySK INT,
        price DECIMAL(10, 2)
    );
    ''')
except Exception as e:
    print_with_border(f"Error creating dimProducts: {e}")

# Inserting data into dimProducts
try:
    print_with_border('Inserting data into dimProducts on duckdb')
    conn.execute('''
    INSERT INTO dimProducts (productSK, productNK, productName, categorySK, price) VALUES
    (1, 'POTION', 'Potion', 1, 200.00),
    (2, 'SUPER_POTION', 'Super Potion', 1, 600.00),
    (3, 'POKEBALL', 'PokéBall', 2, 300.00),
    (4, 'GREAT_BALL', 'Great Ball', 2, 600.00),
    (5, 'ULTRA_BALL', 'Ultra Ball', 2, 1200.00),
    (6, 'REVIVE', 'Revive', 3, 1500.00),
    (7, 'FULL_RESTORE', 'Full Restore', 1, 3000.00),
    (8, 'MAX_POTION', 'Max Potion', 1, 2500.00),
    (9, 'ANTIDOTE', 'Antidote', 1, 100.00),
    (10, 'BURN_HEAL', 'Burn Heal', 1, 200.00),
    (11, 'ICE_HEAL', 'Ice Heal', 1, 200.00),
    (12, 'PARALYZE_HEAL', 'Paralyze Heal', 1, 200.00),
    (13, 'AWAKENING', 'Awakening', 1, 300.00),
    (14, 'REPEL', 'Repel', 2, 350.00),
    (15, 'SUPER_REPEL', 'Super Repel', 2, 700.00),
    (16, 'MAX_REPEL', 'Max Repel', 2, 1200.00),
    (17, 'HEALTHY_TREAT', 'Healthy Treat', 3, 1500.00),
    (18, 'LURE', 'Lure', 2, 200.00),
    (19, 'NUGGET', 'Nugget', 4, 5000.00),
    (20, 'MYSTIC_WATER', 'Mystic Water', 5, 1500.00);
    ''')
except Exception as e:
    print_with_border(f"Error inserting data into dimProducts: {e}")


# dimProdCategories
try:
    print_with_border('Creating dimProdCategories on duckdb')
    conn.execute('''
    CREATE TABLE dimProdCategories (
        categorySK INT PRIMARY KEY,
        categoryName VARCHAR(50)
    );
    ''')
except Exception as e:
    print(f"Error creating dimProdCategories: {e}")


# Inserting data into dimProdCategories
try:
    print_with_border('Inserting data into dimProdCategories on duckdb')
    conn.execute('''
    INSERT INTO dimProdCategories (categorySK, categoryName) VALUES
    (1, 'Medicine'),
    (2, 'Poké Balls'),
    (3, 'Revival Items'),
    (4, 'Accessories'),
    (5, 'Battle Items');
    ''')
except Exception as e:
    print_with_border(f"Error inserting data into dimProdCategories: {e}")

print_with_border('Closing connection to duckdb')
# Closing connection
conn.close()
