calls = 0
#def count_calls(): # не понимаю, зачем нужна функция, когда считаю кол-во вызовов через перемееную calls
def string_info(string_):
    global calls
    print(str((len(string_), string_.upper(), string_.lower())))
    calls += 1
def is_contains(string_, list_to_search):
    global calls
    calls += 1
    if string_.lower() in str(list_to_search).lower():
        print(True)
    else:
        print(False)
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)