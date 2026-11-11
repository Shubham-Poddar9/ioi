def maximun(a):
    length=len(a)
    if length ==1:
        return a[0]
    return max(a[0],maximun(a[1:]))

a=[1,2,34,324,345,57,45,4657]

print("largest element of array are ",maximun(a))