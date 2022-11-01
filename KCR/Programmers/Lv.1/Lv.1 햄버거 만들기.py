# 첫 번째 풀이 : 시간 초과
def solution(ingredient):
    line = ''
    cnt = 0
    for i in ingredient :
        line += str(i)
        if line[-4:] == '1231':
            line = line[:-4]
            cnt += 1
    return cnt