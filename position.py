class Position():
    def __init__(self, signals, units,
                 exposure, avg_price, cur_price):
        self.side = signals
        self.units = units
        self.exposure = exposure
        self.avg_sprice = avg_price
        self.cur_price = cur_price
        self.profit_base = self.calculate_profit_base()
        self.profit_perc = self.calculate_profit_perc()

    def calculate_pips(self):
        return self.side * (self.cur_price - self.avg_price)
