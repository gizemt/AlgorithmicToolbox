# Uses python3
import sys

def get_change(m):
    #write your code here
    n10 = int(m/10)
    n5 = int((m - n10*10)/5)
    n1 = (m - n10*10 - n5*5)
    return n10 + n5 + n1

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
