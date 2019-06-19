import unittest
import ta_backtest.strategy.percent_jump as percent


class TestPercentJump(unittest.TestCase):

    def test_can_buy(self):
        data = [100 for x in range(1, 100)]
        self.assertFalse(percent.can_buy(data, 0))
        self.assertFalse(percent.can_buy(data, 3))
        self.assertFalse(percent.can_buy(data, 98))

    def test_can_sell(self):
        data = [100 for x in range(1, 100)]
        can_sell = percent.can_sell(data, [1, 2, 3], 90)
        self.assertTrue(can_sell)

    def test_potential_trades(self):
        data = [x for x in range(1, 100)]
        try:
            percent.potential_trades(data)
        except Exception:
            self.fail("do_trades(data, cash) raised ExceptionType unexpectedly!")


if __name__ == '__main__':
    unittest.main()
