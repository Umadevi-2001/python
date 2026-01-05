def name(a):
    return 'i am ',a
print(name("Uma"))
print(type(name("Uma")))

print("..........")
def even(a):
    if a%2==0:
        print(f"{a} is even")
    else:
        print(f"{a} is odd")
a=int(input())
even(a)

print("..........")
def pos(a):
    if a>0:
        print(f"{a} is positive")
    elif a<0: 
        print(f"{a} is negative")
    else:
        print("Zero")
a=int(input())
pos(a)