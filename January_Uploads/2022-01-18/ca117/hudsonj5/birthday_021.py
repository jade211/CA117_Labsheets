#!/usr/bin/env python3

import sys
import calendar

def birthday(s):
   data = s.split()
   day = int(data[0])
   month = int(data[1])
   year = int(data[2])
   day_of_week = (calendar.weekday(year, month, day))
   if day_of_week == 0:
      return "You were born on a Monday and Monday's child is fair of face."
   elif day_of_week == 1:
      return "You were born on a Tuesday and Tuesday's child is full of grace."
   elif day_of_week == 2:
      return "You were born on a Wednesday and Wednesday's child is full of woe."
   elif day_of_week == 3:
      return "You were born on a Thursday and Thursday's child has far to go."
   elif day_of_week == 4:
      return "You were born on a Friday and Friday's child is loving and giving."
   elif day_of_week == 5:
      return "You were born on a Saturday and Saturday's child works hard for a living."
   elif day_of_week == 6:
      return "You were born on a Sunday and Sunday's child is fair and wise and good in every way."


for date in sys.stdin:
   date = date.strip()
   date = birthday(date)
   print(date)
