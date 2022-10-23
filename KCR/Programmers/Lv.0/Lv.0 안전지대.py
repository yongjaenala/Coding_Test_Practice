# 런타임 에러 발생

def solution(board):
    if 0 not in sum(board,[]) :
        return 0
    for i in range(len(board)) :
        for j in range(len(board)) :
            if board[i][j] == 1 :
                if (i != 0) & (board[i-1][j] != 1) :
                    board[i-1][j] = 2
                if (i != len(board)-1) & (board[i+1][j] != 1) :
                    board[i+1][j] = 2
                if (j != 0) & (board[i][j-1] != 1) :
                    board[i][j-1] = 2
                if (j != len(board)-1) & (board[i][j+1] != 1) :
                    board[i][j+1] = 2
                if (i != 0) & (j != 0) & (board[i-1][j-1] != 1) :
                    board[i-1][j-1] = 2
                if (i != 0) & (j != len(board)-1) & (board[i-1][j+1] != 1) :
                    board[i-1][j+1] = 2
                if (i != len(board)-1) & (j != 0) & (board[i+1][j-1] != 1) :
                    board[i+1][j-1] = 2
                if (i != len(board)-1) & (j != len(board)-1) & (board[i+1][j+1] != 1) :
                    board[i+1][j+1] = 2

    result = sum(board,[])
    return result.count(0)