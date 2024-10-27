data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def sum_ (a):
    s = 0
    if isinstance(a, int) or isinstance(a, float):
        s += a
    elif isinstance(a, str):
        s += len(a)
    elif isinstance(a, set) or isinstance(a, tuple) or isinstance(a, list):
        for elem in a:
            s += sum_(elem)
    elif isinstance(a, dict):
        for i, k in a.items():
            s += sum_(i)
            s += sum_(k)
    return s
print (sum_(data_structure))




#result = calculate_structure_sum(data_structure)
#print(result)
