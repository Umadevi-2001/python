def fact():
    #arr=[10,20,23,43,23]
    arr=input().split()
    idx=0
    size=len(arr)
    while idx<size:
        print(f"factors of {arr[idx]} :",end=" ")
        arr[idx]=int(arr[idx])
        for i in range(1,arr[idx]+1):
            if arr[idx]%i==0:
                print(i,end=" ")
        print()
        idx+=1


fact()
