def prime(number):
    """Проверка на простоту"""
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True

if prime(int(input())):
    print('True')
else:
    print('False')
