def solution(ingredient):
    line = ''
    cnt = 0
    for i in ingredient :
        line += str(i)
        # if '1231' in line : -> 시간초과 for문이 한 번 더 돌아가는 거라 O(n^2)
        if line[-4:] == '1231':
            line = line[:-4]
            cnt += 1
    return cnt