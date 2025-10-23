#Ивановой Вероники 11ИС, дз с 25.3.2025

def excluding(nums, n): #функция на удаление макс и мин значений
    if n > 0:
        nums_list = nums.copy() # создаем копию списка
        # удаляем n наименьших и наибольших значений
        for i in range(n):
            nums_list.remove(min(nums_list))
        for i in range(n):
            nums_list.remove(max(nums_list))
        return nums_list
    else:
        return nums

user_nums = input('Введите целые числа, разделяя их пробелами: ')
#проверка на дурака
try:
    nums = list(map(int, user_nums.split()))
    if len(nums) < 4: # проверка на кол-во чисел
        print('Error: должно быть введено более 4х чисел')

    n = int(input('Введите кол-во чисел для удаления: '))
    nums_list = excluding(nums, n)

    print(f'Введенный список: {nums}')
    print(f'Измененный список: {nums_list}')
except ValueError:
    print('Error input')

