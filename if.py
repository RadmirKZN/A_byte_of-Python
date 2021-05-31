#!/home/radmir/PycharmProjects/pythonProject1/if.py
number = 23
guess = int(input('Введите число:'))
if guess == number:
    print('Пздравляю! Вы угадали!')
    print('Хотя и не выйграли, никакого приза.')
elif guess < number:
    print('Нет. Загаданное число больше, этого.')
else:
    guess > number
    print('Загаданное число меньше этого.')
print('Завершено.')
