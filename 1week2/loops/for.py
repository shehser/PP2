#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) #apple banana cherry

#We can use for loop even for strings
for x in "banana":
  print(x) #b a n a n a

#Also we can use break for "for"
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) #apple

#We also can use continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) # apple banana