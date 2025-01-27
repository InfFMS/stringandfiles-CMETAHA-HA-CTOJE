# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле.
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.
count_lines = 0
count_words = 0
count_symbols = 0
with open('task1.txt', encoding='utf-8') as file:
    for line in file:
        count_lines += 1
        for i in line:
            if i != ' ':
                count_words += 1
        count_symbols += len(line)
    print('count_lines', count_lines)
    print('count_words', count_words)
    print('count_symbols', count_symbols)




