def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

a, b = map(int, input().split())
c, d = map(int, input().split())

numerator = a * d + c * b
denominator = b * d

g = gcd(numerator, denominator)
numerator //= g
denominator //= g

print(numerator, denominator)
    