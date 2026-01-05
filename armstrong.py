# check given number is armstrong number or not
num = int(input())
num1 = num
count = 0
sum = 0
# Count number of digits
n = num
while n > 0:
    count += 1
    n //= 10
# Calculate Armstrong sum
while num1 > 0:
    digit = num1 % 10
    sum += digit ** count
    num1 //= 10
if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

    






    


