# For

text = input("Write a piece of text: ")
VOWELS = "AEIOU"

for letter in text:
    if letter.upper() in VOWELS:
        print(letter, end="")

print() # Just adds a line break

# For else

text = input("Write a piece of text: ")
VOWELS = "AEIOU"

for letter in text:
    if letter.upper() in VOWELS:
        print(letter, end="")
else:
    print() # Just adds a line break

# Range()

print(list(range(0,10)))

# For range()

for number in range(0, 11):
    print(number, end=" ")

# 5 times table

for number in range(0, 51, 5):
    print(number, end=" ")

# While

option = -1

while option != 0:
    option = int(input("[1] Withdraw \n[2] Bank Statement\n[0] Exit \n: "))

    if option == 1:
        print("Withdrawing...")
    
    elif option == 2:
        print("Showing bank statement"...)

# Using break

while True:
    number = int(input("Guess the number! It is between 0 and 100! While you don't guess it, the program keep running!: "))

    if number == 10:
        break

    print(number)

# Using continue
# This will only show the odd numbers

for number in range(100):

    if number % 2 == 0:
        continue

    print(number, end=" ")
