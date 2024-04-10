# If
balance = 2000.0
withdraw = float(input("Inform the withdraw value: "))

if balance >= withdraw:
    print("Success!")

if balance < withdraw:
    print("Insufficient funds!")

# If else

balance = 2000.0
withdraw = float(input("Inform the withdraw value: "))

if balance >= withdraw:
    print("Success!")

else:
    print("Insufficient funds!")

# If elif else

option = int(input("Inform an option: [1] Withdraw \n[2] Statement: "))

if option == 1:
    value = float(input("Inform the withdraw value: "))

elif option == 2:
    print("Showing bank statement... ")
else:
    sys.exit("Unavaliable option! Closing...")

# Nested if elif else

normal_account = True
university_student_account = False

balance = 2000
withdraw = 500
overdraft = 450

if normal_account:
    if balance >= withdraw:
        print("Success!")
    elif balance <= (balance + overdraft):
        print("Success with overdraft!")
elif university_student_account:
    if balance >= withdraw:
        print("Success!")
    else:
        print("Insufficient Funds!")

# Ternary If

status = "Success!" if balance >= withdraw else "Failed!"

print(f"{status} when withdrawing the value!")