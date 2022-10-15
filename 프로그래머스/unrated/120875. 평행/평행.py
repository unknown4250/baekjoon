def solution(dots):
    dots.sort()

    first_x = dots[0][0]
    first_y = dots[0][1]

    second_x = dots[1][0]
    second_y = dots[1][1]

    third_x = dots[2][0]
    third_y = dots[2][1]

    fourth_x = dots[3][0]
    fourth_y = dots[3][1]


    # 1-2, 3-4 선분이 서로 직선
    if first_y - second_y != 0 and third_y - fourth_y != 0:
        if (first_x - second_x) / (first_y - second_y) == (third_x - fourth_x) / (third_y - fourth_y):
            return 1
    
    # 1-3, 2-4 선분이 서로 직선
    if first_y - third_y != 0 and second_y - fourth_y != 0:
        if (first_x - third_x) / (first_y - third_y) == (second_x - fourth_x) / (second_y - fourth_y):
            return 1

    # 1-4, 2-3 선분이 서로 직선
    if first_y - fourth_y != 0 and third_y - second_y != 0:
        if (first_x - fourth_x) / (first_y - fourth_y) == (second_x - third_x) / (second_y - third_y):
            return 1


    # 두 선분의 y 좌표가 각각 같다면 평행
    if abs(first_y - second_y) == 0 and abs(third_y - fourth_y) == 0:
        return 1
    if abs(first_y - third_y) == 0 and abs(second_y - fourth_y) == 0:
        return 1
    if abs(first_y - fourth_y) == 0 and abs(third_y - second_y) == 0:
        return 1

    return 0