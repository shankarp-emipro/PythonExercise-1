import datetime

class DateDifference:
    def __init__(self, date1, date2):
        self.date1 = date1
        self.date2 = date2

    def get_date_difference(self):
        # returns -
        d_diff = self.date1 - self.date2       # d_diff - no. of day difference

        print("No. of days between {date1} and {date2} is: {d_diff}".format(date1=self.date1, date2=self.date2, d_diff=d_diff.days))


dd = DateDifference(datetime.datetime(2020, 3, 30), datetime.datetime(2020, 1, 15))
dd.get_date_difference()
