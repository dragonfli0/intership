def generate_fibonacci_up_to(limit):
    fib = [1, 2]
    while True:
        next_fib = fib[-1] + fib[-2]
        if next_fib > limit:
            break
        fib.append(next_fib)
    return fib

def canonical_fibonacci_representation(N):
    if N == 0:
        return "0"
    fib = [1, 2]
    while fib[-1] + fib[-2] <= N:
        fib.append(fib[-1] + fib[-2])
    fib.reverse()  # Now largest first
    representation = []
    for f in fib:
        if N >= f:
            representation.append('1')
            N -= f
        else:
            representation.append('0')
    # Remove leading zeros
    while representation and representation[0] == '0':
        representation.pop(0)
    if not representation:
        return "0"
    return ''.join(representation)

# Read input
N = int(input())
result = canonical_fibonacci_representation(N)
print(result)
