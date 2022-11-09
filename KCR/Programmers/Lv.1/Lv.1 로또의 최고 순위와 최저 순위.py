def solution(lottos, win_nums):
    rank = [6, 5, 4, 3, 2]
    # 6, 5, 4, 3, 2 -> 1, 2, 3, 4, 5
    # 나머지 6등
    lottos.sort()
    win_nums.sort()
    cnt = 0
    for i in lottos :
        if i in win_nums :
           cnt += 1
    # 순위
    answer = []
    for i in range(2) :
        if cnt < 2 :
            answer.insert(0, 6)
        elif cnt >= 6 :
            answer.insert(0, 1)
        else :
            answer.insert(0, rank.index(cnt) +1)
        cnt += lottos.count(0)
    return answer