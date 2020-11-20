def prime(number):
    """Проверка на простоту"""
    i = 2
    while i * i <= number:
        if number % i == 0:
            return 0
        i += 1
    return 1

if prime(int(input())):
    print('YES')
else:
    print('NO')
