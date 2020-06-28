"""

Алфавит языка племени «тумба-юмба» содержит всего несколько букв. Найдите все слова длины K,
которые можно построить с помощью этого алфавита и в которых нет двух гласных букв, стоящих рядом.
Гласными считаются буквы 'A', 'E', 'I', 'O' и 'U'.

"""


def func(s):
    global count
    if len(s) == k:  # Если длина s равна k
        print(s)  # То печатаем s т.к. это слово
        count += 1  # И плюсуем 1
    else:  # Иначе
        if s[-1] in glas:  # если последняя буква в s равна гласной
            for j in sglas:  # Прибавляем согласную и делаем рекурсию для следующего прибавления
                func(s + j)  # Т.к. после гласной может идти только согласная
        else:  # Иначе
            for j in stroka:  # Прибавляем буквы из всей строки и делаем рекурсию
                func(s + j)  # Т.к. после согласной может идти любая буква из строки


stroka = input()  # Вводим нашу строка
k = int(input())  # Вводим длину слова
glas = []  # Массив для гласных
count = 0  # Переменная для счета
sglas = []  # Массив для согласных
for i in stroka:  # Разделяем нашу основную строку на два массива глас и соглас
    if i in {'A', 'E', 'I', 'O', 'U'}:
        glas.append(i)
    else:
        sglas.append(i)
for i in stroka:  # Последовательно берем э-ты из строки и дополняем ее буквами из других массивов
    func(i)  # Выполняем функцию

print(count)  # Печатаем ко-во слов в языке
