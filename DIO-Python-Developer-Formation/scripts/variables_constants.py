# Using variables

age = 23
name = 'William'
print(f'My name is {name} and I am {age} year(s) old.')

age, name = (23, 'William')
print(f'My name is {name} and I am {age} year(s) old.')

# Changing the values of variables

age = 23
name = 'William'
print(f'My name is {name} and I am {age} year(s) old.')
print(age, name)

age = 27
name = 'Giovanna'
print(f'My name is {name} and I am {age} year(s) old.')
print(age, name)

# Properly creating a constant in Python (convention)

ABS_PATH = '/home/william/Documents/python_course'
DEBUG = True
STATES = [
    'SP',
    'RJ',
    'MG',
]
AMOUNT = 30.2

# Best practices

# The naming convention should be *nake case
new_value = 2

# Choose meaningful names
student_name = 'Peter'
student_last_name = 'Parker'
student_grade = 9.8

#Constants should be all uppercase

ABS_PATH = '/home/william/Documents/python_course'

