# Uses python3
import numpy as np

def edit_distance(s, t):
    #write your code here
    cost = np.zeros([len(s)+1, len(t)+1])
    cost[0,:] = range(len(t)+1)
    cost[:,0] = range(len(s)+1)
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            if s[i-1] == t[j-1]:
                cost[i,j] = cost[i-1, j-1]
            else:
                cost[i,j] = min((cost[i-1, j], cost[i-1, j-1], cost[i, j-1])) + 1
    # print(cost)
    return cost[-1, -1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
    # print(edit_distance('editing', 'distance'))

