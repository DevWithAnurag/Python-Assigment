
# 5. Implementation of all operators in Python
x = 10
y = 3

# Arithmetic Operators
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Modulus:", x % y)
print("Exponentiation:", x ** y)

# Comparison Operators
print("Equal:", x == y)
print("Not Equal:", x != y)
print("Greater Than:", x > y)
print("Less Than:", x < y)
print("Greater or Equal:", x >= y)
print("Less or Equal:", x <= y)

# Logical Operators
a, b = True, False
print("AND:", a and b)
print("OR:", a or b)
print("NOT:", not a)

# Bitwise Operators
print("Bitwise AND:", x & y)
print("Bitwise OR:", x | y)
print("Bitwise XOR:", x ^ y)
print("Bitwise NOT:", ~x)
print("Left Shift:", x << 2)
print("Right Shift:", x >> 2)

# Assignment Operators
x += 5  # Equivalent to x = x + 5
print("Assignment after += 5:", x)

# Identity Operators
a, b = [1, 2, 3], [1, 2, 3]
c = a
print("Is Operator:", a is c)
print("Is Not Operator:", a is not b)

# Membership Operators
print("In Operator:", 1 in list_var)
print("Not In Operator:", 10 not in list_var)