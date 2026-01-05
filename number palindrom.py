num=int(input())
rev=0
while num>0:
    digt=num%10
    rev=rev*10+digt
    num=num//10

if num==rev:
    print("palindrom")
else:
    print("not a palindrom")

