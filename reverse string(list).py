arr=input().split()
size=len(arr)
idx=0
rev=0
print(arr)
for i in range(size,-1):
    arr[i]=int(arr[i])
    a=arr[0]
    print(arr[i])
    rev=rev*10+arr[i]
print(arr)