# https://school.programmers.co.kr/learn/courses/30/lessons/120829
# 각도기
# 90도보다 작으면 예각(1)
# 90도면 직각(2)
# 90도보다 크고 180도 보다 작으면 둔각(3)
# 180도면 평각(4)

def solution(angle):
    answer = 0

    if angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif angle < 180:
        answer = 3
    else:
        answer = 4

    return answer