# 기울기 : (y2-y1)/(x2-x1)
def solution(dots):
    answer = 0
    slop = []
    for i in range(0,len(dots)-1):
        for j in range(i+1,len(dots)):
            slop.append((dots[j][1]-dots[i][1])/(dots[j][0]-dots[i][0]))

    for i in range(0,len(slop)-1):
        if (slop[i] == slop[i+1]):
            answer += 1
        elif(slop[i] == slop[i+2] & i < 2):
            answer += 1

    return answer

dots = [[1,4],[9,2],[3,8],[10,4]]
slop = []

print(len(dots))
print(solution(dots))