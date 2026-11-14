def ways(stairs):
    if stairs < 0:
        return 0
    if stairs==0:
        return 1
    return ways(stairs-1)+ways(stairs-2)

input("press enter to see the answer")
print("ways(3)=",ways(3))
print("ways(4)=",ways(4))

n=int(input("enter no of steps:- "))
guess=int(input("enter your guess "))
print("the answer is this ",ways(n),"your guess is ",guess)