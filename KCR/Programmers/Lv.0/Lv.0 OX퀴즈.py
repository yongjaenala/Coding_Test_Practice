def solution(quiz):
    answer = []
    for q in quiz :
        quiz = q.split('=')
        result = quiz[1]
        problem = quiz[0]
        if eval(problem) == int(result) : # eval : 문자열 계산식을 계산해주는 함수
            answer.append('O')
        else :
            answer.append('X')
    return answer