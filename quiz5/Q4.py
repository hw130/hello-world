#일을 7로 나눴을 때
#1은 월요일
#2는 화요일
#...
#7은 일요일
def after_100(month,date,day):
    month31=[1,3,5,7,8,10,12]
    month30=[4,6,9,11] #30일만 가지는 '달'들을 리스트에 저장
    weekday=['월','화','수','목','금','토','일']
    _100date=date+99
    week=weekday[day % 7]

    print(f'{month}월 {day}일 {week}요일부터 100일 뒤는{month}월 {day}일 {week}요일')



after_100(6,21,"월")
