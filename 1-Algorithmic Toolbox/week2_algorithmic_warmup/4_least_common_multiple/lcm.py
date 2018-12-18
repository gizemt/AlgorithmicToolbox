# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd(a, b):
    a0 = min(a,b)
    a1 = max(a,b)
    if a1%a0 == 0:
    	return a0
    else:
    	return gcd(a1%a0, a0)

def lcm(a,b):
	return int(b/gcd(a,b))*a

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

