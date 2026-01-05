def num(a):
    sum=0
    for i in range(a):
        sum+=i
    print(sum)
a=int(input())
num(a)


print( "product of natural no")

def num(a):
    product=1
    for i in range(1,a):
        product*=i
    print(product)
a=int(input())
num(a)
 
print("sum of even numbers")
def even(n):
    for i in range(n):
        esum=0
        osum=0
        if i%2==0:
            esum+=i
        else:
            osum+=i
    print("even sum ",esum)
    print("sum of odd  ",osum)
n=int(input())
even(n)

            
        