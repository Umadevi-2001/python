#factorial of first n numbers
n= int(input("enter a number"))
a=1
fact=1
#for i in range(1,n+1):
while a<=n:
    fact *=a
    a+=1
print(fact)



