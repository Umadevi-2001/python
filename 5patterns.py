n=int(input())
a=n*n
for i in range(1,n+1):
    for j in range(1,n+1):
        print(a,end=" ")
        a-=1
    
    print( )
'''25 24 23 22 21 
20 19 18 17 16
15 14 13 12 11
10 9 8 7 6
5 4 3 2 1'''

#n=int(input())
a=0
for i in range(n):
    for j in range(n):
        print(a,end=" ")
        a+=2
    print()
''' 0 2 4 6 8
10 12 14 16 18 
20 22 24 26 28
30 32 34 36 38
40 42 44 46 48'''