#Ввод неупорядоченной массива чисел через пробел, формирование списка
while True:
    try:
        list_input = str(input("Введите последовательность чисел через пробел\n")).split(" ")
        list_float = list(map(float, list_input))
        break
    except ValueError as error:
        print(error)
        print("Неверный тип данных")

#Ввод случайного числа, добавление его в массив
while True:
    try:
        any_number = float(input("Введите любое произвольное число "))
        list_float.append(any_number)
        break
    except ValueError as error:
        print(error)
        print("Неверный тип данных")

#Функция для сортировки массива от меньшего к большему
def sorting():
    array = list_float
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return(array)

#Функция поиска случайного числа
def searching(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return searching(array, element, left, middle - 1)
    else:
        return searching(array, element, middle + 1, right)

sorted_array = sorting() #Для хранения сортированного массива
idx = searching(sorted_array, any_number, 0, len(sorted_array)) #Для хранения индекса случайного числа
print("Сортированный массив: ", sorted_array)
print("Введенное число: ", any_number)
if idx >= 1: #Выводим индекс ближайшего меньшего числа
    print("Индекс ближайшего меньшего числа: ", idx - 1)
else: #На случай, если случайное число - наименьшее
    print("Число, которые Вы ввели - наименьшее")

