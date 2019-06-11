import ta_backtest.tools.rsi as rsi


def can_buy(data: [float], index: int):
    last_rsi = rsi.last_rsi(data[0:index+1])
    return last_rsi < 30


def can_sell(data: [float], index: int):
    last_rsi = rsi.last_rsi(data[0:index+1])
    return last_rsi > 70
