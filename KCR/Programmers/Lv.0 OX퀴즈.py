def solution(quiz):
    answer = []
    for q in quiz :
        quiz = q.split('=')
        result = quiz[1]
        problem = quiz[0]
        if eval(problem) == int(result) :
            answer.append('O')
        else :
            answer.append('X')
    return answer