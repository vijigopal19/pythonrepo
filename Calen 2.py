import datetime
import calendar


def findDay(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    print(born)
    return calendar.day_name[born]


date = '03 02 2019'
print(findDay(date))
print(calendar.weekday(2022, 3, 4))
