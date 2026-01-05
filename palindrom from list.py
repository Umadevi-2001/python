num=[121,1234,12321,232,3454]
size=len(num)
idx=0
while idx>size:
    rev=0
    while num[idx]>0:
        digt=num[idx]%10
        rev=rev*10+digt                               
        
        num[idx]=num[idx]//10

    if num[idx]==rev:
        print("palindrom")
    else:
        print("not a palindrom")
    idx+=1