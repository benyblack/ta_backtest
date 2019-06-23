import ta_backtest.tools.rsi as rsi

RSI_BUY_LIMIT = 30
RSI_SELL_LIMIT = 70


def can_buy(rsi_list: [float], index: int):
    return rsi_list[index] < RSI_BUY_LIMIT


def can_sell(rsi_list: [float], index: int):
    return rsi_list[index] > RSI_SELL_LIMIT


def potential_trades(data):
    rsi_list = rsi.rsi(data)
    buy_points = [index for index, val in enumerate(data) if can_buy(rsi_list, index)]
    sell_points = [index for index, val in enumerate(data) if can_sell(rsi_list, index)]
    return buy_points, sell_points
