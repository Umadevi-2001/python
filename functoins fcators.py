def factor():
    a=int(input())
    num=a
    b=a%10
    while b>0:
        n=1
        print(f"{b} factors :",end=" ")
        while n<=b:
            if b%n==0:
                print(n,end=" ")
            n+=1
        print()
        a=a//10
        b=a%10
factor()

