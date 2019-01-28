# Uses python3
import sys
import itertools
import numpy as np

def naive_partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0

def partition3(A):
    s = np.sum(A)
    print(s/3)
    if s%3 != 0:
        return 0
    else:
        s3 = int(s/3)
        P = np.zeros([len(A), s3+1, s3+1])
        P[:, 0, 0] = 1
        for i in range(1, len(A)):
            P[i, A[i-1], 0] = 1
            P[i, 0, A[i-1]] = 1
        for i in range(1, len(A)):
            for f1 in range(1, s3+1):
                for f2 in range(1, s3+1):
                        p = [0]
                        if f1 - A[i] >= 0:
                            p.append(P[i-1, f1 - A[i], f2])
                        if f2 - A[i] >= 0:
                            p.append(P[i-1, f1, f2 - A[i]])
                            p.append(P[i-1, f1, f2])
                        P[i, f1, f2] = np.sum(p) > 0
        # print(P)
        return P[-1, -1, -1]

if __name__ == '__main__':
    #input = sys.stdin.read()
    n, *A = [13, 1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]# [11, 17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]#list(map(int, input.split()))
    print(partition3(A))


