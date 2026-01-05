n=int(input())
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()
print()
print()
for i in range(n):
    for j in range(n):
        if i==0 or i==2 and j==0 or i==1 and j==1 or i==2 and j==1 or j==n-1 and i==n-1  or j==n-2 and i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
        