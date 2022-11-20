# 첫 번째 풀이
# def solution(answers):
#     answer = []
#     s1 = [1, 2, 3, 4, 5]
#     s2 = [2, 1, 2, 3, 2, 4, 2, 5]
#     s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
#
#     s1l = len(answers) // len(s1)
#     s2l = len(answers) // len(s2)
#     s3l = len(answers) // len(s3)
#
#     s1 = s1 * (s1l + 1)
#     s2 = s2 * (s2l + 1)
#     s3 = s3 * (s3l + 1)
#
#     def check(s):
#         for i in range(len(answers)):
#             if s[i] == answers[i]:
#                 s[i] = 'O'
#             else:
#                 s[i] = 'X'
#         return s.count('O')
#
#     c1 = check(s1)
#     c2 = check(s2)
#     c3 = check(s3)
#
#     li = [c1, c2, c3]
#
#     for i, c in enumerate(li):
#         if c != 0 and c == max(li):
#             answer.append(i + 1)
#
#     return answer

# 두 번째 풀이
def solution(answers):
    scores = [0, 0, 0]
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i, j in enumerate(answers):
        if j == s1[i % len(s1)]:
            scores[0] += 1
        if j == s2[i % len(s2)]:
            scores[1] += 1
        if j == s3[i % len(s3)]:
            scores[2] += 1
    return [i+1 for i, s in enumerate(scores) if s == max(scores)]