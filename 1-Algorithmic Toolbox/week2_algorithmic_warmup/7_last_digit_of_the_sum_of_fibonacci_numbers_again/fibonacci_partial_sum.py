# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

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

def fibonacci_partial_sum(from_, to):
    return (fibonacci_sum_last_digit(to)-fibonacci_sum_last_digit(from_-1))%10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    # print(fibonacci_partial_sum_naive(from_, to))
    print(fibonacci_partial_sum(from_, to))

