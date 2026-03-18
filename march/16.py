#CREATE A SIMPLE CAL USEING ELIF

# num1 = float(input("Enter the first num"))
# num2 = float(input("Enter the second num"))

# op = input("Enter the opration")

# if op == "+":
#     print("Addition is:", num1 + num2)

# elif op == "-":
#     print("Subtraction is:", num1 - num2)

# elif op == "*":
#     print("Multiplication is:", num1 * num2)

# elif op == "/":
#     if num2 != 0:
#         print("Division is:", num1 / num2)
#     else:
#         print("Cannot divide")

# else:
#     print("Invalid Operation")

# Bank Account

# initial bal: 10000

# choice
# a. Deposit
# b. Withdraw
# c. Check Balance


# deposit = 1000

# balance = balance + 1000
# print(balance)

# main balance = 11000

# withdraw = 5000
# balance = balance - 5000
# print(balance)
# main balance = 6000

balance = 10000
print("Bank Account")
print("a. Deposit")
print("b. Withdraw")
print("c. Check balance")

choice = input("Enter your choice: ")

if choice == "a":
    deposit = int(input("Enter amount to deposit: "))
    balance = balance + deposit
    print("Amount deposited: " )
    print("Main balance: ", balance)

elif choice == "b":
    withdraw = int(input("Enter amount to withdraw: "))
    balance = balance - withdraw
    print("Amount deposited: " )
    print("Main balance: ", balance)

else:
    print("The balance is: ", balance)
    