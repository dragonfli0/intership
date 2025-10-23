def gcd(x, y):
    x, y = abs(x), abs(y)
    while y != 0:
        x, y = y, x % y
    return x

a, b, c = map(int, input().split())

if a == 0 and b == 0:
    if c == 0:
        print("YES")
    else:
        print("NO")
else:
    g = gcd(a, b)
    if c % g == 0:
        print("YES")
    else:
        print("NO")
