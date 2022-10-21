quiz = ["3 - 4 = -3", "5 + 6 = 11"]	# ["X", "O"]
quiz = ["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]	# ["O", "O", "X", "O"]

def solution(quiz):
    for q in quiz :
        quiz = q.split('=')
        answer = quiz[1]
        problem = quiz[0]
        if 
