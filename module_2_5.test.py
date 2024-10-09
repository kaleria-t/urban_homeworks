def get_matrix (n,m,value):
    matrix = []
# на n я должна каждый виток цикла создавать новый список (всего будет n списков), в который потом
# во вложенном цикле буду записывать необходимое количество (m раз) переменных value
    for i in range (n):
        matrix.append([])
        for j in range (m):
            matrix[i].append(value)
    return matrix
matrix = get_matrix(3,5,1)
print(*matrix)

