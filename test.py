# Useful modules: math, numpy, sys.
import math

test = "this thing"
pi = math.pi

list1 = ["sammich", 3, pi, complex(1.6, 2.7)]

if 1.6 + 2.7j in list1:
    print("I've got it, baby!")
else:
    print("Tough luck, babe.")

print(test.replace("this", "that").replace("thing", "that"))

