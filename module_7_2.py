def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    string_positions = {}
    n = 0
    for i in strings:
        n += 1
        first_str_byte = file.tell()
        file.write(i+'\n')
        tuple_ = (n, first_str_byte)
        string_positions[tuple_] = i
    file.close()
    return dict(string_positions)

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)



