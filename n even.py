n=int(input())
x=0
a=0
while x<=n:
    print(x)#print n even numbers
    x+=a
    x+=2
print()
print(x)#print sum of n even numbers
print()
print()


#----->print n odd numbers
n=int(input())
x=1
a=0
while x<=n:
    print(x)#print n odd numbers
    a+=x
    x+=2
    
print()
print(a)#print sum of n odd numbers
