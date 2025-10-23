# Иванова 11 ИС
people = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"] # список

people.append("Jerry") # добавляет имя Джерри в конец списка
print (people)
people.insert(3, "Jerry") # добавляет элемент Джерри в список по индексу 3
print (people)
people.extend(people) # добавляет набор элементов в конец списка
print (people)
people.remove("Alice") # удаляет первое вхождение элемента Алиса
print (people)
people.clear() # удаляет все элементы из списка
print(people)

people1 = list(["Tom", "Bob", "Alice", "Sam", "Sam", "Sam", "Tim", "Bill"]) # список
print(people1)
print(people1.index("Alice")) # возвращает индекс элемента Алиса
print(people1.pop(2)) # удаляет элемент по индексу 2 и возвращает его как результат
print(people1.pop()) # удаляет элемент последний элемент и возвращает его как результат
print(people1.count("Sam")) # возвращает кол-во вхождений элемента Сэм в список
people1.sort() # сортирует элементы
print(people1)
people1.reverse()
print(people1) # расставляет элементы в обратном порядке
print(people1.copy()) # копирует список

people2 = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"] # список
print(len(people2)) # возвращает длину списка
print(sorted(people2))# возвращает отсортированный список
print(min(people2))# возвращает наименьший элемент списка
print(max(people2))# возвращает наибольший элемент списка
