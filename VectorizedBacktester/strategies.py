from copy import deepcopy
import numpy as np


class movingaveragestrategy:
    def __init__(self, data, short_window=5, long_window=20):
        self.data = deepcopy(data)
        self.short_window = short_window
        self.long_window = long_window

    def generate_signal(self):
        self.data['signal'] = 0 # initiate all data positions to 0
        self.data['closeMid'] = (self.data.closeBid + self.data.closeAsk) / 2
        self.data['fastma'] = self.data['closeMid'].rolling(window=self.short_window).mean()
        self.data['slowma'] = self.data['closeMid'].rolling(window=self.long_window).mean()
        self.data.dropna(inplace=True)
        self.data['signal'] = np.where(self.data.fastma > self.data.slowma, 1, -1)
