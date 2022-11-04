def solution(emergency):
    answer = []
    emer = sorted(emergency, reverse=True)

    for i in emergency:
        answer.append(emer.index(i) + 1)

    return answer


def solution_another(emergency):
    return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]
