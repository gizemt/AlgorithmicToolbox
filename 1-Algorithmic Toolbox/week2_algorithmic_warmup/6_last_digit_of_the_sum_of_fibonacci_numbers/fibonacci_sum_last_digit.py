# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

# Gizem
def get_fibonacci_mod(m):
    if (m == 0):
        return m, 0
    elif m == 1:
        return [0, 1], [0, 1] 
    else:
        fb = [0, 1]
        cumsum = [0, 1]
        while len(fb)==2 or not (fb[-1] == 1 and fb[-2] == 0):
            fb.append((fb[-1] + fb[-2])%m)
            cumsum.append((cumsum[-1]+fb[-1])%m)
        return fb[:-2], cumsum[:-2]

def fibonacci_sum_last_digit(n):
    fb_mod_array, cumsum_array = get_fibonacci_mod(10)
    return ((cumsum_array[-1])*int(n/(len(fb_mod_array))) + cumsum_array[n%(len(fb_mod_array))])%10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    # print(fibonacci_sum_naive(n))
    print(fibonacci_sum_last_digit(n))
