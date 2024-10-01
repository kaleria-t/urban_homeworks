immutable_var = 'sun', True, 14, 411
print (immutable_var)
#immutable_var[3] = 114 #попыталась изменить элемент кортежа. Нельзя изменить элементы кортежа, тк кортеж - неизменяемая коллекция
print (immutable_var)
mutable_list = [8, 3, 'moon', (2, 3, 4)]
mutable_list[0] = 'apple'
mutable_list[3] = [False, 234]
print (mutable_list)