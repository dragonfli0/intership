def Fibonacci(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for iter in range(n-1):
        oldPrevious = previous
        previous = current
        current = oldPevious + previous
    return current
