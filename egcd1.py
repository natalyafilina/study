def egcd(cort):
    """Расширенный алгоритм Евклида"""
    if cort[0] == 0:
        return cort[1], cort[2], cort[3]
    nod0, coefx1, coefy1 = egcd((cort[1] % cort[0], cort[0], cort[2], cort[3]))
    coefx0 = coefy1 - (cort[1] // cort[0]) * coefx1
    coefy0 = coefx1
    return nod0, coefx0, coefy0

def result(first, second):
    nod, coefx, coefy = egcd((int(first), int(second), 0, 1))
    my_string = str(nod) + ' = ' + first + ' * ' + str(coefx) + ' + ' + second + ' * ' + str(coefy)
    return my_string

