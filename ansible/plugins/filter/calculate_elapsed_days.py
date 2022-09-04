"""
This is to convert a timestamp in the form of yyyy-mm-dd to the number of days since that timestamp.
"""

import datetime

def calculate_elapsed_days(date_stamp):
    date_format = "%Y-%m-%d"
    today = datetime.date.today()
    sample_date = datetime.strptime(date_stamp, date_format)
    delta = sample_date - today
    return delta.days


class FilterModule(object):
    def filters(self):
        """
        Associate the filter with a specific function
        :return: the filter-to-function association
        """
        return {
            'calculate_elapsed_days': calculate_elapsed_days
        }
