# Task 1: Create a function to calculate and return result

def calculate(a, b, op):
    if op == "add":
        return a + b
    elif op == "sub":
        return a - b
    elif op == "mul":
        return a * b
    elif op == "div":
        if b!= 0:
            return a / b
        else:
            return "Can not divide by zero"
    else:
        return "Invalid Operation"

print(calculate(10, 2, "add"))

# Task 2: craete a function to check whether a number is even or odd

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter the num"))
ans = check_even_odd(num)
print("The number is:", ans)

#Task 3: Create a function to find a factorial of the number

def fact(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a number:"))
print("Factorial of the given number is: ", fact(num))

#Task 4: Create a function to find the maximum of number

def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(find_max(10, 25, 15))
    
#Task 5: Create a function to check whether the string is plindrome or not

def palindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

print(palindrome("madam"))
print(palindrome("hello"))

#Task 6: Create a fucntion to calculate the area of circle

def area_circle(r):
    area = 3.14 * r * r
    return area

# function call
print(area_circle(5))