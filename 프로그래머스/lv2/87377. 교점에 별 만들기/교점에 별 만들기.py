from itertools import combinations

def intersection_points(line1, line2):
    a, b, e = line1
    c, d, f = line2

    # 두 직선이 평행하거나 일치하는 경우(AD-BC=0)
    if a * d - b * c == 0:
        return

    # x, y 좌표
    x = (b * f - e * d) / (a * d - b * c)
    y = (e * c - a * f) / (a * d - b * c)

    # 교점이 정수가 아니면 제외
    if x == int(x) and y == int(y):
        # 정수형으로 리턴
        return (int(x), int(y))

def solution(line):
    answer = []
    point_list = []
    x_points, y_points = set(), set()

    # 두 선의 조합에서 교점이 발생하는지 확인
    for line1, line2 in combinations(line, 2):
        point = intersection_points(line1, line2)

        # 교점이 존재하지 않거나 이미 있는 교점이라면 제외
        if not point or point in point_list:
            continue

        # 두 직선의 교점 저장
        point_list.append(point)
        x_points.add(point[0])
        y_points.add(point[1])

    # x, y 좌표의 최소값과 최대값
    min_x, min_y = min(x_points), min(y_points)
    max_x, max_y = max(x_points), max(y_points)

    # 별의 크기(가로x세로)만큼만 '.'으로 초기화
    answer = [['.'] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
    
    # 교점에 * 그리기
    for x, y in point_list:
        answer[max_y-y][x-min_x] = '*'

    return [''.join(ans) for ans in answer]