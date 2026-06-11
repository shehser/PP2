#While loop will be woeking until condition is true
a = 1
while(a<6):
    print(a)
    a += 1

#To stop while you can use break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  #Output: 1 2 3 

#With the continue statement we can stop the current iteration of the loop, and continue with the next:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)