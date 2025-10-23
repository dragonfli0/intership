def spoces():
    def MaximumLoot(W, Weight, Cost):
        # Создаем список пар (стоимость/вес, индекс) для сортировки
        items = []
        for i in range(len(Weight)):
            if Weight[i] > 0:
                value_per_weight = Cost[i] / Weight[i]
                items.append((value_per_weight, i))
        
        items.sort(reverse=True)    # Сортируем по убыванию стоимости за единицу веса
        
        total_value = 0.0
        remaining_weight = W
        
        for value_per_weight, index in items:    # Берем предметы в порядке убывания стоимости за единицу веса
            if remaining_weight <= 0:
                break
            
            # Берем максимально возможное количество этого предмета
            amount = min(Weight[index], remaining_weight)
            total_value += Cost[index] / Weight[index] * amount
            remaining_weight -= amount
        
        return total_value

    n, W = map(int, input().split())
    Weight = []
    Cost = []

    for _ in range(n):
        c, w = map(int, input().split())
        Cost.append(c)
        Weight.append(w)

    # Вычисление и вывод результата с тремя знаками после запятой
    result = MaximumLoot(W, Weight, Cost)
    print(f"{result:.3f}")

def Souvenir():
    n, S = map(int, input().split())
    prices = []    # Считываем цены сувениров
    for _ in range(n):
        price = int(input())
        prices.append(price)
    
    prices.sort()    # Сортируем цены по возрастанию (жадный алгоритм)
    
    count = 0
    spent = 0
    
    # Берем самые дешевые сувениры
    for price in prices:
        if spent + price <= S:
            spent += price
            count += 1
        else:
            break
    print(count)

def Revenue(Click, Price):
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    result = Revenue(clicks, prices)
    print(result)

    revenue = 0
    # Создаем копии списков, чтобы не изменять оригиналы
    clicks = Click.copy()
    prices = Price.copy()
    
    while len(clicks) > 0:
        p = clicks.index(max(clicks))        # Находим индекс с максимальным значением в clicks
        q = prices.index(max(prices))        # Находим индекс с максимальным значением в prices
        
        revenue += clicks[p] * prices[q]        # Добавляем к выручке произведение максимальных значений
        # Удаляем использованные элементы
        clicks.pop(p)
        prices.pop(q)
    return revenue


def BillboardAdvertising():
    n, k, w = map(int, input().split())
    # Считываем заявки рекламодателей (стоимость за неделю, максимальное количество недель)
    advertisers = []
    for _ in range(k):
        c, w_max = map(int, input().split())
        advertisers.append((c, w_max))
    # Сортируем рекламодателей по убыванию стоимости за неделю
    advertisers.sort(reverse=True)
    
    total_profit = 0
    total_slots = n * w  # Общее количество доступных слотов
    # Заполняем слоты по порядку, начиная с самых дорогих рекламодателей
    for cost_per_week, max_weeks in advertisers:
        slots_to_use = min(max_weeks, total_slots)
        total_profit += cost_per_week * slots_to_use
        total_slots -= slots_to_use
        
        if total_slots == 0:
            break
    
    print(total_profit)


