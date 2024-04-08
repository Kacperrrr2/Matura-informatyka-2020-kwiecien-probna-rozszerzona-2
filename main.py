import math


def nwd(a,b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    return a

def nww(a,b):
    a+b/nwd(a,b)

def czypierwsza(a):
    if a==2:
        return True

    if a<=1 or a%2==0:
        return False
    for i in range(3,int(math.sqrt(a))+1,2):
        if a%i==0:
            return False
    return True

def rideOrDie():
    print("ride")


