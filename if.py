def que_hacer(edad):
    if edad < 7:
        return 'Детский сад'
    elif edad < 18:
        return 'Школа'
    elif edad < 22:
        return 'ВУЗ'
    else: return 'Работа'

edad = input('Введите ваш возраст: ')
r = que_hacer(int(edad))
print(r)
#-----------------------------------
def igual(str1,str2):
    if not type(str1) is str or not type(str2) is str: return 0
    elif str1 == str2: return 1
    elif str1 != str2 and len(str1) > len(str2): return 2
    elif str1 != str2 and str2 == 'learn': return 3
    else: return 4
r = igual('один', 3)
print(r)    
r = igual('один', 'один')
print(r)
r = igual('один', 'два')
print(r)
r = igual('один', 'learn')
print(r)