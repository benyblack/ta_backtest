import unittest
import ta_backtest.strategy.sma_crossover as sma


class TestSimpleRsi(unittest.TestCase):

    def test_prev_sma(self):
        data1 = [(1, 1), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2),
                 (2, 2), (2, 2), (2, 2), (2, 2), (2, 2)]
        data2 = [(1, 1), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2),
                 (2, 2), (2, 2), (2, 3), (2, 2), (2, 2)]
        self.assertEqual(sma.prev_sma(data1, 10), (2, 2))
        self.assertEqual(sma.prev_sma(data2, 10), (2, 3))

    def test_can_buy(self):
        data1 = [(1, 1), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2),
                 (2, 2), (2, 2), (2, 2), (2, 2), (2, 2)]
        data2 = [(1, 1), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2),
                 (2, 2), (2, 2), (2, 3), (2, 2), (3, 2)]
        self.assertEqual(sma.can_buy(data1, 10), False)
        self.assertEqual(sma.can_buy(data2, 10), True)

    def test_can_sell(self):
        data1 = [(1, 1), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2),
                 (2, 2), (2, 2), (2, 2), (2, 2), (2, 2)]
        data2 = [(1, 1), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2),
                 (2, 2), (2, 2), (4, 3), (2, 2), (3, 4)]
        self.assertEqual(sma.can_sell(data1, 10), False)
        self.assertEqual(sma.can_sell(data2, 10), True)

    def test_potential_trades(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2,
                3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]
        self.assertEqual(sma.potential_trades(data), ([], []))
