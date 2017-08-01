class vectorizedbacktest:
    def __init__(self, data, strategy, strategy_params):
        self.data = data  # price history data
        self.strategy = strategy(self.data, **strategy_params)
        self.result = 'backtest yet to be run'
        self.performance = 'perf. yet to be calculated'

    def runtest(self):
        self.result = self.strategy.generate_signal()
        self.result['tradeID'] = (~(self.result['signal'] ==
                                    self.result['signal'].shift(1))).cumsum()
        self.result['return'] = np.log(self.result['closeMid'] /
                                       self.result['closeMid'].shift(1))
        self.result['strategy'] = self.result['return'] * self.result['signal']
        # take into account of transaction cost.
        # For every order, return reduced by the spread.
        self.result['strategy'] = np.where(self.result['signal'] >
                                           self.result.signal.shift(1),
                                           self.result['strategy'] -
                                           np.log(self.result.closeAsk /
                                           self.result.closeBid),
                                           self.result.strategy)
        return self.result

    def calperformance(self):
        numdays = np.unique(self.result.index.date).size
        self.result['benchmark'] = self.result['return'].cumsum() + 1
        self.result['equitycurve'] = self.result['strategy'].cumsum() + 1
        self.result['drawdown'] = (self.result['equitycurve'] /
                                   (self.result.expanding().max()) - 1)
        drawdown_max = self.result['drawdown_max'].max()
        # regroup to calculate daily return, this is used to calculate
        # the annualized std and sharpe ratio
        # create a groupy object to sum up daily returns
        daily_returns = self.result['strategy'].groupby(self.result.index.normalize())
        # sum them up
        self.daily_return = daily_returns.aggregate(np.sum)
        # get volatility
        vol = self.daily_return.std() * ((numdays) ** 0.5)
        average_daily_return = self.daily_return.mean()
        total_return = self.result['equitycurve'][-1] - 1
        sharpe = (average_daily_return * numdays) / vol

# trade analysis
        trades = self.result[['strategy', 'tradeID']].groupby('tradeID')
        self.trade = trades.aggregate(np.sum)
        total_count = self.trade['strategy'].count()
        positive_count = (self.trade['strategy'][self.trade['strategy'] > 0]
                          ).count()
        # negative_count = (self.trade['strategy'][self.trade['strategy'] < 0]
        #                   ).count()
        # winning_rate = float(positive_count) / total_count
        # average_positive_return = (self.trade['strategy'
        #                                       ][self.trade['strategy'
        #                                                    ] > 0]).mean()
        average_negative_return = (self.trade['strategy'][self.trade['strategy'
                                                                     ] > 0]
                                   ).mean()
        profit_factor = - average_positive_return / average_negative_return
        average_return = self.trade['strategy'].mean()
        max_trade = self.trade['strategy'].max()
        min_trade = self.trade['strategy'].min()
        # store trade metrics
        self.performance = {'Total Number of Trades': total_count,
                            'Winning Rate': winning_rate,
                            'Profit Factor': profit_factor,
                            'Average Return per Trade': average_return,
                            'Average Positive Return': average_positive_return,
                            'Average Negative Return': average_negative_return,
                            'Max Drawdown': drawdown_max,
                            'Total Return': total_return,
                            'Annualized Volatility': vol,
                            'Sharpe Ratio': sharpe,
                            'Largest Winning Trade': max_trade,
                            'Largest Losing Trade': min_trade}
