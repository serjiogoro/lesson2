l = []
for i in range(10): l.append(i)
for n in l:
    print(n+1)
#------------------------------------
s = input('Введите строку: ')
for c in s:
    print(c)
#------------------------------------
sts = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '4a', 'scores': [3,4,2,5,2]},
    {'school_class': '4a', 'scores': [3,3,4,5,2]},
    {'school_class': '4b', 'scores': [3,4,4,5,3]},
    {'school_class': '4b', 'scores': [4,4,3,5,2]},
    {'school_class': '4c', 'scores': [3,4,5,5,5]},
    {'school_class': '4c', 'scores': [3,4,2,3,2]},
]
cl = {'school_class': '', 'scores': 0, 'cnt':0}
cl_list = []
cn = 0
sc = 0
for st in sts:
    if st['school_class'] not in cl_list:
        cl_list.append(st['school_class'])
    for s in st['scores']:
        cn += 1
        sc += s
print(f'Средняя оценка в школе: {sc/cn}')
cn = 0
sc = 0
for c in cl_list:
    for st in sts:
        if st['school_class'] == c:
            for s in st['scores']:
                cn += 1
                sc += s
    print(f'Средняя оценка в {c} классе: {sc/cn}')
    cn = 0
    sc = 0