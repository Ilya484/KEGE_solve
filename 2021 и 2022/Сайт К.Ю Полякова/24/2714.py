'''
Текстовый файл 24-j6.txt состоит не более чем из 106 десятичных цифр. 
Восходящей последовательностью называется последовательность цифр, в которой 
каждая цифра меньше следующей за ней. Например, в последовательности 7238903278 
три таких последовательности – 2389, 03 и 278. Длиной последовательности называется 
количество входящих в нее цифр. Определите сколько в файле восходящих последовательностей 
длиной 5, не входящих в восходящие последовательности большей длины.
'''
# https://prnt.sc/2Ywfs32d5ASB


f = open('24.txt')
s = str(f.readline())

count, condition = 0, 1

for i in range(len(s) - 1):
    if (int(s[i]) < int(s[i + 1])):
        condition += 1

        if (condition == 5) and (s[i + 2] <= s[i + 1]):
            count += 1
            condition = 1
    else:
        condition = 1

print(count)
