n=int(input("enter your number: "))

def power(n):
    if(n<=0):
        return False

    if (n==1):
        return True

    if(n%4==0):
        return power(n/4)
    return False

if(power(n)):
    print("power of 4")
else:
    print("Not power of 4 ")