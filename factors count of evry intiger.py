arr=[10,20,2,5,4,7]
size=len(arr)
idx=0
while idx<size:
    n=1
    count=0
    while n <= arr[idx]:
        if arr[idx]%n==0:
            count+=1
        n+=1
    print("count of factors ",arr[idx]," :",count)
       
    idx+=1