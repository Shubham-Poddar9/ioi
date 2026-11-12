def reverse(a):
    if len(a)==1:
        return a[0]

    firstchar=a[0]
    return reverse(a[1:])+firstchar

a="shubham"
print(reverse(a))