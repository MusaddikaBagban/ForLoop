text = " hello World "

# 1. upper() - 
# Converts all characters to uppercase

print(text.upper())  # " HELLO WORLD "

# 2. lower() - Converts all characters to lowercase

print(text.lower())  # " hello world "

# 3. title() - Converts the first character of each word to uppercase

print(text.title())  
# " Hello World "

# 4. capitalize() - Converts the first character of the string to uppercase

print(text.capitalize())  
# " Hello world "

# 5. swapcase() - Swaps the case of each character

print(text.swapcase())  # " HELLO wORLD "

# Removing whitespace

# 6. strip() - 
# Removes leading and trailing whitespace

print(text.strip())  # "hello World"

# 7. lstrip() - 
# Removes leading whitespace

print(text.lstrip())  # "hello World "

# 8. rstrip() - Removes trailing whitespace

print(text.rstrip())  # " hello World"

# 9. replace() - Replaces occurrences of a substring with another substring

# replace(old, new)
print(text.replace("World", "Python"))  # " hello Python "

# 10. split() - 
# Splits the string into a list of substrings based on a delimiter

print(text.split())  # ["hello", "World"]

# 11. join() - Joins a list of strings into a single string with a specified delimiter

words = ["Hello", "World"]

print(" ".join(words))  # "Hello World"

# 12. find() - Returns the index of the first occurrence of a substring

print(text.find("World"))  # 7

# 13. count() - Returns the number of occurrences of a substring

print(text.count("o"))  # 2

# 14. startswith() - Checks if the string starts with a specified substring

print(text.startswith(" hello"))  # True

# 15. endswith() - Checks if the string ends with a specified substring

print(text.endswith("World "))  # True

# 16. isalpha() - Checks if all characters in the string are alphabetic

print(text.isalpha())  # False (because of spaces)

"abc".isalpha()  # True

# 17. isdigit() - Checks if all characters in the string are digits

print(text.isdigit())  # False

"123".isdigit()  # True

#List Methods

# 1. append() - Adds an item to the end of the list
numbers = [1, 2, 3]
numbers.append(4)

print(numbers)  # [1, 2, 3, 4]

# 2. extend() - Extends the list by appending elements from another iterable
numbers.extend([5, 6])
print(numbers)  # [1, 2, 3, 4, 5, 6]

# 3. insert() - Inserts an item at a specified index
numbers.insert(0, 0)
print(numbers)  # [0, 1, 2, 3, 4, 5, 6]

# 4. remove() - Removes the first occurrence of a specified value
numbers.remove(3)
print(numbers)  # [0, 1, 2, 4, 5, 6]

# 5. pop() - Removes and returns the item at a specified index (default is the last item)
last_item = numbers.pop()
print(last_item)  # 6
print(numbers)  # [0, 1, 2, 4, 5]

# 6. clear() - Removes all items from the list
numbers.clear()
print(numbers)  # []

# 7. index() - Returns the index of the first occurrence of a specified value
numbers = [1, 2, 3, 4, 5]
index_of_3 = numbers.index(3)

print(index_of_3)  # 2

# 8. count() - Returns the number of occurrences of a specified value
numbers.append(3)
count_of_3 = numbers.count(3)
print(count_of_3)  # 2

# 9. sort() - Sorts the items of the list in place
numbers.sort()
print(numbers)  # [1, 2, 3, 3, 4, 5]

# 10. reverse() - Reverses the items of the list in place
numbers.reverse()
print(numbers)  # [5, 4, 3, 3, 2, 1]



