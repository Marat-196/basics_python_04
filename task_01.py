# 1. Напишите функцию для транспонирования матрицы


def transp_matrix(mtrx):
    my_list = list()
    row = len(my_mtrx)
    col = len(my_mtrx[0])
    for i in range(col):
        lst = list()
        for j in range(row):
            lst.append(my_mtrx[j][i])
        my_list.append(lst)
    return my_list


my_mtrx = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('Начальная матрица')
for i in my_mtrx:
    print(*i)
result = transp_matrix(my_mtrx)
print('-' * 15)
print('Транспонированная матрица')
for i in result:
    print(*i)

my_mtrx = [[1, 2, 3], [101, 102, 103], [201, 202, 203], [301, 302, 303], [401, 402, 403]]
print('Начальная матрица')
for i in my_mtrx:
    print(*i)
result = transp_matrix(my_mtrx)
print('-' * 15)
print('Транспонированная матрица')
for i in result:
    print(*i)
