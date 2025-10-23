#Ивановой Вероники 11 ИС. Задача на шифрование с использованием XOR
cipher = str(input("Введите сообщение капсом (пример: ДОБРОЕ УТРО!): "))
keys = int(input("Введите ключ : "))
codecipher = []
decodecipher = []
# Вводим алфавит
alphabet = {
    0: "А", 1: "Б", 2: "В", 3: "Г", 4: "Д", 5: "Е", 6: "Ё", 7: "Ж", 8: "З", 9: "И",
    10: "Й", 11: "К", 12: "Л", 13: "М", 14: "Н", 15: "О", 16: "П", 17: "Р", 18: "С",
    19: "Т", 20: "У", 21: "Ф", 22: "Х", 23: "Ц", 24: "Ч", 25: "Ш", 26: "Щ", 27: "Ъ",
    28: "Ы", 29: "Ь", 30: "Э", 31: "Ю", 32: "Я"
}
# Шифрование
for i in cipher:
    for key, value in alphabet.items():
        if i in alphabet.values():
            if i == value:
                code = (key + keys) % 33  # Применяем преобразование к ключу
                new_code = (key^keys) # Применяем XOR
                codecipher.append(alphabet.get(new_code, i)) # добавляем в результат
                break
        else:
            codecipher.append(i)
            break
# Дешифрование
for i in codecipher:
    for key, value in alphabet.items():
        if i in alphabet.values():
            if i == value:
                code = (key + keys) % 33  # Применяем преобразование к ключу
                new_code = (key^keys) # Применяем XOR

                decodecipher.append(alphabet.get(new_code, i)) # Добавляем в результат
                break
        else:
            decodecipher.append(i)
            break
# Вывод
print("Зашифрованное сообщение: "+''.join(codecipher))
print("Исходное сообщение: "+''.join(decodecipher))