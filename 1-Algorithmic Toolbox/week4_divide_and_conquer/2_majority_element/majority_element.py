# Uses python3
import sys
import numpy as np

def get_majority_element(a, left, right):
    a_sorted = np.sort(a)
    n_maj = n//2
    flag = -1
    for i in range(len(a)-n_maj):
        if a_sorted[i] == a_sorted[i+n_maj]:
            flag = 1
    return flag

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
