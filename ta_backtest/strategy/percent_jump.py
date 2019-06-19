BUY_PERCENT_LIMIT = 5
SELL_PERCENT_LIMIT = 2


def get_percent(a, b):
    return (b/a - 1) * 100


def can_buy(data: [float], index: int):
    if index < 2:
        return False
    percent = ((data[index - 2] / data[index]) - 1) * 100
    return percent > BUY_PERCENT_LIMIT


def can_sell(data: [float], buy_points: [float], index: int):
    if buy_points == []:
        return False
    last_buy_index = max([i for i, x in enumerate(buy_points) if i < data[index]])
    sell_percent = get_percent(data[index], data[last_buy_index])
    distance = index - last_buy_index
    return sell_percent >= SELL_PERCENT_LIMIT or distance > 3


def potential_trades(data):
    buy_points = [index for index, val in enumerate(data) if index > 1 and can_buy(data, index)]
    if len(buy_points) == 0:
        return [], []
    sell_points = [index for index, val in enumerate(data) if index > 1 and can_sell(data, buy_points, index)]
    return buy_points, sell_points
