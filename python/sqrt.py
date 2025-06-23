def square (x):
    return x * x

def average(x, y):
    return (x + y) / 2

def improve(guess, x):
    return average(guess, x / guess)

def good_enough(guess, new_guess):
    return abs(new_guess - guess) < (guess * 0.001) 

def sqrt_iter(guess, new_guess, x):
    if good_enough(guess, new_guess):
        return new_guess
    else:
        return sqrt_iter(new_guess, improve(new_guess, x), x) 
    
def sqrt(x):
    return sqrt_iter(0, 1.0, x)

print(sqrt(10000000040000))


