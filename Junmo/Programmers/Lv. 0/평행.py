# 기울기가 무한대인 직선에 대한 케이스가 추가 되지 않아서 정답 처리된 듯
# https://school.programmers.co.kr/learn/courses/30/lessons/120875
# 평행

def solution(dots):
    answer = 0

    inclination = 0
    inc_list = []
    for i in range(len(dots) - 1):
        for j in range(i + 1, len(dots)):
            try:
                inclination = (dots[j][1] - dots[i][1]) / (dots[j][0] - dots[i][0])
            except:
                continue
            inc_list.append(inclination)

    for i in range(len(inc_list) - 1):
        for j in range(i + 1, len(inc_list)):
            if inc_list[i] == inc_list[j]:
                answer = 1

    return answer