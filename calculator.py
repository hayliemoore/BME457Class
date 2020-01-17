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
  
x = input ("enter a letter: ")
print("yout entered {}".format(x))
if x == "a":
  z = add(47, 7)
  print (z)
if x == "b":
    z = subtract(47, 7)
    print (z)
if x == "c":
    z = multiply(47, 7)
    print (z)
if x == "d":
    z = divide(47, 7)
    print (z)
elif x == "s": 
  a = 20
  b = -3
  c = a - b
  print(" {} - {} = {}  ".format (a, b, c))
else:
  print("The {} comman is not recognized." .format(x))
  
  print("Done")
