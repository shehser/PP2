#To open the file, use the built-in open() function.
f = open("demofile.txt","r")
print(f.read())
#You can also use the with statement when opening a file:
with open("demofile.txt","r") as f:
  print(f.read())
#You can return one line by using the readline() method:
with open("demofile.txt","r") as f:
  print(f.readline())

#Also you can create new file, if it doesn't exist by "x"
f = open("myfile.txt", "x")

