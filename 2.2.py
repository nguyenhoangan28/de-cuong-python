a, b = map(float,input().split())
if a == 0:
    if b > 0:
        print("VSN")
    else:
        print("VN")
elif a > 0:
    x = -b/a 
    print("x > {0:.2f}".format(x))
else:
    x = -b/a 
    print("x < {0:.2f}".format(x))
