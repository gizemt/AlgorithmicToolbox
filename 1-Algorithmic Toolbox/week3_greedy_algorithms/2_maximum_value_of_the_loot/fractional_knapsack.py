# Uses python3
import sys
import numpy as np

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    unit_value = np.array([values[i]*1./weights[i] for i in range(len(values))])
    sorted_idx = np.argsort(unit_value)
    total_weight = 0.
    i = 1
    while total_weight < capacity:
    	item_weight = min(capacity - total_weight, weights[sorted_idx[-i]])
    	value += item_weight*unit_value[sorted_idx[-i]]
    	total_weight += item_weight
    	i+=1
    	print item_weight
    	print total_weight
    	print value

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
