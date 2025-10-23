def FibonacciLastDigit(n):
    if n <= 1:
        return n 
    # Используем только две переменные вместо массива
    prev = 0
    current = 1

    for i in range(2, n+1):
        # Вычисляем следующее значение по модулю 10
        next_val = (prev + current) % 10
        prev = current
        current = next_val
    
    return current
print(FibonacciLastDigit(100))

def FibonacciLastAmount(n):
    # Используем период Пизано и формулу S_n = F_{n+2} - 1
    # Но аккуратно обрабатываем вычитание
    
    if n <= 1:
        return n
    
    k = (n + 2) % 60
    if k == 1:
        return 0
    if k == 0:
        k = 60
    
    a, b = 0, 1
    for i in range(2, k + 1):
        a, b = b, (a + b) % 10
    
    return (b - 1) % 10
n = int(input())
print(FibonacciLastAmount(n))

def FibonacciPartialSum(m, n):
    """
    Вычисляет последнюю цифру частичной суммы чисел Фибоначчи от F(m) до F(n)
    Использует формулу: Сумма от i=m до n F_i = (Сумма от i=0 до n F_i) - (Сумма от i=0 до m-1 F_i)
    """
    if m > n:
        return 0
    if m == 0:
        return FibonacciLastAmount(n)   # Если начинаем с F(0), просто возвращаем сумму до n
    
    sum_to_n = FibonacciLastAmount(n)    # Вычисляем сумму от 0 до n
    
    sum_to_m_minus_1 = FibonacciLastAmount(m - 1)
    partial_sum = (sum_to_n - sum_to_m_minus_1) % 10    # Частичная сумма = (сумма до n) - (сумма до m-1)
    return partial_sum
# Ввод пользователя для частичной суммы
m, n = map(int, input().split())
print(FibonacciPartialSum(m, n))

def FibonacciLastDigit(n):
    """
    Вычисляет последнюю цифру n-го числа Фибоначчи
    Оптимизировано с использованием периода Пизано (60 для mod 10)
    """
    if n <= 1:
        return n
    
    k = n % 60    # Используем период Пизано: F_n mod 10 = F_{n mod 60} mod 10
    
    prev = 0
    current = 1

    for i in range(2, k+1):
        next_val = (prev + current) % 10
        prev = current
        current = next_val
    
    return current

def FibonacciSumOfSquares(n):
    """
    Вычисляет последнюю цифру суммы квадратов первых n+1 чисел Фибоначчи (от F_0 до F_n)
    Использует формулу: F_0^2 + F_1^2 + ... + F_n^2 = F_n * F_{n+1}
    """
    if n <= 1:
        return n
    # Вычисляем последние цифры F_n и F_{n+1}
    last_digit_Fn = FibonacciLastDigit(n)
    last_digit_Fn_plus_1 = FibonacciLastDigit(n + 1)
    
    result = (last_digit_Fn * last_digit_Fn_plus_1) % 10    # Последняя цифра произведения = (последняя цифра F_n * последняя цифра F_{n+1}) mod 10
    
    return result
# Тестируем функцию для суммы квадратов
print("\nПоследняя цифра суммы квадратов чисел Фибоначчи:")
print(f"Сумма F(0)^2 до F(5)^2: {FibonacciSumOfSquares(7)}")  # 0^2+1^2+1^2+2^2+3^2+5^2 = 0+1+1+4+9+25 = 40, последняя цифра 0
print(f"Сумма F(0)^2 до F(10)^2: {FibonacciSumOfSquares(73)}")
print(f"Сумма F(0)^2 до F(100)^2: {FibonacciSumOfSquares(1234567890)}")