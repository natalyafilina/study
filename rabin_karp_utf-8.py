t = """Вместе шли они в сраженья через минные поля,
на узлах сопротивленья славу поровну деля.
Не страшили дождь и ночь их, и немало огневых
подавили они точек, не считая запятых.
Воевала дело зная та четверка храбрецов -
Иваненко, Иванбаев, Иванидзе, Иванов."""
p = "Иван"

# t = "pppppp"
# p = "pp"


def find_all_rabin_karp(text, pattern):
    """
    Поиск всех вхождений алгоритмом Рабина-Карпа
    """
    result = []
    patternsum = sum(ord(s) for s in pattern)
    textwindowsum = sum(ord(text[i]) for i in range(len(pattern)))
    if text.startswith(pattern, 0):
        result.append(0)
    for i in range(len(text) - len(pattern)):
        textwindowsum += ord(text[i + len(pattern)]) - ord(text[i])
        if textwindowsum == patternsum:
            if text.startswith(pattern, i + 1):
                result.append(i + 1)
    return result

print(find_all_rabin_karp(t, p))
