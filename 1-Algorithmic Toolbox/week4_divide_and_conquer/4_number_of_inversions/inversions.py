# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        # if a[left] > a[right]:
        #    number_of_inversions += 1
        #    b[left], b[right] = a[right], a[left]
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    # print(' ')
    #write your code here
    i = left
    j = ave
    ib = left
    while i < ave and j < right:
        l = a[i]
        r = a[j]
        if l <= r:
            b[ib] = l
            i += 1
        else:
            j += 1
            b[ib] = r
            number_of_inversions += 1
        ib += 1
        # print(b, i, j, left, ave, right)
    if i >= ave:
        b[ib:right] = a[j:right]
    if j >= right:
        b[ib:right] = a[i:ave]
    a[left:right] = b[left:right]
                
    # number_of_inversions += (num_left + num_right)
    return number_of_inversions

if __name__ == '__main__':
    # input = sys.stdin.read()
    n, *a = [5, 2, 3, 9, 2, 9]# list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
