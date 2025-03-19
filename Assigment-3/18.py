# 18. Palindrome Check
num = int(input())
original = num
rev_num = 0

while num > 0:
    digit = num % 10
    rev_num = rev_num * 10 + digit
    num //= 10

if original == rev_num:
    print("Palindrome")
else:
    print("Not a Palindrome")
