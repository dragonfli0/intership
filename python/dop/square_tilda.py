#квадрат
def square(size):
    for i in range(size):
        if i == 0 or i == size - 1:
            print(" ~ " * size)  # Верхняя и нижняя границы
        else:
            print(" ~ " + "   " * (size - 2) + " ~ ")  # Боковые границы
# Задайте размер квадрата
size = 5
square(size)