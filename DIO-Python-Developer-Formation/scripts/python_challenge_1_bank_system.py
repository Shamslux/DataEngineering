menu = """
============ Welcome to Cobra Bank ==============
=================================================
############ Select one of the options below ####

[d] Deposit
[w] Withdrawal
[s] Bank statement
[q] Quit

=> """

balance = 0
limit = 500
bank_statement = ""
number_of_withdrawals = 0
WITHDRAWAL_LIMIT = 3

while True:

    option = input(menu)

    if option == "d":
        print("Deposit option selected")
        print("==== Processing ===")
        deposit = input("Insert how much do you want to deposit? -> R$ ")
        print("==== Processing ===")
        if int(deposit) > 0:
            print(f"{deposit} received!")
            #balance = balance + int(deposit)
            balance += int(deposit)
        elif int(deposit) <= 0:
            print(f"{deposit} not accepted, try a value above zero and not negative") 
        else:
            print("We found an error while processing, please, try again!")
    
    elif option == "w":
        print("Withdrawal option selected")
        print("==== Processing ===")
        if balance <= 0:
            print(f"Your balance is R$ {balance:.2f}, it is not possible to proceed with the withdrawal.")
        elif number_of_withdrawals >= WITHDRAWAL_LIMIT:
            print("Your withdrawal limit has been reached for today!")
        else:
            withdrawal = int(input(f"Enter how much you want to withdraw. You still have {WITHDRAWAL_LIMIT - number_of_withdrawals} withdrawals possible today -> R$ "))
            print("==== Processing ===")
            if withdrawal > limit:
                print(f"The amount exceeds the limit of {limit} per withdrawal.")
            elif withdrawal > balance:
                print("There are not enough funds to make this withdrawal.")
            else:
                balance -= withdrawal
                number_of_withdrawals += 1
                print("==== Processing ===")
                print(f"Withdrawal successful! Your new balance is R$ {balance:.2f}")

    
    elif option == "s":
        print("Bank Statement option selected")
        print("==== Processing ===")
        print(f"Total money in your account R$ {balance:.2f}")
    
    elif option == "q":
        break

    else:
        print("Invalid option, please, select again the desired option.")

