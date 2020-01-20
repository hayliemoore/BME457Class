# calculator.py




def add (x, y):
  z = x + y
  print(" {} + {} = {} ".format(x, y, z))
  return z
def subtract (x, y):
    z = x - y
    print(" {} - {} = {} ".format(x, y, z))
    return z
def multiply (x, y):
    z = x * y
    print(" {} * {} = {} ".format(x, y, z))
    return z
def divide (x, y):
    z = x / y
    print(" {} / {} = {} ".format(x, y, z))
    return z
    
a = input ("enter first number: ")
b = input ("enter second number: ")
x = int(a) 
y = int(b)
  
sym = input ("enter a letter: ")
print("you entered {}".format(x))
if sym == "a":
  z = add(x, y)
  print (z)  
elif sym == "b":
    z = subtract(x, y)
    print (z)
elif sym == "c":
    z = multiply(x, y)
    print (z)
elif sym == "d":
    z = divide(x, y)
    print (z)
else:
    print("the {} command is not recognized.".format(x))   
print("Done")
