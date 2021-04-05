import numpy as np

def mape(y_true, y_pred):
    """ This actual returns the decimal form
    not the percent, because nobody gives a shit.

    Args:
        y_true: Actual outcome
        y_pred: Predicted outcome

    Returns:
        mean aboslute percentage error

    >>> round(mape([1, 2, 3], [1.1, 2.2, 3.3]), 2)
    0.1
    """

    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    diff = np.abs(y_true - y_pred)

    return np.mean(diff / y_true)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
