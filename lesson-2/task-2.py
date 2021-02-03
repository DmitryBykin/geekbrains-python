# Задание 2
# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с
# индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

input_str = input('Введите элементы списка (через пробел): ')
input_list = input_str.split(' ')
print(f'Исходный список: {input_list}')

ind = 0
while ind < (len(input_list) - 1) if len(input_list) % 2 else ind < len(input_list):
    input_list[ind], input_list[ind + 1] = input_list[ind + 1], input_list[ind]
    ind += 2

print(f'Преобразованный список: {input_list}')
