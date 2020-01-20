# calculator.py

a = input ("enter first number: ")
b = input ("enter second number: ")
x = int(a) 
y = int(b)


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
print("you entered {}".format(x))
if x == "a":
  z = add(int(a), int(b))
  print (z)  
if x == "b":
    z = subtract(int(a), int(b))
    print (z)
if x == "c":
    z = multiply(int(a), int(b))
    print (z)
if x == "d":
    z = divide(int(a), int(b))
    print (z)
