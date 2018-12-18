# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

# Gizem
def get_fibonacci_mod(m):
    if (m == 0):
        return m
    elif m == 1:
        return [0, 1] 
    else:
        fb = [0, 1]
        while len(fb)==2 or not (fb[-1] == 1 and fb[-2] == 0):
            fb.append((fb[-1] + fb[-2])%m)
        return fb[:-2]

def get_fibonacci_huge(n, m):
    fb_mod_array = get_fibonacci_mod(m)
    return fb_mod_array[n%(len(fb_mod_array))]

def fibonacci_sum_squares(n):
    return (get_fibonacci_huge(n, 10)*get_fibonacci_huge(n+1, 10))%10

if __name__ == '__main__':
    n = int(stdin.read())
    # print(fibonacci_sum_squares_naive(n))
    print(fibonacci_sum_squares(n))
