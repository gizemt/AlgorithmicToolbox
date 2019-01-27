# Uses python3
import sys

def get_change(m):
    #write your code here
    c = [0] * (m + 1)

    for i in range(1, m + 1):
        if i < 3:
            c[i] = c[i-1] + 1
        elif i < 4:
            c[i] = min(c[i-1], c[i-3]) + 1
        else:
            c[i] = min((c[i-1], c[i-3], c[i-4])) + 1
    return c[m]

if __name__ == '__main__':
    m = 34 #int(sys.stdin.read())
    print(get_change(m))
