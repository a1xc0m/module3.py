s = '''Было просто пасмурно, дуло с севера
А к обеду насчитал сто граций серого.
Так всегда первого ноль девятого
То ли весь мир сошел с ума, то ли я - того...
На столе записка от неё смятая
Недопитый виски допивая с матами.
Посмотрю в окно, допишу главу
Первое сентбря, дворник жжёт листву.
Серым облакам наплевать на нас
Если знаешь как жить - живи
Ты хотела плыть как все - так плыви!'''



def decompose(a):
    str = list(a.split(' '))
    str1 = []
    str2 = ['\n', '.', ',', '!', '?', '-']
    for i in range(len(str)):
        if (len(str[i]) < 5) and (str[i] not in str2):
            str1.append(str[i])
    print(str1)


decompose(s)
