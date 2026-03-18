# Task 1:Loop control statement

# Break

for i in range(1, 10):
    if i == 5:
        break
    print(i)

# Continue 

for i in range(1,10):
    if i == 3:
        continue
    print(i)

# Print number for i to 10 using for loop

for i in range(1,11):
    print(i)

# Task 2: Print even number form 1 to 20

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

for i in range(1,21,2):
    print(i)

# Task 3: Print odd number form 1 to 15

for i in range(1, 16, 2):
    print(i, end=' ')

# Task 4: Print each character of the string

text = "Python"
for char in text:
    print(char)

# Task 5: Print all items in the list

data = ["Miki", "Hely", "Alice"]

for item in data:
    print(item)

# Task 6: Find the sum of the numbers from 1 to 10

total = 0
for i in range(1,11):
    total += i
print(total)

#Task 7: Print multiplication table of 5

num = 5

for i in range(1,11):
    print(num, "x", i, "=", num * i)


#Task 8: Count how many vowels in the Stirng

text = "Hello world"
vowel = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowel:
        count += 1
print(count)

#Task 9: Print numbers in reverse order from 10 to 1

for i in range(10, 1, -1):
    print(i)

# Task 10:Print square of numbers from 1 to 5

for i in range(1, 6):
    print(i ** 2)

#
