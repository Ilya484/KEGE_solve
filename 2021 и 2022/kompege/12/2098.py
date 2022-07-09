'''
(Досрочный ЕГЭ 2020 г.) Исполнитель Редактор получает на вход строку цифр и 
преобразовывает её. Редактор может выполнять две команды, в обеих командах v и w 
обозначают цепочки цифр.
1. заменить (v, w)
2. нашлось (v)
Первая команда заменяет в строке первое слева вхождение цепочки v на цепочку w, 
вторая проверяет, встречается ли цепочка v в строке исполнителя Редактор. 
Если она встречается, то команда возвращает логическое значение «истина», 
в противном случае возвращает значение «ложь». Дана программа для исполнителя Редактор:
НАЧАЛО
  ПОКА нашлось (>1) ИЛИ нашлось (>2) ИЛИ нашлось (>3)
    ЕСЛИ нашлось (>1)
      ТО заменить (>1, 22>)
    КОНЕЦ ЕСЛИ
    ЕСЛИ нашлось (>2)
      ТО заменить (>2, 2>)
    КОНЕЦ ЕСЛИ
    ЕСЛИ нашлось (>3)
      ТО заменить (>3, 1>)
    КОНЕЦ ЕСЛИ
  КОНЕЦ ПОКА
КОНЕЦ
На вход приведённой ниже программе поступает строка, начинающаяся с символа «>», 
а затем содержащая 11 цифр 1, 12 цифр 2 и 30 цифр 3, расположенных в произвольном 
порядке. Определите сумму числовых значений цифр строки, получившейся в результате 
выполнения программы. Так, например, если результат работы программы представлял бы 
собой строку, состоящую из 50 цифр 4, то верным ответом было бы число 200.
'''
# https://prnt.sc/BF7OUBBJNbfK


s = '>' + 11 * '1' + 12 * '2' + 30 * '3'

while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '22>', 1)
    if '>2' in s:
        s = s.replace('>2', '2>', 1)
    if '>3' in s:
        s = s.replace('>3', '1>', 1)

print(sum(map(int, s[:-1])))
