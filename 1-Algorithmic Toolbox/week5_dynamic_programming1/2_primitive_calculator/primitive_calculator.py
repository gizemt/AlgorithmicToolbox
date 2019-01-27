# Uses python3
import sys
import numpy as np

def greedy_optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def optimal_sequence(N):
    
    seq = [0] * (N+1)
    seq[1] = 1
    cost = [0] * (N+1)
    
    for n in range(2, N+1):
        temp_cost = []
        temp_seq = []

        if n % 2 == 0:
            temp_cost.append(cost[n // 2] + 1)
            temp_seq.append(n // 2)
        if n % 3 == 0:
            temp_cost.append(cost[n // 3] + 1)
            temp_seq.append(n // 3)
        if n - 1 > 0:
            temp_cost.append(cost[n - 1] + 1)
            temp_seq.append(n - 1)
    
        cost[n] = min(temp_cost)
        seq[n] = temp_seq[np.argmin(temp_cost)]
    # print(cost)
    # print(seq)
    
    m = N
    sequence = [m]
    while 1:
        ts = seq[m]
        sequence.append(ts)
        m = ts
        if m == 1:
            break;
    return reversed(sequence)


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
