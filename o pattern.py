n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==4 or i==4:
            print("1",end=" ")
        else:
            print(" ",end=" ")
    print()
