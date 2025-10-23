# table — некоторый ассоциативный контейнер (в table[i] будем сохранять F[i])
table = {}

def Fibonacci(n):
    if n not in table:  # если table[n] ещё не вычисляли
        if n <= 1:
            table[n] = n
        else:
            table[n] = Fibonacci(n-2) + Fibonacci(n-1)
    return table[n]

n = int(input())
result = Fibonacci(n)
print(result)

