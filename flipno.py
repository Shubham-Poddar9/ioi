def flip(n):
    if n//10==0:
        return n
    one=n%10
    z=flip(n//10)
    return one*pow(10,len(str(z)))+z

print("flip(453)= ", flip(453))
print("flip(768)=", flip(768))