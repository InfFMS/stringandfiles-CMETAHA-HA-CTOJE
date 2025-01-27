# Откройте текстовый файл task3.txt для чтения.
# Извлеките все уникальные слова из файла (слова разделяются пробелами и знаками пунктуации).
# Подсчитайте, сколько раз каждое уникальное слово встречается в тексте.
# Запишите результаты в новый файл в формате:
# слово1: количество
# слово2: количество
#
# Убедитесь, что слова записаны в алфавитном порядке.

import string

punc = string.punctuation
spases = string.whitespace
bad_symbols = punc + spases
upWords = list(string.ascii_uppercase) + 'А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я'.split()
lowWords = list(string.ascii_lowercase) + 'а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я'.split()

with open('task3.txt', encoding='utf-8') as file:
    lst = []
    for line in file:
        for i in line:
            if i not in punc:
                lst.append(i)

word = []
lst_1 = []
for i in lst:
    if i not in spases:
        if i in upWords:
            i = upWords.index(i)
            i = lowWords[i]
        word.append(i)
    if i in spases:
        if len(word) != 0:
            lst_1.append(''.join(word))
        word = []
lst_1.append(''.join(word))

reester = []
for i in range(len(lst_1)):
    if lst_1[i] not in reester:
        reester.append(lst_1[i])
        print(f'"{lst_1[i]}" количество: {lst_1.count(lst_1[i])}')
