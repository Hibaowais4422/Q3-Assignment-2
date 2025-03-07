# Arithmetic Operators
a = 10
b = 3

print("Arithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)

# Assignment Operators
x = 5
print("\nAssignment Operators")
x += 3  
print("x += 3:", x)
x -= 2  
print("x -= 2:", x)
x *= 2  
print("x *= 2:", x)
x /= 2  
print("x /= 2:", x)

# Comparison Operators
print("Comparison Operators")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Logical Operators
x, y = True, False
print("Logical Operators")
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

# Identity Operators
c = [1, 2, 3]
d = [1, 2, 3]
e = c

print("Identity Operators")
print("c is d:", c is d)
print("c is e:", c is e)
print("c is not d:", c is not d)

# Membership Operators
my_list = [1, 2, 3, 4, 5]

print("Membership Operators")
print("2 in my_list:", 2 in my_list)
print("10 not in my_list:", 10 not in my_list)

# Bitwise Operators
p = 6  # 110 in binary
q = 3  # 011 in binary

print("Bitwise Operators")
print("p & q:", p & q)   # AND
print("p | q:", p | q)   # OR
print("p ^ q:", p ^ q)   # XOR
print("~p:", ~p)         # NOT
print("p << 1:", p << 1)  # Left Shift
print("p >> 1:", p >> 1)  # Right Shift
