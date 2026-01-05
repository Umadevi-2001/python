n=int(input())
'''for a in range(n):
    for b in range(a):
        print("*",end=" ")
    print( )
for c in range(n,0,-1):
    for d in range(c):
        print("*",end=" ")
    print( )'''

for p in range(n+1):
    for q in range(n+1-p):
        print(" ",end=" ")
    for k in range(p):
        print("*",end=" ")
    print()
    '''
for i in range(n-1,0,-1):
    for j in range(n+1-i):
        print(" ",end=" ")
    for l in range(i):
        print("*",end=" ")
    print()'''
