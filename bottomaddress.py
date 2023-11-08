import sys

def f():
    two = []
    three = []
    for line in sys.stdin:
        arr = []
        for i in line:
            
            if i == ',':
                arr.append(line.index(i))
        three.append(line[arr[0]+2:].rstrip())
        arr = []

    for t in three:
        print(t)
f()
