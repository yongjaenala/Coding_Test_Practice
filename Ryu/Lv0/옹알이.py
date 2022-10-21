def solution(input):
    shy = ["aya", "ye", "woo", "ma"]
    answer = 0
    for i in input:
        for j in shy:
            if j*2 in i: # 같은 발음을 하는 것을 어려워 함
                continue
            else:
               i = i.replace(j, "")
        if len(i.strip()) == 0:
                answer += 1
    return answer

babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
print(solution(babbling))
