# Иванова 11 ИС постфиксная-инфиксная форма
def main(): # Главная функция
    math_exp = input("Введите математическое выражение в инфиксной форме: ") # Запрашиваем у пользователя математическое выражение
    postfix = in_post(math_exp)  # Преобразуем инфиксное выражение в постфиксное
    result = rate_post(postfix) # Вычисляем значение постфиксного выражения
    print("Результат вычисления:", result)

def quantity(n): #Возвращает приоритет операции
    if n in ('+', '-'):
        return 1
    if n in ('*', '/'):
        return 2
    return 0

def is_number(a): # Функция для проверки, является ли строка числом
    try:
        int(a)
        return True
    except ValueError:
        return False

def in_post(math_exp): # Функция для преобразования инфиксного выражения в постфиксное
    output = []  # Список для итогового постфиксного выражения
    oper = []  # Список для операторов
    lexemes = math_exp.split()  # Разделяем выражение на лексемы
    for lexeme in lexemes:
        if is_number(lexeme):  # Если лексема число
            output.append(lexeme)
        elif lexeme == '(':  # Если лексема (
            oper.append(lexeme)
        elif lexeme == ')':  # Если токен )
            while oper and oper[-1] != '(':
                output.append(oper.pop())
            oper.pop()  # Удаляем открывающую скобку из oper
        else:  # Если лексема оператор
            while (oper and quantity(oper[-1]) >= quantity(lexeme)):
                output.append(oper.pop())
            oper.append(lexeme)
    while oper:  # Функция для добавления оставшиеся операторы в выходной список
        output.append(oper.pop())
    return output

def rate_post(postfix): # Функция для вычисления постфиксного выражения
    values = []  # Список для операндов
    for lexeme in postfix:
        if is_number(lexeme):  # Если лексема число
            values.append(int(lexeme))
        elif lexeme in ('+', '-', '*', '/'):  # Если лексема бинарный оператор
            right = values.pop()  # Удаляем последний элемент как правый операнд
            left = values.pop()  # Удаляем предпоследний элемент как левый операнд
            if lexeme == '+':
                result = left + right
            elif lexeme == '-':
                result = left - right
            elif lexeme == '*':
                result = left * right
            elif lexeme == '/':
                if right == 0:  # Проверка деления на ноль
                    return "Ошибка: Деление на ноль"
                result = left // right  # Целочисленное деление
            values.append(result)  # Добавляем результат обратно в стек
        elif lexeme == '-':  # Унарный оператор
            if values:
                negated_value = -values.pop()
                values.append(negated_value)
    return values[0] if values else None  # Возвращаем результат

if __name__ == "__main__": # Запуск программы
    main()