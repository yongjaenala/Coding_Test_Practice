def solution(sides):
    # 새로운 변이 가장 긴 변일 수 있는 경우의 수
    case = list(range(1, sum(sides)))
    answer = []
    for i in range(len(case)) :
        # 새로운 변이 가장 긴 변일 경우
        if (case[i] >= max(sides)) & (sum(sides) > case[i]) :
            answer.append(case[i])
        # 기존 max변이 가장 긴 변일 경우
        elif (case[i] <= max(sides)) & (max(sides) < case[i] + min(sides)) :
            answer.append(case[i])
    return len(answer)