def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = input('Введите текст: ')
if (is_palindrome(something)):
    print('Да, это полиндром.')
else:
    print('Нет, это не полиндром.')