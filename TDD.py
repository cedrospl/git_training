import string

def f1(x,y = 0):
    return (x * x) + y

def f2(x = "BUUUUM"):
    if (x) == "BUUUUM":
        return x
    else:
        return x[0]
    
