__author__ = 'arthur'

import datetime
import calendar


FMT_DATE_PATTERN_V1 = '%d/%m/%Y'
FMT_DATE_PATTERN_EXTENDED = '%d %b %Y'
FMT_DATE_PATTERN_WEEKDAYS = '%A %d %b, %Y'
FMT_DATE_PATTERN_MYSQL = '%Y-%m-%d'
FMT_DATE_TIME_PATTERN = '%d/%m/%Y %H:%M:%S'
FMT_DATE_TIME_PATTERN_EXTENDED = '%d %b %Y %H:%M:%S'
FMT_DATE_TIME_PATTERN_FULL = '%d %B %Y %I:%M:%S %p'
FMT_DATE_TIME_PATTERN_CONSOLE = '%a %d %b %I:%M %p'
FMT_DATE_TIME_PATTERN_MYSQL = '%Y-%m-%d %H:%M:%S'
FMT_DATE_TIME_PATTERN_RATE_AM = '%Y %d %b, %H:%M'


# checks if the input dates are actually the same day
def is_same_day(day1, day2):
    return day1.year == day2.year and day1.month == day2.month and day1.day == day2.day


# checks if the input date is inside the given period
def is_in_range(day, period_start_day, period_end_day):
    return period_start_day <= day <= period_end_day


# checks if the input date is a weekend day
def is_weekend(day):
    return day.weekday() == 5 or day.weekday() == 6


# checks if the given year is a leap year
def is_leap_year(year):
    return calendar.isleap(year)


# gets list of days for the given time period
def get_period_days_as_list(date_start, date_end):
    if type(date_start) == datetime.datetime:
        start = date_start.date()
    else:
        start = date_start
    if type(date_end) == datetime.datetime:
        end = date_end.date()
    else:
        end = date_end
    result = []
    while start <= end:
        result.append(start)
        start = start + datetime.timedelta(1)
    return result


# returns number of days for the given period
def get_days_count(date_start, date_end):
    return (date_end - date_start).days


# returns the first day of the month of given day
def get_first_day_of_month(day):
    return datetime.date(day.year, day.month, 1)


# returns the last day of the month of given day
def get_last_day_of_month(day):
    return datetime.date(day.year, day.month + 1, 1) - datetime.timedelta(1)


# returns the number of days in month of given day
def get_month_days_count(day):
    return calendar.monthrange(day.year, day.month)[1]


# calculates the current month of given day, then returns the first day of next month
def get_next_month(day):
    return datetime.date(day.year, day.month + 1, 1)


# calculates the current month of given day, then returns the first day of previous month
def get_previous_month(day):
    if day.month == 1:
        return datetime.date(day.year - 1, 12, 1)
    return datetime.date(day.year, day.month - 1, 1)


# returns the next day of given date
def get_next_day(day):
    return day + datetime.timedelta(1)


# returns the previous day of given date
def get_previous_day(day):
    return day - datetime.timedelta(1)


# appends specified number of days to the given date
def add_days(_date, days_count):
    return _date + datetime.timedelta(days_count)


# subtracts specified number of days from the given date
def subtract_days(_date, days_count):
    return _date - datetime.timedelta(days_count)


# returns the 00:00:00 datetime for given input
def get_day_start(_datetime):
    return datetime.datetime(year=_datetime.year, month=_datetime.month, day=_datetime.day,
                             hour=0, minute=0, second=0, microsecond=0)


# returns the 23:59:59 datetime for given input
def get_day_end(_datetime):
    return datetime.datetime(year=_datetime.year, month=_datetime.month, day=_datetime.day,
                             hour=23, minute=59, second=59, microsecond=0)
