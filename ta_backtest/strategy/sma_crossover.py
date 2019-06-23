import ta_backtest.tools.sma as sma

SMA_LOWER_BAND = 10
SMA_UPPER_BAND = 20


def can_buy(sma_list: [(float, float)], index: int):
    if index == 0:
        return False
    current_lower_sma, current_upper_sma = sma_list[index]
    prev_lower_sma, prev_upper_sma = prev_sma(sma_list, index)
    return prev_lower_sma < prev_upper_sma and current_lower_sma > current_upper_sma


def can_sell(sma_list: [(float, float)], index: int):
    if index == 0:
        return False
    current_lower_sma, current_upper_sma = sma_list[index]
    prev_lower_sma, prev_upper_sma = prev_sma(sma_list, index)
    return prev_lower_sma > prev_upper_sma and current_lower_sma < current_upper_sma


def prev_sma(sma_list: [(float, float)], index: int):
    if index < 2:
        return sma_list[1]
    prev_lower_sma, prev_upper_sma = sma_list[index - 1]
    if prev_lower_sma == prev_upper_sma:
        return prev_sma(sma_list, index-1)
    return prev_lower_sma, prev_upper_sma


def potential_trades(data):
    sma_low_list = sma.sma(data, SMA_LOWER_BAND)
    sma_high_list = sma.sma(data, SMA_UPPER_BAND)
    data = [(x, sma_high_list[i]) for i, x in enumerate(sma_low_list)]
    buy_points = [index for index, val in enumerate(data) if can_buy(data, index)]
    sell_points = [index for index, val in enumerate(data) if can_sell(data, index)]
    return buy_points, sell_points
