#operators is general are used to perform operation on variables.
#Arithmatic
a = 20
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)

#Relational
print(a < b)
print(a == b)

str1 = "jyoti"
str2 = "JYOTI"

print(str1 == str2)

#AND => condition => true => true
a = 4
b = 5
c = 6
print(b>a and c>b)

#OR => any condition is true , the output will be true.

print(b>a or a>c)

#true

#Assignment
a += 20 #== a = a + 20
b -= 2 # == b = b - 2
print(a)
 #24

print(b)
 #3

#input() : need user side input
# num1 = input("Enter your num1")
# num2 = input("Enter your num2")
# print(int(num1) + int(num2))

#if else condition:
# => based on the condition if we have multiples statement , then we #can use if else condition
#syntax:
# if condition:
#     true statement
# else:
#     false statement

# username = "Musaddika"
# password = 12345

# if username == "Musaddika" and password == 12344:
#     print("Login successfully")
# else:
#     print("Login unsuccessfull") 

# Uname = input("Enter your username")
# Pass = int(input("Enter your password"))

# if Uname == "Bagban" and Pass == 123:
#     print("Logon successfull")
# else:
#     print("Login unsuccessfull")

#Task 1:

# no = int(input("Enter the number"))

# if no > 0:
#     print("Number is positive")
# elif no < 0:
#     print("Number is negative")
# else:
#     print("number is zero")

# #Task 2:

# num = int(input("Enter the number"))

# if num %2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd")

#Task 3:

# age = int(input("Enter the age"))

# if age >= 18:
#     print("Person is elligible")
# else:
#     print("Person is not elligible")

#Task 4:

# num1 = int(input("Enter the num1"))
# num2 = int(input("Enter the num2"))
# num3 = int(input("Enter the num3"))

# if num1 > num2 and num1 > num3:
#     print(num1 , "is greatest")
# elif num2 > num1 and num2 > num3:
#     print(num2, "is greatest")
# else:
#     print(num3, "is greatest")
    
#Task 5:

# num = int(input("Enter the num"))

# if num %5 == 0:
#     print(num, " is divisible by 5.")
# else:
#     print(num, " is not divisible by 5.")

#Task 6:

# marks = int(input("Enter the marks"))

# if marks >= 90 and marks <= 100:
#     print("Grade A+")
# elif marks >= 80 and marks < 90:
#     print ("Grade A")
# elif marks >=70 and marks < 80:
#     print("grade B")
# else:
#     print("Grade C")

# year = int(input("Enter the year"))

# if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leep year")
# else:
#     print("Not a leap year")


num = int(input("Enter the number"))

if num %3 == 0 and num %5 == 0:
    print(num, " is divisible by both 3 and 5")
else:
    print(num, " is not divisible by both 3 and 5")