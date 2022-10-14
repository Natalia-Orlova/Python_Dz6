# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import randint

def create_random_list(count):
    if count <= 0:
        print("Введено некорректное значение, повторите попытку")
        return []
    ls = [randint(0, 100) for i in range(count)]
    return(ls)

def compare_numbers(lst):
    new_list = [lst[i+1] for i in range(len(lst) - 1) if lst[i+1] > lst[i]]
    return (new_list)

num = int(input("Введите количество элементов: "))
first_list = create_random_list(num)
print(first_list)

result = compare_numbers(first_list)
print(result)
