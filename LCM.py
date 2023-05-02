def GCD(x, y): # Greatest Common Divisor
    if (y == 0):
        return x
    else:
        return GCD(y, x%y)

def LCM(x, y): # Least Common Multiple
    return x*y / GCD(x, y)
    
x = int(input("x: "))
y = int(input("y: "))

print("GCD : {0}".format(GCD(x, y)))
print("LCM : {0}".format(LCM(x, y)))