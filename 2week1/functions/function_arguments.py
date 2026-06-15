#Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
"""
Output:
Emil Refsnes
Lobias Refsnes
Linus Refsnes
"""

#A parameter is the variable listed inside the parentheses in the function definition.

#An argument is the actual value that is sent to the function when it is called.
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

#By default, a function must be called with the correct number of arguments.
#Correct one:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes") #Emil Refsnes

#Error:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")


#You can assign default values to parameters. If the function is called without an argument, it uses the default value:
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")
"""
Hello Emil
Hello Tobias
Hello friend
Hello Linus
"""

#You can send any data type as an argument to a function (string, number, list, dictionary, etc.)
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits) #apple banana cherry
