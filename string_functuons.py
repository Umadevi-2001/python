'''a="hello thops tech"
print(a[0::2])
print(a[5::2])
print(a[::2])'''
'''a="0123456789"
print(a[0:5:2])...op:024---->to skip 2 values after a value
print(a[0:7:3])...op:036  [starting index:stop index:step to skip]
print(a[0::3]).....op:0369 
print(a[:8:3])....op:036 to print a character skip 2 values upto 8 characters 
print(a[::-1])...op:9876543210 revers a string

a="thops tech career"
print(a[0::2])
a="123321"
b=a[::-1]
print(a==b)'''

'''
a = input()
b = a[::-1]

if a == b:
    print("palindrome")
else:
    print("not a palindrome")
'''
s = input("Enter a string: ")
i = 0

while True:
    try:
        print(s[i])
        i += 1
    except IndexError:
        break
