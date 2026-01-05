5# factors of given number
n=int(input())
fact=1
i=1
sum=0
count=0
evensum=0
evencount=0
oddsum=0
ocount=0
#for i in range (1,n+1):
while i<=n+1:
    if n%i==0:
        count+=1# count of factors
        sum+=i  #sum of factors
        fact*=i #product of factors
        print(i)
        if i%2==0: # even factors
            evensum+=i
            evencount+=1
        else:   # odd factors
            oddsum+=i
            ocount+=1
    i+=1 
    
print("product of ",n,"factors:",fact)
print("sum of ",n,"factors:",sum)
print("conunt of ",n,"factors",count)
print(evensum)
print(evencount)
print(oddsum)
print(ocount)

print()
