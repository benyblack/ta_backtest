import unittest
import ta_backtest.strategy.simple_rsi as rsi

class TestSimpleRsi(unittest.TestCase):

    def test_can_buy_rsi_100(self):
        data = []
        for x in range(1,100):
            data.append(x)
        can_buy = rsi.can_buy(data, 14)
        self.assertFalse(can_buy)
    
    def test_can_buy_rsi_0(self):
        data = []
        for x in range(100,1,-1):
            data.append(x)
        can_buy = rsi.can_buy(data, 14)
        self.assertTrue(can_buy)
    
    def test_can_sell_rsi_100(self):
        data = []
        for x in range(1, 100):
            data.append(x)
        can_sell = rsi.can_sell(data, 14)
        self.assertTrue(can_sell)

    def test_can_sell_rsi_0(self):
        data = []
        for x in range(100, 1, -1):
            data.append(x)
        can_sell = rsi.can_sell(data, 14)
        self.assertFalse(can_sell)

if __name__ == '__main__':
    unittest.main()