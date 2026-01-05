arr=[10,20,2,5,4,7]
size=len(arr)
idx=0
while idx<size:
    n=1
    while n <= arr[idx]:
        if arr[idx]%n==0:
            print("factora of ",arr[idx], ":",n)
        n+=1
    idx+=1
    

