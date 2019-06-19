import unittest
import ta_backtest.strategy.trader as trader


class TestTrader(unittest.TestCase):

    def test_do_trades(self):
        data = [x for x in range(1, 100)]
        try:
            trader.do_trades(data, [[], []], 1, 0.001)
        except Exception:
            self.fail("do_trades(data, cash) raised ExceptionType unexpectedly!")


if __name__ == '__main__':
    unittest.main()
