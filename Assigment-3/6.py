# 6. Valid Triangle
a, b, c = input("Enter three angles: ").split()
a, b, c = int(a), int(b), int(c)

total = a + b + c

if total == 180:
    print("Valid Triangle")
else:
    print("Not a Valid Triangle")
