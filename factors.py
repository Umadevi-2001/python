#check whether num1 is a factor of num2
num1=int(input())
num2=int(input())
if num1!=0 and num2%num1==0:
    print("num1 is factor of num2")
else:
    print("not a factor")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 == 0:
    print("Cannot divide by zero")
elif num2 % num1 == 0:
    print("num1 is a factor of num2")
else:
    print("num1 is not a factor of num2")
