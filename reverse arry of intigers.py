# reverse array of intigers(to change string into intigers and reverse it)
arr=input().split()
size=len(arr)
idx=0
print(arr)
for i in range(0,size):
    arr[i]=int(arr[i])
print(arr)
print(arr[0])
num=arr[0]
n=num%10
rev=0
while n>0:
    rev=rev*10+n
    num=num//10
    n=num%10
print(rev)
if arr[0]==rev:
    print("palindrom")
else:
    print("not a palindrom")
