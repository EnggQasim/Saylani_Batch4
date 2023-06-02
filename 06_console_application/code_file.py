import sys

l = sys.argv

if len(l)>1:
    if l[1] == '--upgrade':
        print("Successfully update",l[0])
    else:
        print(l)