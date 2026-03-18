#Task 1:
text = 'Hello'
result =  list(text)
print(result)

#Task 2:
sen = "Python is easy to learn"
words = sen.split()
print(words)

#Task 3:
words = ["I", "love", "Python"]
result = " ".join(words)
print(result)

#Task 4:
word = "education"
count = word.count('a') + word.count('e') + word.count('i') + word.count('o') +word.count('u')
print (count)

#Task 5:
text = "python is easy and python is powerfull"
count = text.count("python")
print(count)

#Task 6:
names = ["jyoti", "rahul", "sneha"]
names[0] = names[0].title()
names[1] = names[1].title()
names[2] = names[2].title()
print(names)

#Task 7:
items = ["data", "science", "is", "fun"]
items[1] = "Analyst"
result = " ".join(items)
print(result)

#Task 8:
text = ["I", "Love", "Java"]
text[2] = "python"
print(" ".join(text))

#Task 9:
cities = ["Delhi", "Mumbai", "Chennai", "Kolkata"]
print(", ".join(cities))

#Task 10:
text = "Python"
lst = list(text)
lst.reverse() 
result = "".join(lst)
print(result)
