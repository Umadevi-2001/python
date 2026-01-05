# check given number is armstrong number or not
num =input().split()
for i in range(0,len(num)):
    num[i]=int(num[i])
print(num)
num1=num[0]
count=0
digit=0
while num1 > 0:
    count += 1
    num1 //= 10
print(count)
# Calculate Armstrong sum
while num1 > 0:
    digit = num1 % 10
    sum += digit ** count
    num1 //= 10
# Check result
if sum == num[0]:
    print("Armstrong number")
else:
    print("Not an Armstrong number")