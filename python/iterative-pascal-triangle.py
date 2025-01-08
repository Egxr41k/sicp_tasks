def iterative_pascal_triangle(n: int) -> list[list[int]]:
  return iter_rows(n, 0, [])

def iter_rows(n: int, row_index: int, result: list[list[int]]) -> list[list[int]]:
  if (row_index == n):
    return result
  result.append(iter_columns(row_index, 0, result))
  return iter_rows(n, row_index + 1, result)
     
def iter_columns(row_index: int, col_index: int, result: list[list[int]]) -> list[int]:
    if col_index > row_index:
        return []
    elif col_index == 0 or col_index == row_index:
      return [1] + iter_columns(row_index, col_index + 1, result)
    else:
      first_parent = result[row_index-1][col_index-1]
      second_parent = result[row_index-1][col_index]

      return [first_parent + second_parent] + iter_columns(row_index, col_index + 1, result)
    
triangle = iterative_pascal_triangle(5)
for row in triangle:
    print(" ".join(f"{num:4}" for num in row))