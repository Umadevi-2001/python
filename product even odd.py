n=int(input())
'''x=2
a=1
count=0
while count<n:
    a*=2
    print(x)
    x+=2
    count+=1
print()
print(a)# print product of n even numbers



print()
x=1
a=1
count=0
while count<n:
    a*=x
    print(x)
    count+=1
    x+=2
print()
print(a)'''
start=0
pro=1
oddpro=1
while start<=n:
    if start%2==0:
        if start>0:
            pro*=start
    else:
       oddpro*=start 
    start+=1
print(pro)
print(oddpro)
    
