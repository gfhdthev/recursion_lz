def pascal_triangle(n):
    if n == 1:  #если аргумент 1, то возвращаем 1
        return [[1]]
    triangle = pascal_triangle(n - 1)
    last_row = triangle[-1]  #последняя строка из предыдущего треугольника
    new_row = [1] + [last_row[i - 1] + last_row[i] for i in range(1, len(last_row))] + [1] #перебираем пары и добавляем по крайм 1
    return triangle + [new_row]  #возвращаем новый треугольник

first = int(input('Введите сколько строчек треугольника Паскаля вывести:'))

print(pascal_triangle(2))