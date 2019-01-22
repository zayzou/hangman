import os


def file_exist(file_path):
    return os.path.exists(file_path)


def write_file(file_path, content):
    with open(file_path, 'w') as file_handler:
        file_handler.write(content)


def read_file(file_path):
    if file_exist(file_path):
        with open(file_path, 'r') as file_handler:
            data = file_handler.read()
            return data
    else:
        print(f'{file_path} does not exist')
        return ''


def line_count(file_path):
    with open(file_path) as file_handler:
        nbr_of_lines = sum(1 for line in file_handler)
        file_handler.close()
        return nbr_of_lines


def running_counter():
    PATH = 'data/count.txt'
    number = 0
    if not file_exist(PATH):
        number += 1
        write_file(PATH, str(number))
    else:
        number = int(read_file(PATH))
        number += 1
        write_file(PATH, str(number))
    print(f'the programme is running for the {number} time')


def read_line_with_index(file_path, index):
    if not file_exist(file_path):
        print('file not found ')
        return 0
    file = open(file_path, 'r')
    i = 0
    while index != i:
        line = file.readline()
        i += 1
    return line
