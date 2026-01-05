arr=[10,15,9,3,7,25,1]
idx=0
size=len(arr)
while idx<size:
    n=1
    count=0
    while n<=arr[idx]:
        if arr[idx]%n==0:
            count+=1 
        n+=1
    print(f"composite number {arr[idx]}" if count!=2 and count!=1 else f" prime {arr[idx]}")
    idx+=1