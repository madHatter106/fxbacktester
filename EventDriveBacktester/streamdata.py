import requests
import json
import os


class DataStreamer:
    """
    class to stream data from OANDA.
    fxTrade environments:
        live - the live (real money) environment
        practice - the practice (paper money) env.

        Inputs:
        -------
        environment
            Open, high, low, close, volume (ohlcv)
            Pandas DataFrame

        Output:
        -------
        Action signal
            TimeStamp, signal {-1, 0, 1}
            Pandas DataFrame

    """
    def __init__(self, instruments, oandaTOK, oandaID, environment):

        domainDict = {'live': 'stream-fxtrade.oanda.com',
                      'practice': 'stream-fxpractice.oanda.com'}
        self.domain = domainDict[environment]
        self.accessToken = oandaTOK
        self.accessId = oandaID
        self.intruments = instruments

    def ConnectToStream(self):
        streamUrl = 'https://%s/v1/prices' % self.domain
        headers = {'Authorization': 'Bearer %s' % self.accessToken}
        params = {'instruments': instruments, 'accountId': self.accessId}
        try:
            session = requests.Session()
            req = requests.Request('GET', streamUrl, headers=headers, params=params)
            pre = req.prepare()
            resp = session.send(pre, stream=True, verify=True)
            if resp.status_code != 200:
                if resp.status_code == 401:
                    print("Unauthorized access. Verify credentials.")
                elif resp.status_code == 400:
                    print("Malformed request. Verify payload.")
                return None
            return resp
        except Exception as e:
            session.close()
            print("Caught exception when connecting to stream\n %s" % str(e))

    def Stream2Queue(self):
        resp = self.ConnectToStream()
        if resp:
            for line in response.iter_lines(1):
                pass
        else:
            return
