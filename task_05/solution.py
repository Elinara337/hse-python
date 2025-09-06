# Задание 5: Циклы (for)
# Реализуйте функции с использованием цикла for


def sum_of_numbers(n):
    """
    Возвращает сумму чисел от 1 до n включительно
    """
    ans = 0
    for i in range(1, n + 1):
        ans += i
    return ans
    pass


def factorial(n):
    """
    Возвращает факториал числа n (произведение чисел от 1 до n)
    Для n <= 1 возвращает 1
    """
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans
    pass


def count_vowels(s):
    """
    Возвращает количество гласных букв в строке s
    Гласные: 'a', 'e', 'i', 'o', 'u' (регистр не имеет значения)
    """
    ans = 0
    s = s.lower()

    for c in s:
        if c in ['a', 'e', 'i', 'o', 'u']:
            ans += 1

    return ans
    pass


def find_max(numbers):
    """
    Возвращает максимальное число из списка numbers
    Если список пуст, возвращает None
    """
    if len(numbers) == 0:
        return None

    max_num = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > max_num:
            max_num = numbers[i]
            
    return max_num
    pass


def filter_even_numbers(numbers):
    """
    Возвращает новый список, содержащий только четные числа из списка numbers
    """
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
    pass


def generate_multiplication_table(n):
    """
    Возвращает таблицу умножения размером n x n в виде списка списков
    Например, для n=3 результат должен быть:
    [
        [1, 2, 3],
        [2, 4, 6],
        [3, 6, 9]
    ]
    """
    table = []

    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        table.append(row)

    return table
    pass
