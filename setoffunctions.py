def issquare(a):
    if (a**0.5)%1==0:
        return True
    else:
        return False

def istriangle(a,b,c):
    if (a+b>c and b+c>a and a+c>b):
        return True
    else:
        return False
	