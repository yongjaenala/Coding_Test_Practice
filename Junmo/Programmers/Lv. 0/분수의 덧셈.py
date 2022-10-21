# 분수의 덧셈
# 분수가 입력된다. (첫 번째 분자, 첫 번째 분모, 두 번째 분자, 두 번째 분모)
# 입력된 분수들의 합을 기약분수 (분자, 분모) 형태의 배열로 출력하라.

def solution(denum1, num1, denum2, num2):
    answer = []

    answer_dnum = denum1 * num2 + denum2 * num1
    answer_num = num1 * num2

    for i in range(min(answer_dnum, answer_num), 0, -1):
        if answer_dnum % i == 0 and answer_num % i == 0:
            answer_dnum /= i
            answer_num /= i
            break;

    answer = [int(answer_dnum), int(answer_num)]

    return answer

print(solution(1, 4, 1, 4))