arr=[10,15,9,3,7,25,1]
idx=0
size=len(arr)
while idx<size:
    n=1
    sum=0
    while n<=arr[idx]:
        if arr[idx]%n==0:
            sum=sum+n 
        n+=1
    print(f"{arr[idx]} sum of factors=",sum)
    idx+=1