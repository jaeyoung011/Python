import datetime

def solution(a, b):

    days = ['MON','TUE','WED','THU','FRI','SAT','SUN'] # SUN,MON,TUE,WED,THU,FRI,SAT 는 Mon 가 나옴
    answer = days[datetime.date(2016,a,b).weekday()]

    return answer

print(solution(5, 24))