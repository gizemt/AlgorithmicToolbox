# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

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

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    # print(get_fibonacci_huge_naive(n, m))
    print(get_fibonacci_huge(n, m))
