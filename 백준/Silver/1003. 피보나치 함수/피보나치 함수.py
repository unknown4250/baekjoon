import sys
input = sys.stdin.readline

n = int(input())

def fibonacci(n):
    nums[0], nums[1] = [1,0], [0, 1]

    if n >= 2:
        for i in range(2, n+1):
            zero = nums[i-1][0] + nums[i-2][0]
            one = nums[i-1][1] + nums[i-2][1]
            nums[i] = [zero, one]
    return nums[n]

for _ in range(n):
    num = int(input())
    nums = [[0,0]] * 101
    res = fibonacci(num)
    print(res[0], res[1])
