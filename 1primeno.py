n=int(input())
a=1
count=0
while a<=n:
    if n%a==0:
        count+=1
    a+=1    
if count==2:
    print("prime")
else:
    print("not a prime")