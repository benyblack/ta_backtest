import ta_backtest.tools.rsi as rsi


def can_buy(rsi_list: [float], index: int):
    return rsi_list[index] < 30


def can_sell(rsi_list: [float], index: int):
    return rsi_list[index] > 70


def potential_trades(data):
    rsi_list = rsi.rsi(data)
    buy_points = [index for index, val in enumerate(data) if can_buy(rsi_list, index)]
    sell_points = [index for index, val in enumerate(data) if can_sell(rsi_list, index)]
    return buy_points, sell_points
