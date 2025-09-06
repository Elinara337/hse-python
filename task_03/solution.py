# Задание 3: Строки и операции со строками
# Реализуйте функции для работы со строками


def string_length(s):
    """
    Возвращает длину строки
    """
    return len(s)
    pass


def string_concatenation(s1, s2):
    """
    Соединяет две строки
    """
    return s1 + s2
    pass


def string_to_uppercase(s):
    """
    Преобразует строку к верхнему регистру
    """
    return s.upper()
    pass


def string_to_lowercase(s):
    """
    Преобразует строку к нижнему регистру
    """
    return s.lower()
    pass


def string_replace(s, old, new):
    """
    Заменяет в строке s все вхождения подстроки old на new
    """
    return s.replace(old, new)
    pass


def string_split(s, delimiter):
    """
    Разбивает строку по указанному разделителю
    """
    if delimiter == '':
        return list(s)
    return s.split(delimiter)
    pass


def string_strip(s):
    """
    Удаляет начальные и конечные пробелы из строки
    """
    return s.strip()
    pass


def is_palindrome(s):
    """
    Проверяет, является ли строка палиндромом
    (читается одинаково слева направо и справа налево)
    Регистр и пробелы не учитываются
    """
    lower_strip_s = s.lower().replace(' ', '')
    return lower_strip_s[::-1] == lower_strip_s
    pass
