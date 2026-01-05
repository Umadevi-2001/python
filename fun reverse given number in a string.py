def arr():
    n=input()
    size=len(n)
    rev=""
    for i in range(size-1,-1,-1):
        print(n[i])
        rev=rev+n[i]
    print(rev)
    if n==rev:
        print("given string is a Palindrom")
    else:
        print("given string is not a palindrom")
arr()
