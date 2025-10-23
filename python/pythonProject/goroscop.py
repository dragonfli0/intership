# Иванова и Удин 11ИС
print("Ваш знак зодиака")

#Ввод данных пользователем
day = int(input("Введите Ваш день рождения "))
month = input("Введите Ваш месяц рождения (словом) ")

#Определяем знак зодиака
if (month == "март" and day >= 21) or (month == "апрель" and day <= 19):
    zodiac_sign = "Овен"
elif (month == "апрель" and day >= 20) or (month == "май" and day <= 20):
    zodiac_sign = "Телец"
elif (month == "май" and day >= 21) or (month == "июнь" and day <= 21):
    zodiac_sign = "Близнецы"
elif (month == "июнь" and day >= 22) or (month == "июль" and day <= 22):
    zodiac_sign = "Рак"
elif (month == "июль" and day >= 23) or (month == "август" and day <= 22):
    zodiac_sign = "Лев"
elif (month == "август" and day >= 23) or (month == "сентябрь" and day <= 22):
    zodiac_sign = "Дева"
elif (month == "сентябрь" and day >= 23) or (month == "октябрь" and day <= 23):
    zodiac_sign = "Весы"
elif (month == "октябрь" and day >= 24) or (month == "ноябрь" and day <= 23):
    zodiac_sign = "Скорпион"
elif (month == "ноябрь" and day >= 22) or (month == "декабрь" and day <= 21):
    zodiac_sign = "Стрелец"
else:
    zodiac_sign = "Определить знак зодиака не получилось"

print(f"Ваш знак зодиака: {zodiac_sign}")