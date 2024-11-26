import re

def process_array_command(command, array):

    command = command.lower()

    pattern1 = r"получить элемент по (\d+) индексу"
    pattern2 = r"получить элементы с (\d+) по (\d+) с шагом (\d+)"
    pattern3 = r"получить (\d+) элемент с конца массива"

    match1 = re.match(pattern1, command)
    match2 = re.match(pattern2, command)
    match3 = re.match(pattern3, command)

    try:
        if match1:
            index = int(match1.group(1))
            if 0 <= index < len(array):
                return array[index]
            else:
                return "Ошибка: индекс вне границ массива"

        elif match2:
            start_index = int(match2.group(1))
            end_index = int(match2.group(2))
            step = int(match2.group(3))
            if 0 <= start_index <= end_index < len(array) and step != 0:
                return array[start_index:end_index + 1:step]
            else:
                return "Ошибка: некорректные индексы или шаг"

        elif match3:
            index = int(match3.group(1))
            if 1 <= index <= len(array):
                return array[-index]
            else:
                return "Ошибка: индекс вне границ массива"

        else:
            return "Ошибка: неверный формат команды"

    except Exception:
        return "Ошибка: произошла непредвиденная ошибка"


if __name__ == "__main__":
    someArray = [10, 20, 30, 40, 50, 100, 34, 24, 167, 4, 1, 45, 99]

    print("Доступные команды:")
    print("- Получить элемент по n индексу (n - номер элемента)")
    print("- Получить элементы с n по b с шагом v (n - начальный индекс, b - конечный индекс, v - шаг)")
    print("- Получить n элемент с конца массива (n - номер элемента с конца)")

    command = input("Введите команду для массива: ")
    result = process_array_command(command, someArray)
    print(result)