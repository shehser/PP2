#Elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True

a = 33 
b = 33
if(a>b):
    print("a is greater than b")
elif(a==b):
    print("They are equal")

#Note: you can make multiple variation of elif:
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")