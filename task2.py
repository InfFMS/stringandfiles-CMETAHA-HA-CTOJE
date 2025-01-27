# Откройте текстовый файл task2.txt для чтения.
# Считайте его содержимое в строку.
# Найдите и замените все вхождения слова "Python" на слово "Питон" (регистр учитывать).
# Запишите обновленный текст в новый файл с другим именем.
# Выведите на экран сообщение о количестве произведённых замен.
with open('task2.txt', encoding='utf-8') as file:
    lst = []
    count = 0
    for line in file:
        count += line.count('Python')
        lst.append(line.replace('Python', 'Питон'))
with open('task2_.txt', 'w', encoding='utf-8') as file:
    for i in lst:
        file.write(i)
print(count)
