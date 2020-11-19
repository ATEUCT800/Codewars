# What is your favourite day of the week? Check if it's the most frequent day of the week in the year.

# You are given a year as integer (e. g. 2001). You should return the most frequent day(s) of the week in that year. The result has to be a list of days sorted by the order of days in week (e. g. ['Monday', 'Tuesday'], ['Saturday', 'Sunday'], ['Monday', 'Sunday']). Week starts with Monday.

# Input: Year as an int.

# Output: The list of most frequent days sorted by the order of days in week (from Monday to Sunday).

# Preconditions:

# Week starts on Monday.
# Year is between 1583 and 4000.
# Calendar is Gregorian.

from datetime import datetime, timedelta
import calendar

def most_frequent_days(year):
    days_count = []
    day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']

    for i in range(7):
        days_count.append(0)

    starting_date = datetime(year = year, month = 1, day = 1)
    end_date = datetime(year = year, month = 12, day = 31)
    number_of_days = 365 + int(calendar.isleap(year))
    dates = (starting_date + timedelta(days=x) for x in range(number_of_days))

    for date in dates:
        days_count[date.weekday()] += 1
    
    max_days = max(days_count)
    return [day_name[i] for i in range(7) if days_count[i] == max_days]



print(most_frequent_days(2427))