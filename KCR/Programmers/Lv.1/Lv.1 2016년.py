def solution(a, b):
    # 2016-01-01 : FRI
    to_first = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weekdays = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    return weekdays[(sum(to_first[:a-1])+b)%7 -1]
