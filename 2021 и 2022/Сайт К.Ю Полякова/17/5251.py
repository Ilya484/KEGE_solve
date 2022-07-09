'''
В файле 17-328.txt содержится последовательность целых чисел. Элементы последовательности – 
четырёхзначные натуральные числа. Найдите все тройки элементов последовательности, для 
которых восьмеричная запись суммы любой пары чисел тройки содержит только чётные цифры, 
а сумма всех чисел тройки меньше, чем сумма цифр всех чисел в файле, делящихся на 22. 
В ответе запишите количество найденных троек, затем минимальную из сумм элементов таких троек. 
В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
'''
# https://prnt.sc/V7WxcoGfMQWP


from itertools import combinations

f = open('17-328.txt')
arr = [int(x) for x in f.readlines()]

# нашли числа -> перевод в строку -> соединим элементы -> найдем сумму цифр строки
summ_22 = sum(map(int, ''.join((str(i) for i in arr if (i % 22 == 0)))))
count, min_sum = 0, float('inf')

for i in range(len(arr) - 2):
    # комбинации двух чисел превращаем в сумму (восьмеричная запись)
    summ = [oct(sum(x))[2:]
            for x in list(combinations([arr[i], arr[i + 1], arr[i + 2]], r=2))]

    # перебор цифр сумм пар чисел через генератор
    if (all(t[j] not in '1357' for t in summ for j in range(len(t))) and
            (arr[i] + arr[i + 1] + arr[i + 2]) < summ_22):
        summ_22 += 1
        min_sum = min(min_sum, arr[i] + arr[i + 1] + arr[i + 2])

print(summ_22, min_sum)
