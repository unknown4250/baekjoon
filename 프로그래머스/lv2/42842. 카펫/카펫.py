def solution(brown, yellow):
    answer = []
    blocks = brown + yellow

    for col in range(1, blocks + 1):
        if (blocks / col) % 1 == 0:
            row = blocks / col
            if col >= row:
                if 2 * row + 2 * col == brown + 4:
                    answer = [col, int(row)]

    return answer