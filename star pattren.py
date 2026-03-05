"""
Pattern Programs in Python

This script demonstrates different star and number patterns
using nested loops in Python.
"""

# Input from user
n = int(input("Enter the number of rows: "))

print("\n1. Increasing Star Pattern")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()


print("\n2. Decreasing Star Pattern")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


print("\n3. Continuous Number Triangle Pattern")
num = 1
for i in range(n, 0, -1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


print("\n4. Increasing Number Pattern")
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


