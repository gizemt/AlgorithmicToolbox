# Uses python3
import sys
import math
def optimal_summands(n):
    summands = []
    #write your code here
    if n < 3:
    	summands = [n]
    else:
    	k = math.floor(math.sqrt(2*n + 0.25) - 0.5)
    	summands = [x for x in range(1, k)]
    	summands.append(n - int(k*(k - 1)/2))
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
