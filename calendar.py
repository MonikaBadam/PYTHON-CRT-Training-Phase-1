import calendar
def abc(year, month):
    c=calendar.TextCalendar(firstweekday=calendar.SUNDAY)
    cal= c.monthdatecalendar(year,month)
    for row in cal:
        for day in row:
            if day.month==month:
                print(f"(day.day:2)")
            else:
                print(" ", end=" ")
        print()

