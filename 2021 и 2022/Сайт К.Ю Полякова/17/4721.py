'''
В файле 17-243.txt содержится последовательность целых чисел. Элементы последовательности 
могут принимать целые значения от 0 до 10 000 включительно. Определите количество пар чисел, 
в которых ровно один из двух элементов больше, чем сумма цифр всех чисел в файле, 
делящихся на 61, а десятичная запись другого оканчивается на 33. В ответе запишите два числа: 
сначала количество найденных пар, а затем – минимальную сумму элементов таких пар. 
В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
'''
# https://prnt.sc/Dok3GLbTP-ju


f = open('17-243.txt')
arr = [int(x) for x in f.readlines()]

sums_61 = ([sum(map(int, str(i))) for i in arr if (i % 61 == 0)])

minn, k = float('inf'), 0

for i in range(len(arr) - 1):
    d = sorted([arr[i], arr[i + 1]])
    if (d[1] > sums_61 and d[0] <= sums_61) and (d[0] % 100 == 33):
        k += 1
        minn = min(arr[i] + arr[i + 1], minn)

print(k, minn)
