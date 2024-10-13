def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params('apple', 35) # работает с 0-3 параметрами
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['cat', 71, [4,14]]
values_dict = {'a': 32, 'b': 'tekst', 'c': [-7, 15]}
print_params(*values_list, **values_dict)

values_list_2 = [59, 'sun']
print_params(*values_list_2, 42) # работает