# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

# Все числа по краям треугольника равны 1, а каждое число внутри треугольника равно
# сумме двух чисел над ним. Напишите процедуру, вычисляющую элементы треуголь-
# ника Паскаля с помощью рекурсивного процесса.

# def pascal_triangle(n): # n - глубина треугольника
#   result = [] # пустой массив для результата
#   for i in range(n): # первый цикл для строчек
#       row = [] # пустой массив для цифр в строке
#       for j in range(i+1): # второй цикл для символов в строке (i+1 потому что колличество символов такое же как и номер строки)
#         if j == 0 or j == i: # если символ первый или последний ставим единицу
#           row.append(1)
#         else:
#           first_parent = result[i-1][j-1] # иначе короче первый родитель это на один вверх и вправо  
#           second_parent = result[i-1][j] # а второй это просто на один вверху

#           row.append(first_parent + second_parent) # добавляем сумму первого и второго родителя и так несколько раз
#       result.append(row) # 
#   return result
    
# triangle = pascal_triangle(5)
# for row in triangle:
#   print(row)

def iterative_pascal_triangle(n: int):
    return iter_rows(n, 0)

def iter_rows(n: int, row_index: int):
    if row_index == n:
        return
    # Печать новой строки перед началом вычисления следующей строки
    if row_index > 0:
        print()
    iter_columns(row_index, 0)
    iter_rows(n, row_index + 1)

def iter_columns(row_index: int, col_index: int):
    if col_index > row_index:
        return
    elif col_index == 0 or col_index == row_index:
        # Крайние элементы строки — всегда 1
        print(1, end=" ")
    else:
        # Рекурсивное вычисление элемента внутри строки
        value = (get_pascal_value(row_index - 1, col_index - 1) +
                 get_pascal_value(row_index - 1, col_index))
        print(value, end=" ")
    # Переход к следующему столбцу
    iter_columns(row_index, col_index + 1)

def get_pascal_value(row_index: int, col_index: int):
    # Вычисление значения элемента через древовидную рекурсию
    if col_index == 0 or col_index == row_index:
        return 1
    return (get_pascal_value(row_index - 1, col_index - 1) +
            get_pascal_value(row_index - 1, col_index))

# Тестирование
iterative_pascal_triangle(5)
