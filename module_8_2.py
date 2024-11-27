def add_everything_up(a, b):
    summator = None

    try:
        summator = a+b

    except TypeError:
        summator = (str(a)+str(b))

    finally:
        return summator

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))