import unittest
import ta_backtest.tools.sma as sma


class TestSma(unittest.TestCase):
    def test_sma_10(self):
        data = []
        for x in range(1, 100):
            data.append(x)
        self.assertEqual(sma.sma(data, 10)[-1], 94.5)
