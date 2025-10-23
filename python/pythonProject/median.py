def main():
    median()


def median():
    # ввод значений
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))
    min_a = min(a, b, c)  # находим наименьшее значение
    max_a = max(a, b, c)  # находим наибольшее значение
    median = (a + b + c) - min_a - max_a  # находим медиану
    print(f"Медиана: {median}")  # вывод


main()