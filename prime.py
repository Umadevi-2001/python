a=int(input())
if a<=1:
    print("not a prime")
else:
    count=0
    for i in range(1,a+1):
        if a%i == 0:
            count +=1
if count==2:
    print("prime")
else:
    print("not a prime")

            
        
a = input().lower()
b= 'aeiou'
if a in b:
    print("vowel")
else:
    print("not a vowel")
