def rev():
    n=int(input())
    n1=n
    num=n%10
    rn=0
    while num>0:
        rn=rn*10+num
        n1=n1//10
        num=n1%10
    print(rn)
rev()