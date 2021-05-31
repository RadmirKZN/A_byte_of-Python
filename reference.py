print('Простое присвоение')
shoplist = ['яблок', 'манго', 'морковь','бананы']
mylist = shoplist #Ещё одно имя, указывающее на тот же обект!

del shoplist[0]

print('shoplist:', shoplist)
print('mylist:', mylist)

print('Копирование при поиощи полной вырезки')
mylist = shoplist[:]
del mylist[0]

print('shoplist:', shoplist)
print('myself:', mylist)
