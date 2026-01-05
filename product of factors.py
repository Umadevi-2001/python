num=[10,20,3,6,7]
idx=0
size=len(num)
for idx in range(size):
    product=1
    for i in range(1,num[idx]+1,1):
        if num[idx]%i==0:
            product*=i
    print("product of " ,num[idx],product)
