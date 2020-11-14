def gcd (first, second):
    if second == 0:
        return first
    return gcd(second, first % second)


print(gcd(int(input()), int(input())))
