def solution(s1, s2):
    answer = sum([s1.count(s) for s in s2])
    return answer


def solution(s1, s2):
    return len(set(s1)&set(s2))

def solution(s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    return len(s1.intersection(s2))