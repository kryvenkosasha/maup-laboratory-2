import math

a = int(input())
b = int(input())

least_common_multiple = (a * b) // math.gcd(a, b)
print(least_common_multiple)
