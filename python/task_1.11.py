# если n < 3: f (n) = n
# если n ≥ 3: f (n) = f (n−1) + f (n−2) + f (n − 3)

def f_iter(a, b, c, count):
    if count < 3:
        return c
    else:
        return f_iter(b, c, a + b + c, count - 1)
    
def iterative_f(n):
    return f_iter(0, 1, 2, n)

print(iterative_f(10))
