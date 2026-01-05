#reverse string and check palindrom or not
'''str=input("enter a string")
print(str[::-1])
print(reversed(str))'''

  

str1 =input()
a = ""
size = len(str1)
for i in range(size-1, -1, -1):
    a = a + str1[i]

print("Reversed string:", a)
if str1 == a:
    print("Palindrome")
else:
    print("Not a palindrome")

