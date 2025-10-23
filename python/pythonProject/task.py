import math

''' 
Удин и Иванова 11ИС
'''
def change():
    change = int(input("Введите сумму сдачи ")) # Ввод суммы сдачи
    if change <= 0: # проверка на значение вводимой сдачи
        print ("Нет сдачи")
    else:
        a = change // 200 # toonie
        b = (change % 200) // 100 # loonie
        c = ((change % 200) % 100) // 25 # 25cent
        d = (((change % 200) % 100) % 25) // 10 # 10cent
        e = ((((change % 200) % 100) % 25) % 10) // 5 # 5cent
        f = (((((change % 200) % 100) % 25) % 10) % 5) // 1 #1cent
    print (f'toonie - {a}, loonie - {b}, 25 cent - {c}, 10 cent - {d}, 5 cent - {e}, 1 cent - {f}') # Вывод монет

def bottles():

    BigBottleCost = 0.25 # стоимость большой бутылки
    SmallBottleCost = 0.10 # стоимость маленькой бутылки
    print("Введите кол-во больших бутылок: ")
    BigBottle = int(input()) # количество больших бутылок
    print("Введите кол-во маленьких бутылок: ")
    SmallBottle = int(input()) # количество маленьких бутылок

    if BigBottle < 0 or SmallBottle < 0: # проверка на кол-во бутылок
        print("Количество бутылок не может быть меньше нуля")
    else:
        print(f'Стоимость всех  {(BigBottle * BigBottleCost) + (SmallBottleCost * SmallBottle)}$, ') #Вывод суммы

def distance():
    # Ввод параметров для вычесления
    t1 = float(input("t1 "))
    g1 = float(input("g1 "))
    t2 = float(input("t2 "))
    g2 = float(input("g2 "))

    # Перевод параметров из градусов в радианы
    t1 = (math.pi / 180) * t1
    g1 = (math.pi / 180) * g1
    t2 = (math.pi / 180) * t2
    g2 = (math.pi / 180) * g2
    '''
    Расчет расстояния между объектами
    '''
    distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
    print(distance)

distance()
