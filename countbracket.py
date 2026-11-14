def count(n,l=0,r=0):
    if l==n and r==n:
        return 1
    total = 0
    if l>r:
        total+= count(n,l,r+1)
    if l<n:
        total+=count(n,l+1,r)

    return total

input("press enter to count the cobinations of brackets ")
print("count(1)=",count(1))
print("count(3)=",count(3))

n=int(input("enter no of pairs "))
guess=int(input("enter your guess "))
print("the answer is ",count(n),"your guess is ",guess)