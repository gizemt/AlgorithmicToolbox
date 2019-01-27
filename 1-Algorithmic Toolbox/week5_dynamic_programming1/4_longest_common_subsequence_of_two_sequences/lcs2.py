#Uses python3

import sys
import numpy as np

def lcs2(a, b):
    #write your code here
    lcs = np.zeros([len(a)+1, len(b)+1])
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                lcs[i, j] = lcs[i-1, j-1] + 1
            else:
                lcs[i, j] = max(lcs[i, j-1], lcs[i-1, j])

    return lcs[-1,-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))

