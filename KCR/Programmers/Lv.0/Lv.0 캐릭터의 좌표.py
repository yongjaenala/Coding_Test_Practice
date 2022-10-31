def solution(keyinput, board):
    loc = [0]*4 #[right, left, up, down]
    for i in keyinput :
        if i == 'right' :
            loc[0] += 1
        elif i == 'left' :
            loc[1] += 1
        elif i == 'up' :
            loc[2] += 1
        else :
            loc[3] += 1
    answer = [0+loc[0]-loc[1], 0+loc[2]-loc[3]]
    if answer[0] > board[0] :
        answer[0] = board[0]//2
    elif answer[0] < board[0]*(-1) :
        answer[0] = board[0]//2*(-1)
    elif answer[1] > board[1]:
        answer[1] = board[1] // 2
    elif answer[1] < board[1] * (-1):
        answer[1] = board[1] // 2 * (-1)
    return answer

keyinput = ["left", "right", "up", "right", "right"]	; board = [11, 11]	#[2, 1]
keyinput = ["down", "down", "down", "down", "down"]	; board = [7, 9]	#[0, -4]
print(solution(keyinput,board))