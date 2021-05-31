number = 23
running = True

while running:
    guess = int(input('Введите число: '))

    if guess ==number:
        print('Поздравляю вы угодали!')
        running = False
    elif guess <= number:
        print('Нет, загаданное число больше этого.')
    else:
        print('Нет, загаданное число меньше этого.')
else:
    print('Цикл while закончен.')
print('Завершение.')


