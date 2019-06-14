import unittest
import ta_backtest.strategy.simple_rsi as rsi


class TestSimpleRsi(unittest.TestCase):

    def test_can_buy_rsi_100(self):
        rsi_list = [100 for x in range(1, 100)]
        can_buy = rsi.can_buy(rsi_list, 14)
        self.assertFalse(can_buy)

    def test_can_buy_rsi_0(self):
        rsi_list = [0 for x in range(1, 100)]
        can_buy = rsi.can_buy(rsi_list, 14)
        self.assertTrue(can_buy)

    def test_can_sell_rsi_100(self):
        rsi_list = [100 for x in range(1, 100)]
        can_sell = rsi.can_sell(rsi_list, 14)
        self.assertTrue(can_sell)

    def test_can_sell_rsi_0(self):
        rsi_list = [0 for x in range(1, 100)]
        can_sell = rsi.can_sell(rsi_list, 14)
        self.assertFalse(can_sell)

    def test_do_trades(self):
        data = [x for x in range(1, 100)]
        try:
            rsi.do_trades(data, 1)
        except Exception:
            self.fail("do_trades(data, cash) raised ExceptionType unexpectedly!")


if __name__ == '__main__':
    unittest.main()
