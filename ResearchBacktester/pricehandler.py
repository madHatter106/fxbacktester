from abc import ABCMeta, abstractmethod

class PriceHandler:

    __metaclass__ = ABCMeta

    @abstractmethod
    def stream_to_queue(self):
        """
        Streams a sequence of price data events (timestamp, bid, ask)
        tuples to the event queue.
        """
        raise NotImplementedError("stream_to_queue not implemented!")


class HistoricDFPriceHandler(PriceHandler):
    """
    Handles data listed in a pandas DataFrame.
    """

    def __init__(self, pairs, df_dir, events_queue, granularity='Tick'
                 bid_ask_prefix=''):
        """
        Initializes the historic price data handler.

        Inputs:
        -------
        pairs
            fx symbols to retrieve
            list of strings
        df_dir
            directory where DataFrames are stored
            string
        granularity
            specifies resolution keyword to be searched for as part of DF name
            string
        events_queue
            the queue to add the data to
            Queue object
        bid_ask_prefix
            keyword that precedes 'bid' or 'ask'
        """
        
