def solution(score):
    avg = []
    for j, i in enumerate(score) :
        avg.append(((i[0]+i[1])/2, j))
    avg.sort(reverse=True)
    bf = avg[0][0]
    rank = 1
    for j, i in enumerate(avg) :
        if (bf == i[0]) & (j != 0) :
            rank = avg[j-1][2]
            avg[j] = (avg[j][1], avg[j][0], rank)
            rank = j +1
        else :
            avg[j] = (avg[j][1], avg[j][0], rank)
        bf = i[0]
        rank += 1
    avg.sort()
    answer = []
    for i in avg :
        answer.append(i[2])
    return answer

# 테스트 케이스
score = [[80, 70], [90, 50], [40, 70], [50, 80]]	#[1, 2, 4, 3]
score = [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]	#[4, 4, 6, 2, 2, 1, 7]
score = [[100,100],[100,100],[100,100],[100,90]]  #[1,1,1,4]
score = [[0,0],[0,0],[0,0]]
score = [[1, 2], [1, 1], [1, 1]] # [1, 2, 2]
score = [[0, 20], [80, 100], [10, 10], [90, 90], [20, 0]] #-> [3, 1, 3, 1, 3]
score = [[0, 20], [10, 10], [30, 0], [10, 11], [0, 30], [14, 6], [15, 15]] #-- > [5 , 5 , 1, 4, 1, 5, 1]
print(solution(score))