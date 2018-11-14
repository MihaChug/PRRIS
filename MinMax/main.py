# -*- coding: utf-8 -*-

inputText = open("input.txt")
data = inputText.read()
#создаем список из слов для удобства поиска
data = data.split(' ')
inputText.close
first = input("Input first word: ")
second = input("Input second word: ")
#определяем все вхождения первого и второго слова в исходном тексте
firstInputs = [i for i in range(len(data)) if data[i] == first]
secondInputs = [i for i in range(len(data)) if data[i] == second]
#максимальная разница в индексах - максимальное расстояние
maxRange = max(abs(firstInputs[0] - secondInputs[-1]), abs(secondInputs[0] - firstInputs[-1]))
minRange = len(data)
#ищем минимальное значение
for i in firstInputs:
    for j in secondInputs:
        maxMin = abs(i - j)
#если вычисленное расстояние больше текущего минимального и второй индекс больше первого, то переходим к следующему вхождению первого слова
        if minRange < maxMin and j > i:
            break
        minRange = min(minRange, maxMin)
print(minRange - 1, " ", maxRange - 1)



