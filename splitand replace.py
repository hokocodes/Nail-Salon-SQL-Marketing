import sys
import re

def f():
    two = []
    three = []
    for line in sys.stdin:
        arr = []
        for i in line:
            
            if i.isdigit():
                arr.append(line.index(i))
        three.append(line[arr[0]:].rstrip())
        arr = []

    for t in three:
        print(t)
f()
