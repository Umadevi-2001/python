#reverse given number $check given number is palindrom or not
num=int(input())
num1=num
n=num%10
a=0
#for n in range(0):
while n>0:
    print(n)
    a=a*10+n
    num=num//10
    n=num%10
print(a)
if num1==a:
    print("given number is palindrom")
else:
    print("not a palindrom")

