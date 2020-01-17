# calculator.py

def add (x, y):
  z = x + y
  print(" {} + {} = {}  ".format (x, y, z))
  return z
  
x = input ( "enter a letter: ")
print("yout entered {}".format(x))
if x == "a":
  z = add(56, 73)
  
elif x == "s": 
  a = 20
  b = -3
  c = a - b
  print(" {} - {} = {}  ".format (a, b, c))
else:
  print("The {} comman is not recognized." .format(x))
  
  print("Done")
