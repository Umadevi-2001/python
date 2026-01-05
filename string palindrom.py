string=input()
size=len(string)
idx=size-1
rev=""
while idx>=0:
    print(string[idx])
    rev=rev+string[idx]
    idx-=1
print(rev)
if string==rev:
    print("given string is palindrom")
else:
    print("noa a palindrom")

