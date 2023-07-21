import pandas as pd
from faker import Faker
import random

# Create a Faker instance
fake = Faker('pt_BR')

# Generate fake data
def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        full_name = fake.name()
        birthdate = fake.date_of_birth(minimum_age=18, maximum_age=90)
        gender = random.choice(['M', 'F'])
        cep = fake.postcode()
        data.append([full_name, birthdate, gender, cep])
    return data

# Generate 20 fake records
num_records = 20
fake_data = generate_fake_data(num_records)

# Create a DataFrame from the fake data
df = pd.DataFrame(fake_data, columns=['Full Name', 'Birthdate', 'Gender', 'CEP'])

# Save the DataFrame as an Excel file in the specified path
save_path = r"C:\Users\jpmul\Downloads\fake_data.xlsx"
df.to_excel(save_path, index=False)
print(f"Fake data saved as '{save_path}'.")
