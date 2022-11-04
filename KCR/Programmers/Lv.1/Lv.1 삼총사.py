def solution(number):
    possible = []
    for i in range(len(number)-2) :
        for j in range(i+1, len(number)-1) :
            for k in range(j+1, len(number)) :
                possible.append((number[i]+number[j]+number[k]))
    return possible.count(0)