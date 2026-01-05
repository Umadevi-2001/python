def pal():
    n=input().split( )
    idx=0
    size=len(n)
    print(n)
    while idx<size:
        num=n[idx]
        a=len(num)
        rev=""
        for i in range(a-1,-1,-1):
            rev=rev+num[i]
        if num==rev:
            print(f"{num} given string is palindrom")
        else:
            print(f"{num} Not a palindrom")

        idx+=1
pal()