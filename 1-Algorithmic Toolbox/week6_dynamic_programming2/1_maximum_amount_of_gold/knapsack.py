# Uses python3
import sys
import numpy as np

def greedy_optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result
def optimal_weight(W, n):
    val = np.zeros([len(n)+1, W+1])

    for i in range(1, len(n)+1):
        wi = n[i-1]
        for w in range(1, W+1):
            if w >= wi:
                val[i,w] = max([val[i - 1, w - wi] + wi, val[i-1, w]])
            else:
                val[i, w] = val[i-1, w]
    return val[-1, -1]
        
    
if __name__ == '__main__':
    # input = sys.stdin.read()
    W, n, *w = [10, 3, 1, 4, 8]# list(map(int, input.split()))
    print(optimal_weight(W, w))