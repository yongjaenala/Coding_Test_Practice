# 미해결
def solution(s):
    answer = 0
    s = s.split(' ')
    for i in range(0, len(s)):
        if (s[i] == 'Z'):
            if i == 0:
                continue
            else:
                if s[i - 1] == 'Z':
                    continue
                else:
                    answer -= int(s[i - 1])
        else:
            answer += int(s[i])
    return answer

# s = "1 2 Z 3"
# s = "10 20 30 40"
# s = "Z 1 2 3"
# s = "Z Z 1 2"
# s = "1 2 3 Z Z"
# s = "1"
# s = "0 0 0 0 Z"
# s = "-1 -2 -3"
s = "-1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1"


answer = 0
# print(s.split(' '))
s = s.split(' ')
print(s)
for i in range(0,len(s)):
    if (s[i] == 'Z'):
        if i == 0:
            continue
        else:
            if s[i-1] == 'Z':
                continue
            else:
                answer -= int(s[i-1])
    else:
        answer += int(s[i])
print(answer)
