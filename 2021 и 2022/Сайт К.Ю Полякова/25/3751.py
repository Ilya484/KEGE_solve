'''
Найдите все натуральные числа, принадлежащие отрезку [100 000 000; 101 000 000], 
у которых ровно три различных чётных делителя. В ответе перечислите найденные числа 
в порядке возрастания, справа от каждого числа запишите его второй по величине 
нетривиальный делитель (не равный 1 и самому числу).
'''


# https://prnt.sc/gXnPbsZwZtdj


def dividers(n):
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for i in range(100_000_000, 101_000_000 + 1):
    if i % 2 == 0:
        c = i // 2
        if (int(c ** 0.5) ** 2 == c) and (dividers(c ** 0.5) == True):
            print(i, int(c ** 0.5))
