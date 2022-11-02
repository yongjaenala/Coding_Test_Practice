def solution(money):
    answer = []

    answer.append(money // 5500)
    answer.append(money - (answer[0] * 5500))
    return answer



# def solution(money):
#
#     answer = [money // 5500, money % 5500]
#     return answer