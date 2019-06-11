import unittest
import ta_backtest.tools.rsi as rsi


class TestRsi(unittest.TestCase):

    def test_rsi_100(self):
        data = []
        for x in range(1, 100):
            data.append(x)
        self.assertEqual(rsi.rsi(data)[-1], 100)

    def test_rsi_0(self):
        data = []
        for x in range(100, 1, -1):
            data.append(x)
        self.assertEqual(rsi.rsi(data)[-1], 0)

    def test_last_rsi_100(self):
        data = []
        for x in range(1, 100):
            data.append(x)
        self.assertEqual(rsi.last_rsi(data), 100)

    def test_last_rsi_0(self):
        data = []
        for x in range(100, 1, -1):
            data.append(x)
        self.assertEqual(rsi.last_rsi(data), 0)


if __name__ == '__main__':
    unittest.main()
