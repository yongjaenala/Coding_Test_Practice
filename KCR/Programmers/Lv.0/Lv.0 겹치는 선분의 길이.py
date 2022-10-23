def solution(lines):
    l = {}
    for i in range(min(sum(lines,[])), max(sum(lines,[]))+1) :
        l[i] = 0

    for i in lines :
        for j in range(sorted(i)[0]+1, sorted(i)[1]+1) :
            l[j] += 1
    return len([x for x in l.values() if x >=2])