# 문자열을 왼쪽에서부터 읽어 나간다.
# 첫 문자의 수와 첫문자와 다른문자의 수가 같아지면 문자열을 분리한다.
# 분리후 이 과정을 반복한다. 남은부분없다면 종료
# 분리한 문자열의 수를 리턴


def solution(s):
    answer = list()
    while len(s)>0 :
        a=0
        b=0
        for i in range(len(s)):
            if s[i] == s[0]:
                a += 1
            else:
                b += 1
                if a == b:
                    break
                elif len(s[a+b:]) == 0:
                    answer.append(s[a+b:])
                    break
                else:
                    pass

        answer.append(s[:a+b])
        s = s[a+b:]

    return len(answer)


print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))
