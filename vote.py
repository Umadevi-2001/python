#Check if age is eligible to vote (≥ 18).
a=int(input())
if a>=18 and a<=100:
    print("eligible for votting")
elif a>0 and a<18:
    print("not eligible")
else:
    print("invalid age")

    
age=int(input())
if 18<=age>=100:
    print("eligible")
elif 18>age<0:
    print("not eligible")
else:
    print("invalid")
