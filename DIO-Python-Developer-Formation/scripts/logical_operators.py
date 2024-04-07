# Logical operators
balance = 1000
withdraw = 200
limit = 100
special_account = True

print(balance >= withdraw)
print(balance <= limit)

# and operator (both arguments must be true to be true)

print(balance >= withdraw and balance <= limit)

# or operator (only one argument must be true to be true)

print(balance >= withdraw or balance <= limit)

# not operator

not 1000 > 1500

# Using parentesis to organize logical operators

print(balance >= withdraw and balance <= limit or special_account and balance >= withdraw)
print((balance >= withdraw and balance <= limit) or (special_account and balance >= withdraw))

# Avoid long logical operations, you can just organize as below
normal_account_with_enough_balance = balance >= withdraw and balance <= limit
special_account_with_enough_balance = special_account and balance >= withdraw

exp_3 = normal_account_with_enough_balance or special_account_with_enough_balance
print(exp_3)