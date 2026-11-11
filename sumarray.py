def sum1(a):
    length=len(a)

    if length==1:
        return a[0]
    return a[0] + sum1(a[1:])

a=[1,2,3,4]

print("array total sum : ",sum1(a))