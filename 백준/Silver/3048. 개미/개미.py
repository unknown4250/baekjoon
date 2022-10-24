from sys import stdin
input = stdin.readline

n1, n2 = map(int, input().split())

group1 = [ch for ch in input().strip()]
group2 = [ch for ch in input().strip()]

t = int(input())

# 첫 번째 그룹은 입력과 반대로 움직임
group1 = group1[::-1]

# 결과 배열 초기화(t=0인 경우의 결과를 생각하면 됨)
result = group1 + group2

# t초 동안 반복
while t > 0:
    for i in range(len(result)-1):
        # 맞닿은 두 개미의 그룹이 다르다면 위치를 서로 변경
        if result[i] in group1 and result[i+1] in group2:
            result[i], result[i+1] = result[i+1], result[i]

            # 위치를 바꾼 개미가 첫 번째 그룹의 선두라면 이동 종료
            if result[i+1] == group1[-1]:
                break
    t -= 1

print("".join(result))
