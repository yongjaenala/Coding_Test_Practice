def solution(board):
    if 0 not in sum(board,[]) :
        return 0
    for i in range(0,len(board)) :
        for j in range(0,len(board)) :
            if board[i][j] == 1 :
                if i != 0 :
                    if board[i-1][j] != 1 :
                        board[i-1][j] = 2
                if i != len(board)-1 :
                    if board[i+1][j] != 1 :
                        board[i+1][j] = 2
                if j != 0 :
                    if board[i][j-1] != 1 :
                        board[i][j-1] = 2
                if j != len(board)-1 :
                    if board[i][j+1] != 1 :
                        board[i][j+1] = 2
                if (i != 0) & (j != 0) :
                    if board[i-1][j-1] != 1 :
                        board[i-1][j-1] = 2
                if (i != 0) & (j != len(board)-1) :
                    if board[i-1][j+1] != 1 :
                        board[i-1][j+1] = 2
                if (i != len(board)-1) & (j != 0) :
                    if board[i+1][j-1] != 1 :
                        board[i+1][j-1] = 2
                if (i != len(board)-1) & (j != len(board)-1) :
                    if board[i+1][j+1] != 1 :
                        board[i+1][j+1] = 2

    result = sum(board,[])
    return result.count(0)

board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]  # 16
board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]] #13
board = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1]] # 0
board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1]] #15
board = [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0]] #8
board = [[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]] #15
print(solution(board))