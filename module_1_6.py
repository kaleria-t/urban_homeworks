my_dict = {'Ivan': 19997, 'Oleg': 2005, 'Marta': 1999, 'Sasha': 2012}
print (my_dict)
print (my_dict['Oleg'])
print (my_dict.get('Sonya'))
my_dict.update({'Igor': 1990, 'Masha': 2002})
a = my_dict.pop('Marta')
print (a)
print(my_dict)

my_set = {34, 45, 56, 'apple', False, True, 45, True, 'apple', 'orange', 'berry'}
print(set(my_set))
my_set.add(2) #правильно понимаю, что в списки нельзя добавлять более 1го элемента за раз?
my_set.add(100)
print(my_set)

