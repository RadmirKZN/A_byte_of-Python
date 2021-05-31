class ShorInputExeption(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Введите что нибудь-->')
    if len(text) < 3:
        raise ShorInputExeption(len(text), 3)

except EOFError:
    print('Ну зачем вы сделали мне EOF?')
except ShorInputExeption as ex:
    print('ShortInputExeption: Длина введённой стоки -- {0}; \
   ожидалось, как минимум, {1}'.format(ex.length, ex.atleats))
else:
    print('Не было исключений.')