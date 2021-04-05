import pandas as pd


class RunningDateCV(object):
    """ RunningDateCV will iterate through a range of dates, yield the train vs test splits
    based on a comparison with the passed date column.

    >>> col = pd.to_datetime(['2014-01-01', '2014-01-02', '2014-01-03'])
    >>> for train, test in RunningDateCV(col): break
    >>> train
    array([ True, False, False], dtype=bool)

    """

    def __init__(self, date_column, start_date=None, end_date=None):
        """
            Args:
                date_column: Something that can broadcast a comparison.
                start_date (optional): The starting date
                end_date (optional): The ending date
        """

        self.date_column = date_column
        self.start_date = pd.to_datetime(start_date) or min(date_column)
        self.end_date = pd.to_datetime(end_date) or max(date_column)

        self.date_range = pd.date_range(self.start_date, self.end_date)

    def __iter__(self):

        for dt in self.date_range:

            train_mask = self.date_column <= dt
            test_mask = (dt < self.date_column) & (self.date_column <= self.end_date)

            yield train_mask, test_mask

if __name__ == "__main__":
    import doctest
    doctest.testmod()
