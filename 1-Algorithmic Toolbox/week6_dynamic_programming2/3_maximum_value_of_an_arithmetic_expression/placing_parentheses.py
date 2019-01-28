import numpy as np
# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    #write your code here
    nums = [int(n) for n in dataset[0::2]]
    Amax = np.ones([len(nums), len(nums)])*-10000
    Amin = np.ones([len(nums), len(nums)])*10000
    Amax[np.diag_indices(len(nums))] = nums
    Amin[np.diag_indices(len(nums))] = nums
    
    for d in range(1, len(nums)):
        for i in range(len(nums) - d): 
            j = i + d
            for ii in range(i, j):
                xx = evalt(Amax[i,ii], Amax[ii+1,j], dataset[2*ii + 1])
                nx = evalt(Amin[i,ii], Amax[ii+1,j], dataset[2*ii + 1])
                xn = evalt(Amax[i,ii], Amin[ii+1,j], dataset[2*ii + 1])
                nn = evalt(Amin[i,ii], Amin[ii+1,j], dataset[2*ii + 1])
                if Amax[i,j] < max([xx, nx, xn, nn]):
                    Amax[i,j] = max([xx, nx, xn, nn])
                if Amin[i,j] > min([xx, nx, xn, nn]):
                    Amin[i,j] = min([xx, nx, xn, nn])
            
    # print(Amax)
    # print(Amin)
    return Amax[0,-1]

 
if __name__ == "__main__":
    # print(get_maximum_value(input()))
    print(get_maximum_value('5-8+7*4-8+9'))

