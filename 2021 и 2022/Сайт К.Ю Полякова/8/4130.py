'''
Марина собирает восьмибуквенные слова из букв своего имени. Первые четыре 
буквы новых слов берутся из первых четырех букв имени, так чтобы ни одна буква 
не повторялась. А последние четыре буквы из последних трех букв имени, и они 
могут многократно повторяться. На каком месте окажется имя МАРИАННА в отсортированном 
по алфавиту списке сгенерированных слов? Нумерация начинается с 1.
'''
# https://prnt.sc/i_thcrxFeEUr


from itertools import *

arr = []

for i in permutations('АИМР', r=4):
    for j in product('АИН', repeat=4):
        word = ''.join(i) + ''.join(j)
        arr.append(word)

arr.sort()

for i, elem in enumerate(arr, start=1):
    if elem == 'МАРИАННА':
        print(i)
        break
