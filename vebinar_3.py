def f():
    calls = 0
    def wrapper():
        nonlocal calls
        calls += 1
        return calls
    return wrapper

print(f())

count_calls = f()
o = count_calls

print(count_calls(), '- кол-во вызовов функции после print(count_calls())')
print ('Вывод: вызов исходной функции f() не изменяет счётчик calls')
print(count_calls(), '- кол-во вызовов функции после повторения print(count_calls())')
print ('Вывод: вызов "count_calls()" изменяет счётчик')
print(o is count_calls, ' - о является count_calls')
print (o, ' - вызов функции print(о)')
print(count_calls(), 'вызовов функции после print(o) и print(count_calls())')
print ('Вывод: вызов "о" не изменяет счётчик')
print(o(), '- кол-во вызовов функции после print(о())')
print('Вывод: вызов "о()" изменяет счётчик')
print(f(), 'вызов "f()" по прежнему не изменяет счётчик')
print(count_calls())

def num():
    a = 2
    def plus():
        nonlocal a
        a+=10
        return a
    return plus()
print (num)
a_num = num()
print(a_num)