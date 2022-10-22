def solution(dots):
    case = []
    for i in range(len(dots)-1) :
        for j in range(i+1, len(dots)) :
            case.append([i, j])
    gradi = []
    for c in case :
        if (dots[c[0]][0]-dots[c[1]][0]) != 0 :
            gradient =(dots[c[0]][1]-dots[c[1]][1])/(dots[c[0]][0]-dots[c[1]][0])
            gradi.append(gradient)

    if len(gradi) == len(set(gradi)) :
        return 0
    return 1