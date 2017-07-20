from abc import ABCMeta, abstractmethod


class Portfolio():
    """An abstract base class representing a portfolio of
    positions (including both instruments and cash), determined
    on the basis of a set of signals provided by a Strategy.

    Inputs:
    -------
    Strategy signal
        TimeStamp, signal {-1, 0, 1}
        Pandas DataFrame

    Output:
    -------
    Result
        TimeStamp, equity curve, transaction cost trade record,
        Pandas DataFrame
    """

    __metaclass__ = ABCMeta

    def generate_positions(self):
        """Provides the logic to determine how the portfolio
        positions are allocated on the basis of forecasting
        signals and available cash."""
        raise NotImplementedError("Should implement generate_positions()!")

    def backtest_portfolio(self):
        """Provides the logic to generate the trading orders
        and subsequent equity curve (i.e. growth of total equity),
        as a sum of holdings and cash, and the bar-period returns
        associated with this curve based on the 'positions' DataFrame.

        Produces a portfolio object that can be examined by
        other classes/functions."""
        raise NotImplementedError("Should implement backtest_portfolio()!")
