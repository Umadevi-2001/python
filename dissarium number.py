num=int(input())
num1=num
num2=num1
count=0
while num>0:
    count+=1
    num=num//10
digit=0
a=num1%10
while a>0:
    digit=digit+a**count
    num1=num1//10
    a=num1%10
    count-=1
print(digit)
if num2==digit:
    print(f"{num2} dissarium number")
else:
    print("not a dissarium number")
    

