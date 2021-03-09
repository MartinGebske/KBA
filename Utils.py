#### Hier kommen kleine Helferlein rein
import datetime as dt
from dateutil.rrule import rrule, MONTHLY


def createTimeSpan(s,e):
    """[INFO: ] Returns a monthly Timespan beginning from year(s) to year (e) as a list of strings"""
    startDate = dt.date(s, 1, 1)
    endDate = dt.date(e, 1, 1)

    temp= [d for d in rrule(MONTHLY, dtstart=startDate, until=endDate)]
    dates = []
    for d in temp:
        cur = dt.date.strftime(d, "%b-%y")
        dates.append(str(cur))

    return dates
