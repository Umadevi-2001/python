# check weather a number is niven which is in string format
str1=input().split()
for i in range(len(str1)):
    str1[i]=int(str1[i])
print(str1)
digit=0
num=str1[0]
num1=num%10
while num1>0:
    digit=digit+num1
    num=num//10
    num1=num%10
print(digit)
if str[0]%digit==0:
    print(f"{str[0]} is a niven number")
    





