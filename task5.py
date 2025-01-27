# Откройте текстовый файл task5.txt для чтения.
# Найдите самое длинное слово в тексте. Если таких слов несколько, выберите первое из них.
# Запишите это слово и его длину в новый файл в формате:
# Самое длинное слово: слово
# Его длина: длина
#
# Выведите это слово и длину в консоль.

import string
punc = string.punctuation
space = string.whitespace
lst = punc + space
with open('task5.txt', encoding='utf-8') as file:
    max_len = 0
    word = []
    max_word = []
    for line in file:
        count = 0
        line = list(line)
        for i in line:
            if i in lst:
                if count > max_len:
                    max_len = count
                    max_word = word
                word = []
                count = 0
            else:
                count += 1
                word.append(i)
print(f'Самое длинное слово: {''.join(max_word)}')
print(f'Его длина: {max_len}')
