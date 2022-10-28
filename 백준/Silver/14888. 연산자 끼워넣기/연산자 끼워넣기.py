import sys
input = sys.stdin.readline

# 수열 길이
n = int(input())

# 수열 입력
num = list(map(int, input().split()))

# +, -, x, %
op = list(map(int, input().split()))

# 최대값, 최소값 초기화
maximum = -int(1e9)
minimum = int(1e9)

def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum

    # n번 연산하면 종료
    if depth == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    # 계산할 수 있는 연산자가 남아있는지 확인
    # 중간 계산 값에 연산 결과를 누적해나감
    if plus != 0:
        dfs(depth+1, total+num[depth], plus-1, minus, multiply, divide)
    if minus != 0:
        dfs(depth+1, total-num[depth], plus, minus-1, multiply, divide)
    if multiply != 0:
        dfs(depth+1, total*num[depth], plus, minus, multiply-1, divide)
    if divide != 0:
        dfs(depth+1, int(total/num[depth]), plus, minus, multiply, divide-1)

dfs(1, num[0], op[0], op[1], op[2], op[3])

# 만들 수 있는 최대값, 최소값 출력
print(maximum)
print(minimum)