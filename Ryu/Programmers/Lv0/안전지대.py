# 미해결

def solution(board):
    answer = 0

    for i in range(0,len(board)):
        for j in range(0, len(board)):
            if board[i][j] == 1:
                if i == 0:
                    board[i][j]
    for i in range(0,len(board)):
        for j in range(0, len(board)):
            if board[i][j] == 0:
                answer += 1
    return answer



board1 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
board2 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
board3 = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
board4 = [[0,0,0,0,0],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1]]
board5 = [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
board6 = [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
board7 = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

print(solution(board1)) # 16
print(solution(board2)) # 13
print(solution(board3)) # 0
print(solution(board4)) # 15
print(solution(board5)) # 8
print(solution(board6)) # 15
print(solution(board7)) # 15
