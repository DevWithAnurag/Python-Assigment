# 8. Fibonacci Series up to N
N = int(input())
a, b = 0, 1
print("Fibonacci Series:", end=" ")
while a <= N:
    print(a, end=" ")
    temp = a + b
    a = b
    b = temp
