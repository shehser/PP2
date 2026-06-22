#The bool() function allows you to evaluate any value, and give you True or False in return

print(bool("Hello")) #True
print(bool(15)) #True

#Any string is True, except empty strings and 0 and empty lists
bool(False)  #False
bool(None) #False
bool(0) #False
bool("") #False
bool(()) #False
bool([]) #False
bool({}) #False