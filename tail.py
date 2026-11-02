def tail(n,acc=0):
    if n==0:
        return acc
    return tail(n-1,acc+n)

print("tail recursion with n=5 will be 5+4+3+2+1",tail(5))

a=int(input("enter a number: "))
print(tail(a))