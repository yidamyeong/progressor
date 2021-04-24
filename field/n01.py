def solution(scores):
    n = len(scores)
    student = []

    for i in range(n):
        s = []
        for score in scores:
            s.append(score[i])
        student.append(s)

    avg = []
    for i in range(n):
        student[i].sort()
        lowest = student[i][0]
        highest = student[i][-1]
        count = n

        if student[i][i] == lowest or student[i][i] == highest:
            student[i][i] = 0
            count -= 1

        avg.append(get_grade(sum(student[i]) / count))

    answer = ''.join(avg)
    return answer


def get_grade(average):
    if average >= 90:
        return 'A'
    elif 80 <= average < 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    elif 50 <= average < 70:
        return 'D'
    elif average < 50:
        return 'F'


scores_example = [[50, 60, 70], [55, 65, 75], [70, 90, 80]]

print(solution(scores_example))
