def solution(dots):
    answer = 0
    slop = []
    for i in range(0,len(dots)-1):
        for j in range(i+1,len(dots)):
            slop.append((dots[j][1]-dots[i][1])/(dots[j][0]-dots[i][0]))

    # for i in range(0,len(slop)-1):
    #     for j in range(i+1,len(slop)):
    #         if (slop[i] == slop[j]):
    #             answer += 1
    if (len(slop) == len(set(slop))):
        return 0
    return 1

dots = [[1,4],[9,2],[3,8],[10,4]]
slop = []

print(solution(dots))
# print(solution(dots))=
