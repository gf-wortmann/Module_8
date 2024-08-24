# Домашнее задание по теме "Сложные моменты и исключения в стеке вызовов функции".

def personal_sum(numbers):
    result = 0
    incorrect_data_count = 0
    for number in numbers:
        try:
            result += number
        except TypeError as e:
            incorrect_data_count += 1
            print(f'Некорректный тип данных для подсчёта суммы - {number}')

    return result, incorrect_data_count


def calculate_average(numbers):
    try:
        summ, incorrect_entries = personal_sum(numbers)
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return
    try:
        average_value = summ / (len(numbers) - incorrect_entries)
    except ZeroDivisionError:
        average_value = 0
    return average_value


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
