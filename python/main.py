def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fib_iter(a, b, count):
    if count == 0:
        return b
    else:
        return fib_iter(a + b, a, count - 1)
    
def iterative_fib(n):
    return fib_iter(1, 0, n)

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


int_sum = 0
for i in range(1, 101):
    int_sum += i

def get_total(number: int) -> int:
    if (number == 1): return 1
    return number + get_total(number - 1)
