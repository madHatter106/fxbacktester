import numpy as np
import pandas as pd
from fxbacktester.strategy import Strategy
from fxbacktester.portfolio import Portfolio

"""
This file will make use of data downloaded from OANDA and stored as HDF5
tables via pandas
"""

class RandomForecastingStrategy(Strategy):
    """
    Demo that derives from Strategy to produce a set of signals that are randomly
    generated long/shorts.
    """
    def __init__(self, symbol, bars):
        """
        Inputs:
        -------
        symbol
            string

        bars
            open, high, low, close, volume (ohlcv)
            pandas DataFrame

        Output:
        -------
        signal
            TimeStamp, signal {-1, 0, 1}
            Pandas DataFrame
        """
        self.symbol = symbol
        self.bars = bars

    def generate_signals(self):
        """
        Creates a pandas DataFrame of random signals.
        """
        signals = pd.DataFrame(index=self.bars.index)
        signals['signal'] = np.sign(np.random.randn(len(signals)))

        # the first 5 elements are set to zero in order to minimise
        # upstream NaN errors in the forecaster.
        return signals

class MarketOnOpenPortfolio(Portfolio):
    """
    Inherits Portfolio to create a system that purchases 100 units of
    a particular symbol upon a long/short signal, assuming the market
    open price of a bar.

    In addition, there are zero transaction costs and cash can be immediately
    borrowed for shorting (no margin posting or interest requirements).

    Inputs:
    -------
    symbol
        fx symbol which forms the basis of the portfolio.
        string
    bars
        bars for a symbol set.
        pandas DataFrame
    signals
        (1, 0, -1) for each symbol.
        pandas DataFrame
    initial_capital:
        The amount in cash at the start of the portfolio.
        float
    """

    def __init(self, symbol, bars, signals, initial_capital=100000.0):
        self.symbol = symbol
        self.bars = bars
        self.signals = signals
        self.initial_capital = float(initial_capital)
        self.positions = self.generate_positions()

    def generate_positions(self):
        """
        Creates a 'positions' DataFrame that longs/shorts 1 lot of the
        particular symbol based on the input from the signals dataframe.
        """
        lot =
        positions = pd.DataFrame(index=signals.index).fillna(0.0)
        positions[self.symbol] = lot * signals['signal']
        return positions

    def backtest_portfolio(self):
        """
        Constructs a portfolio from the positions DataFrame by assuming
        the ability to trade at the precise market open price of each bar.

        Calculates the total cash and holdings (market price of each positions
        per bar), in order to generate an equity curve ('total') and a set of
        bar-based returns ('returns')

        Returns the portfolio object for use elsewhere
        """
        
        portfolio = self.positions * self.bars['Open'])
