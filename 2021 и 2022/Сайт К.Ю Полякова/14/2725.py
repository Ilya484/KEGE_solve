'''
В какой системе счисления выполняется равенство 12X · 33X = 406X? 
В ответе укажите число – основание системы счисления.
'''
# https://prnt.sc/dg8d9Dbnf7TN


for i in range(7, 37):
    if (int('12', i)) * (int('33', i)) == (int('406', i)):
        print(i)
        break
