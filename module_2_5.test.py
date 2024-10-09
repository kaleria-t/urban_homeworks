def get_matrix (n,m,value):
    matrix = []
# на n я должна каждый виток цикла создавать новый список (всего будет n списков), в который потом
# во вложенном цикле буду записывать необходимое количество (m раз) переменных value
    for i in range (n):
        matrix.append([])
        for j in range (m):
            matrix[i].append(value)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
