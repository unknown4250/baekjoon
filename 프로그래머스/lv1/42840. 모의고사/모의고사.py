def solution(answers):
    answer = []
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    scores = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == student1[i % len(student1)]:
            scores[0] += 1
        if answers[i] == student2[i % len(student2)]:
            scores[1] += 1
        if answers[i] == student3[i % len(student3)]:
            scores[2] += 1

    max_score = max(scores)

    for i in range(len(scores)):
        if max_score == scores[i]:
            answer.append(i+1)

    return answer
