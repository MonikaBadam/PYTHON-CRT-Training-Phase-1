#import calendar
#create a plain text calendar
calendar = calendar.TextCalendar(calendar.SUNDAY)
str = calendar.formatmonth(2023, 1)
print(str)
