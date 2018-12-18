# Uses python3
import sys

def get_fibonacci_last_digit(n):
    if (n <= 1):
        return n
    else:
        fb = [0, 1]
        for i in range(2,n+1):
            fb.append((fb[i-1] + fb[i-2])%10)
        return fb[-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
