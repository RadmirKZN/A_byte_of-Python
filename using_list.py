shoplist = ['яблоки', 'манго',' морковь', 'бананы']

print('Я должен ', len(shoplist),'покупки.')

print('Покупки:', end = ' ')
for item in shoplist:
    print(item, end = ' ')

print('\nТакже нужно купить риса.')
shoplist.append('рис')
print('Теперь мой список покупок таков:', shoplist)

print('Отсортирую-ка я свой спписок')
shoplist.sort()
print('Отсортированный список покупок выглядет так:', shoplist)

print('Первое, что мне нужно купить, это:', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('Я купил', olditem)
print('Теперь мой список покупок:', shoplist)