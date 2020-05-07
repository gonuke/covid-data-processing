import pandas as pd
import numpy as np


class Semilog_Covid_Plot(Object):
    """

    """
    pass


class Covid_Data(Object):

    pass


class Covid_Data_Annotations(Covid_Data):
    pass


def fit_data(x, y, window, exp_weight_const=0):
    """
    Perform a simple exponential fit to the (x,y) data using a window
    of data.  The data can be weighted exponentially within the window
    to put more weight on some of the data.

    inputs
    ======
    x : numpy array of independent data
    y : numpy array of dependent data (should be same length as x)
    window : tuple indicating range of data to use for fit
    exp_weight_const : data within the window will be weighted exponentially,
                       according to the formula:
                       w = exp( (index-last) / constant )

    """
