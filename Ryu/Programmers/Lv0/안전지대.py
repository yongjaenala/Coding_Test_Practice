def solution(board):
    answer = 0

    for i in range(0,len(board)):
        for j in range(0, len(board)):
            try:
                if (board[i][j]%10) == 1:
                    board[i - 1][j-1] += 10
                    board[i - 1][j] += 10
                    board[i - 1][j + 1] += 10
                    board[i][j - 1] += 10
                    board[i][j] += 10
                    board[i][j + 1] += 10
                    board[i+1][j - 1] += 10
                    board[i+1][j] += 10
                    board[i+1][j + 1] += 10
            except:
                pass
    for i in range(0,len(board)):
        for j in range(0, len(board)):
            if board[i][j] == 0:
                answer += 1
    return answer

board1 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
board2 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
board3 = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
board4 = [[0,0,0,0,0],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1]]



print(solution(board2))
