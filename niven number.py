# check a number is a niven number
num=int(input())
num1=num
n=num%10
digit=0
while n>0:
    digit=digit+n
    num=num//10
    n=num%10
print(digit)
if num1%digit==0:
    print(f"{num1} is niven number")
else:
    print("not a niven number")


