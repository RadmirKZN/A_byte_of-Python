x = 50
def func():
    global x

    print('x =', x)
    x = 2
    print('Заменяем глобальное значение  х на', x)

func()
print(' Значение x  составляет', x)
