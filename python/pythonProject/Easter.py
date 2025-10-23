def get_year():
    """Получает год от пользователя с проверкой"""
    while True:
        try:
            year = int(input("Введите год: "))
            if 1583 <= year <= 9999:
                return year
            else:
                print("Год должен быть между 1583 и 9999")
        except ValueError:
            print("Пожалуйста, введите корректный год")

def calculate_easter_date(year):
    """Вычисляет дату Пасхи по алгоритму Гаусса"""
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    
    month = (h + l - 7 * m + 114) // 31
    day = 1 + ((h + l + 7 * m + 114) % 31)
    
    return day, month

def format_date(day, month, year):
    """Форматирует дату в читаемом виде"""
    months = {3: "марта", 4: "апреля"}
    return f"{day} {months[month]} {year} года"

def main():
    """Основная функция программы"""
    print("Программа для вычисления даты Пасхи")
    print("=" * 40)
    
    year = get_year()
    day, month = calculate_easter_date(year)
    
    print(f"Пасха в {year} году будет {format_date(day, month, year)}")

if __name__ == "__main__":
    main()