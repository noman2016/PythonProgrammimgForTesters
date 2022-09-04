# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

## Arithmetic operators

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

## Assignment operators

x = 10
x += 2
print(x)
x -= 4
print(x)
x *= 4
print(x)
x /= 4
print(x)
x **= 4
print(x)

## Comparison operators

x = 10
y = 6

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x <= y)
print(x >= y)


## Logical operators

x = 10
y = 4

print(x == y and x > y)
print(x == y or x > y)


## Identity operators

x = ["noman", "sqa"]
y = ["noman", "sqa"]

print(x is y)
print(x == y)

## Membership operators

x = ["noman", "sqa"]
y = ["noman", "sqa"]

print("sqa" in y)
print("sqa" not in y)

## Bitwise operators

# & 	AND	                        Sets each bit to 1 if both bits are 1
# |	    OR	                        Sets each bit to 1 if one of two bits is 1
#  ^	XOR	                        Sets each bit to 1 if only one of two bits is 1
# ~ 	NOT	                        Inverts all the bits
# <<	Zero fill left shift	    Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	Signed right shift	        Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

# Binary
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11

x = 1
y = 3
print(x & y)
print(x | y)
