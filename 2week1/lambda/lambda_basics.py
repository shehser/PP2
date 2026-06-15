#A lambda function is a small anonymous function.
x = lambda a : a + 10
print(x(5)) #5+10=15

#Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))

#The power of lambda is better shown when you use them as an anonymous function inside another function.
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))#22

