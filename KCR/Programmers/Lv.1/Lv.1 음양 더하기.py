def solution(absolutes, signs):
    signs = [1 if x == True else -1 for x in signs]
    return sum([x*y for x,y in zip(absolutes, signs)])
