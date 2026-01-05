marks=int(input())
if marks>=91 and marks<=100:
    print("grade:A")
elif 71<=marks<=90:
    print("grade:B")
elif 51<=marks<=70:
    print("grade:C")
elif 50>=marks>=35:
    print("grade:D")
elif marks>100:
    print("invalid input")
else:
    print("fail")
