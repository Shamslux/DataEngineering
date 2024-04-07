# Int to float

price = 10
print(price)

price = float(price)
print(price)

price = 10 / 2
print(price)
print(type(price))

# Float to int

price = 10.30
print(price)

price = int(price)
print(price)
print(type(price))

# Conversion by division

price = 10
print(price)
print(type(price))

print(price / 2)
print(type(price))

""" Just commenting the above case, the instructor said it was a conversion by division; however, I used type() to check and prove that the
type remained integer. With that, I believe he may have based it solely on the appearance of the data. To be, in fact, a
float, there would have to be at least one float (it was a division of two integers). """

print(price // 2)
print(type(price))

# Number to string

price = 10.50
age = 28
print(type(price))
print(type(age))

print(str(price))
print(str(age))
print(type(str(price)))
print(type(str(age)))

text = f"age {age} price {price}"
print(text)
print(type(text))

# String to number

price = "10.50"
age = "28"

print(type(price))
print(type(age))

print(type(float(price)))
print(type(int(age)))

# Conversion Error

price = "python"
print(float(price))