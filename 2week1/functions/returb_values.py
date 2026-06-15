#Functions can return values using the return statement:
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result) #8
#Functions can return any data type, including lists, tuples, dictionaries, and more.
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2]) #apple banana cherry
