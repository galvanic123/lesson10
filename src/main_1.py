def clear_names(file_name: str) -> list:
    """Функция для очистки имён от лишних символов"""
    new_names_list = list()
    with open('data/' + file_name) as names_file:
        names_list = names_file.read().split()
        for name_items in names_list:
            new_name = ''
            for symbol in name_items:
                if symbol.isalpha():
                    new_name +=symbol
            if new_name.isalpha():
                new_names_list.append(new_name)
    return new_names_list

def is_cyrillic(name_item):
    """Проверка на вхождение кириллицы в строку"""
def filter_russian_names(names_list: list) -> list:
    """Фильтрация имён, написанных на русском"""
    new_names_list = list()

if __name__ == '__main_1__':
    cleared_name = clear_names('names.txt')

    for i in cleared_name:
        print(i)

