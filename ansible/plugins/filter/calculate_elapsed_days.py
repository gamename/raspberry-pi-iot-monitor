"""
This is to convert a timestamp in the form of yyyy-mm-dd to the number of days since that timestamp.
"""

import datetime


def calculate_elapsed_days(date_stamp):
    """
    Calculates the number of days since the given timestamp.
    :param date_stamp: Date stamp in ISO 8601 format
    :return: Number of days since the given timestamp
    """
    # print("date_stamp:", date_stamp)
    today = datetime.date.today()
    sample_date = datetime.date.fromisoformat(date_stamp)
    delta = today - sample_date
    # print("delta:", delta.days)
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


def test_calculate_elapsed_days():
    """
    Tests the calculate_elapsed_days function
    :return: Nothing
    """
    assert (calculate_elapsed_days(datetime.date.today().isoformat()) == 0)
    assert (calculate_elapsed_days("2022-08-01") > 30)


if __name__ == "__main__":
    test_calculate_elapsed_days()
