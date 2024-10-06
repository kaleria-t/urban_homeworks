first = int(input('ведите первое число: '))
second = int(input('ведите второе число: '))
third = int(input('ведите третье число: '))
if first == second == third:
    print (3)
elif first == second or first == third or second == third:
    print (2)
else:
    print('нет совпадений')