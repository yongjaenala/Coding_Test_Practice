# 미완
# https://school.programmers.co.kr/learn/courses/30/lessons/120866
# 안전지대

def solution(board):
    answer = 0



    return answer

# 테스트 케이스 9에서 런타임에러
# def solution(board):
#     answer = 0
#
#     tl = len(board)
#     for i in range(0, tl):
#         for j in range(0, tl):
#             if board[i][j] % 10 == 1:
#                 if i == 0 and j == 0:
#                     board[i][j + 1] += 10
#
#                     board[i + 1][j] += 10
#                     board[i + 1][j + 1] += 10
#                 elif i == tl-1 and j == 0:
#                     board[i - 1][j] += 10
#                     board[i - 1][j + 1] += 10
#
#                     board[i][j + 1] += 10
#                 elif i == 0 and j == tl-1:
#                     board[i][j - 1] += 10
#
#                     board[i + 1][j - 1] += 10
#                     board[i + 1][j] += 10
#                 elif i == tl-1 and j == tl-1:
#                     board[i - 1][j - 1] += 10
#                     board[i - 1][j] += 10
#
#                     board[i][j - 1] += 10
#                 elif i == 0:
#                     board[i][j - 1] += 10
#                     board[i][j + 1] += 10
#
#                     board[i + 1][j - 1] += 10
#                     board[i + 1][j] += 10
#                     board[i + 1][j + 1] += 10
#                 elif i == tl-1:
#                     board[i - 1][j - 1] += 10
#                     board[i - 1][j] += 10
#                     board[i - 1][j + 1] += 10
#
#                     board[i][j - 1] += 10
#                     board[i][j + 1] += 10
#                 elif j == 0:
#                     board[i - 1][j] += 10
#                     board[i - 1][j + 1] += 10
#
#                     board[i][j + 1] += 10
#
#                     board[i + 1][j] += 10
#                     board[i + 1][j + 1] += 10
#                 elif j == tl-1:
#                     board[i - 1][j - 1] += 10
#                     board[i - 1][j] += 10
#
#                     board[i][j - 1] += 10
#
#                     board[i + 1][j - 1] += 10
#                     board[i + 1][j] += 10
#                 else:
#                     board[i - 1][j - 1] += 10
#                     board[i - 1][j] += 10
#                     board[i - 1][j + 1] += 10
#
#                     board[i][j - 1] += 10
#                     board[i][j + 1] += 10
#
#                     board[i + 1][j - 1] += 10
#                     board[i + 1][j] += 10
#                     board[i + 1][j + 1] += 10
#     for i in range(0,len(board)):
#         for j in range(0, len(board)):
#             if board[i][j] == 0:
#                 answer += 1
#     return answer