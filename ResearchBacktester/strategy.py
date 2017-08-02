# backtest.py
from abc import ABCMeta, abstractmethod

class Strategy:
    """Strategy is an abstract base class providing an interface for
    all subsequent (inherited) trading strategies.

    The goal of a (derived) Strategy object is to output a list of signals,
    which has the form of a time series indexed pandas DataFrame.

    In this instance only a single symbol/instrument is supported.
    """



    __metaclass__ = ABCMeta

    @abstractmethod
    def generate_signals(self):
        """An implementation is required to return the DataFrame of symbols
        containing the signals to go long, short or hold (1, -1 or 0).

        Inputs:
        -------
        Bar Data
            Open, high, low, close, volume (ohlcv)
            Pandas DataFrame

        Output:
        -------
        Action signal
            TimeStamp, signal {-1, 0, 1}
            Pandas DataFrame

        """
        raise NotImplementedError("Should implement generate_signals()!")
