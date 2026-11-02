def tree(n,num):
    if(n<1 or n>num):
        return
    print(n)
    tree(n-1,num)
    print(n)

n=int(input("enter a number : "))
tree(n,n)