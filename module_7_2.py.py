import io
from pprint import pprint


def custom_write(file_name, strings):
    strings_positions = {}

    # Открываем файл для записи
    with open(file_name, 'w', encoding='utf-8') as file:
        for index, line in enumerate(strings, start=1):
            # Получаем текущую позицию в байтах перед записью строки
            byte_position = file.tell()
            # Записываем строку в файл, добавляя перевод строки
            file.write(line + '\n')
            # Сохраняем позицию и строку в словаре
            strings_positions[(index, byte_position)] = line

    return strings_positions


# Пример выполняемого кода
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

# Выводим полученный результат
for elem in result.items():
    print(elem)