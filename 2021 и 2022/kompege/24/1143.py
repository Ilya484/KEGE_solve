'''
Текстовый файл содержит строку из заглавных букв A, B, C, D, E, F, 
всего не более чем из 106 символов. AF-подстроками назовём непустые последовательности 
идущих подряд символов A, B, C, D, E, F, ограниченные в начале символом A, а в конце символом F 
(граничные символы входят в подстроку). Определите количество AF-подстрок длиной от 7 до 10 символов.
'''
# https://prnt.sc/9VHozNDBTIAl


f = open('24_1.txt')
s = f.readline()

count = 0

for i in range(len(s) - 10):
    if s[i] == 'A':
        for j in range(6, 9 + 1):
            if s[i + j] == 'F':
                count += 1

print(count)
