# Задание 6
# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово
# должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func(word):
    for ch in word:
        if (ord(ch) < 97 or ord(ch) > 122) and ch not in ['-', '.', ',']:
            return word
    return word.capitalize()


words = 'Some types, such функция as ints are русские буквы able to use a more7 efficient ' \
        'функция-функция community-wide ' \
        'algorithm55 when.'.split()

string_capitalized = ' '.join([int_func(word) for word in words])
print(string_capitalized)
