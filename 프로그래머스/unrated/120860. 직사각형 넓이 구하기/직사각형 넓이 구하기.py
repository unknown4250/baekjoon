def solution(dots):

    first_x = dots[0][0]
    first_y = dots[0][1]

    second_x = dots[1][0]
    second_y = dots[1][1]

    third_x = dots[2][0]
    third_y = dots[2][1]

    fourth_x = dots[3][0]
    fourth_y = dots[3][1]

    if first_y == second_y:
        return abs(third_y - first_y) * abs(first_x - second_x)

    if first_y == third_y:
        return abs(second_y - first_y) * abs(first_x - third_x)

    if first_y == fourth_y :
        return abs(second_y - first_y) * abs(first_x - fourth_x)

    return 0