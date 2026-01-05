n=int(input())
for i in range(n):
    for k in range(n-i):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
for l in range(n,-1,-1):
    for m in range(n-l):
        print(end=" ")
    for p in range(l):
        print("*",end=" ")
    
    print()




        