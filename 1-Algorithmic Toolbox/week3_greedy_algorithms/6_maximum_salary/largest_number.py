#Uses python3

import sys

def largest_number(a):
    #write your code here
    res = ""
    while len(a) > 0:
        x_max = str(0)
        for x in a:
            if int(x[0]) > int(x_max[0]):
                x_max = x
            elif int(x[0]) == int(x_max[0]):
                sm = x + x_max
                ms = x_max + x
                if int(sm[:max(len(x), len(x_max))]) > int(ms[:max(len(x), len(x_max))]):
                    x_max = x
        res += x_max
        a.remove(x_max)
    return int(res)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))