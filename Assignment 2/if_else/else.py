#The else statement is executed when the if condition (and any elif conditions) evaluate to False

a = 200
b = 33
if b > a:
  print("b is greater than a") #False
elif a == b:
  print("a and b are equal") #False
else:
  print("a is greater than b") #True, output: a is greater than b
