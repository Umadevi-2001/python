def composite():
    arr=input().split()
    idx=0
    size=len(arr)
    while idx<size:
        arr[idx]=int(arr[idx])
        n=arr[idx]
        count=0
        for i in range(1,n+1):
            if n%i==0:
                count+=1
        if count!=2:
            print(f"{n} is a composite numbers")
        else:
            print(f"{n} is a prime numbers")
        idx+=1
    

composite()
    