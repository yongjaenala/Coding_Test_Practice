# 숫자 비교하기
# 두 수를 입력했을 때 같으면 1, 다르면 -1을 출력

def solution(num1, num2):
    answer = 0

    if num1 == num2:
        answer = 1
    else:
        answer = -1

    return answer