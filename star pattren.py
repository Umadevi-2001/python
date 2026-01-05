'''n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()'''
'''* 
* * 
* * * 
* * * * 
* * * * * '''
'''
print()
print()
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()  
''''''
print()
print()
a=1
for i in range(n,0,-1):
    for j in range(i):
        print(a,end="   ")
        a+=1
    print()
'''
n=int(input())
a=1
for i in range(n):
    for j in range(i):
        print(a,end=" ")
        a+=1
    print()

