# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max1 = max(numbers)
    max2 = 0
    idx_max1 = numbers.index(max1)
    for i in range(n):
        if i != idx_max1:
            max2 = max(max2, numbers[i])

    return max1*max2


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
