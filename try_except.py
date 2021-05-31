try:
    text = input('Введите что-нибудь-->')
except EOFError:
    print('Ну зачем вы зделали мне EOF?')
except KeyboardInterrupt:
    print('Вы отменили операцию.')
else:
    print('Вы ввели {0}'.format(text))
