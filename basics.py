# basics
x = input("enter a letter: ")
print("you entered {}".format(x))
if x == "a":
    a = 1
    b = 2
    c = a + b
    print ("{} + {} = {}".format(a, b, c))
elif x == "s":
      a = 20
      b = -3
      c = a - b
      print("{} - {} = {}".format(a, b, c))
elif x == "m":
    a = 2
    b = 4
    c = a * b
    print("{} * {} = {}".format(a, b, c))
else:
    print("the {} command is not recognized.".format(x))
        
print("Done")
