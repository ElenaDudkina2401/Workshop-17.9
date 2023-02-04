numbers = input('Введите целые числа через пробел: ')
user_number = int(input('Введите любое число: '))
def is_int(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False
if " " not in numbers:
    print("ОТСУТСТВУЮТ ПРОБЕЛЫ (введите числа через пробел).")
    numbers = input('Введите целые числа через пробел: ')
if not is_int(numbers):
    print("НЕВЕРНЫЙ ФОРМАТ ВВОДА (введите число)")
else:
    numbers = numbers.split()
list_numbers = [int(item) for item in numbers]
def qsort(array, left, right):
    middle = (left + right) // 2
    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)
    return array
list_numbers = qsort(list_numbers, 0, len(list_numbers) - 1)
def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Число выходит за диапазон списка, введите меньшее число.'
print(f'Упорядоченный по возрастанию список: {list_numbers}')
if not binary_search(list_numbers, user_number, 0, len(list_numbers)):
    rI = min(list_numbers, key=lambda x: (abs(x - user_number), x))
    ind = list_numbers.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < user_number:
        print(f'''В списке нет данного числа 
Ближайшее меньшее число: {rI} с индексом {ind}
Ближайшее большее число: {list_numbers[max_ind]} с индексом {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке нет данного числа
Ближайшее меньшее число: {rI} с индексом {list_numbers.index(rI)}
В списке нет меньшего числа''')
    elif rI > user_number:
        print(f'''В списке нет данного числа 
Ближайшее меньшее число: {rI} с индексом {list_numbers.index(rI)}
Ближайшее большее число: {list_numbers[min_ind]} с индексом {min_ind}''')
    elif list_numbers.index(rI) == 0:
        print(f'Индекс введенного числа: {list_numbers.index(rI)}')
else:
    print(f'Индекс введенного числа: {binary_search(list_numbers, user_number, 0, len(list_numbers))}')