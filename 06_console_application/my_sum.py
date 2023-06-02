import sys

l = sys.argv

if len(l)>2:
    a = (int(l[1])+int(l[2]))
    print(f"Num1: {l[1]} and Num2: {l[2]} = {a}")