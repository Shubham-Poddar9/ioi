def tail(n,num):
    if n>num:
        return
    print(n)
    tail(n+1,num)
n=int(input("Enter n to print to n: "))
tail(1,n)