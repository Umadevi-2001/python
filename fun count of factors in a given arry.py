def fact():
    arr=input().split()
    idx=0
    size=len(arr)
    while idx<size:
        print(f"count of factors {arr[idx]} : ",end=" ")
        arr[idx]=int(arr[idx])
        count=0
        for i in range(1,arr[idx]+1):
            if arr[idx]%i==0:
                count+=1
        print(count)
        idx+=1
fact()
