#*args and **kwargs allow functions to accept a unknown number of arguments.
#*args If you do not know how many arguments will be passed into your function, add a * before the parameter name.

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus") # The youngest child is Linus

#You can combine regular parameters with *args.
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus") #Hello Emil Hello Tobias Hello Linus

#*args is useful when you want to create flexible functions:
def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3)) #6
print(my_function(10, 20, 30, 40)) #100
print(my_function(5)) #5

#If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#You can combine regular parameters with **kwargs.
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")
"""
Username: emil123
Additional details:
age: 25
city: Oslo
hobby: coding
"""

#You can use both *args and **kwargs in the same function.
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")
