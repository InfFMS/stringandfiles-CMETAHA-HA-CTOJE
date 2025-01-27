# Напишите программу, которая просит пользователя ввести несколько предложений (например, 5, каждое предложение с новой строки).
# Каждое введенное предложение записывается в файл, но:
# Слова во всех предложениях должны быть приведены к верхнему регистру.
# Между словами вместо пробела ставится символ "_".
# После записи откройте этот файл, считайте содержимое и выведите его на экран.

import string

upWords = list(string.ascii_uppercase) + 'А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я'.split()
lowWords = list(string.ascii_lowercase) + 'а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я'.split()

print('Введите 5 предложений через строку: ')
lst = []
for i in range(5):
    str_in = list(input())
    for j in range(len(str_in)):
        if str_in[j] in lowWords:
            str_in[j] = upWords[lowWords.index(str_in[j])]
        if str_in[j] == ' ':
            str_in[j] = '-'
    str_in.append('\n')
    lst.append(str_in)

with open('task4.txt', 'w', encoding='utf-8') as file:
    for i in lst:
        i = ''.join(i)
        file.write(i)
