import calendar

def findDay(date):
    day, mon, yr = (int(i) for i in date.split(' '))
    day_no = calendar.weekday(yr, mon, day)
    print(day_no)    # 0:mon, 1:tue ...
    days = ["Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday", "Sunday"]
    return (days[day_no])

date = '06 04 2019'
print(findDay(date))
