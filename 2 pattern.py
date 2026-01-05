'''n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i%2==0:
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()
#2
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()


n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or j==1 or j==n or i==1 or i==n:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()



n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or j==n:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()
    
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==1 or i==n or j==n:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print( )'''
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==n:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print( )