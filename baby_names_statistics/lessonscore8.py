names = [

'Саша','Саша','Саша','Коля','Миша','Саша','Света','Никита','Миша',

'Валера','Валера','Юля','Юля','Саша','Саша','Саша','Оля','Юля','Саша','Оля','Петя',

'Петя','Юля','Антон','Антон','Маша','Гоша','Оля','Юля','Гоша','Оля','Юля'
 ]



res = {}
for name in names:
     res [name] = res.get(name,0) + 1
for i,x in sorted(sorted(res.items()), key = lambda x :
x[1],reverse = True):
    print(i,x)
