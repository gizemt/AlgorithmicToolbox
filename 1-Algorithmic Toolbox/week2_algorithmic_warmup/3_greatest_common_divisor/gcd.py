# Uses python3
import sys

# def gcd_naive(a, b):
#     current_gcd = 1
#     for d in range(2, min(a, b) + 1):
#         if a % d == 0 and b % d == 0:
#             if d > current_gcd:
#                 current_gcd = d

#     return current_gcd

def gcd(a, b):
    a0 = min(a,b)
    a1 = max(a,b)
    if a1%a0 == 0:
    	return a0
    else:
    	return gcd(a1%a0, a0)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    # print(gcd_naive(a, b))
    print(gcd(a, b))
