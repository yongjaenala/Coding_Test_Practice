# 미해결
# ctrl+z
def solution(s):
    answer = 0
    s = s.split(' ')
    ctrl_z = []
    for i in range(0, len(s)):
        if (s[i] == 'Z'):
            if i == 0:      # 첫번째 Z인 경우
                continue
            else:
                answer -= int(ctrl_z[-1])
                ctrl_z.drop[-1]
        answer += int(s[i])
        ctrl_z.append(s[i])
    return answer



# s = "1 2 Z 3"
# s = "10 20 30 40"
# s = "Z 1 2 3"
# s = "Z Z 1 2"
# s = "1 2 3 Z Z"
# s = "1"
# s = "0 0 0 0 Z"
# s = "-1 -2 -3"
# s = "-1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1 -1 0 Z 1"
s = "-100 10 Z 11 12 Z Z"

answer = 0
# print(s.split(' '))
