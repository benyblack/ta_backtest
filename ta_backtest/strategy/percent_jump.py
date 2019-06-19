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


def do_trades(data: [], init_cash: float, commision: float) -> (float, {}):
    buy_points, sell_points = potential_trades(data)
    history = {}
    if len(buy_points) == 0:
        return init_cash, history

    def buy(buy_index, cash, old_history):
        new_cash = cash * (1 - commision)
        new_transaction = {buy_index: {'type': 'BUY', 'price': data[buy_index], 'cash': new_cash}}
        new_history = {**old_history, **new_transaction}
        sell_indexes = [index for index in sell_points if index > buy_index]
        if len(sell_indexes) == 0:
            return cash, new_history
        return sell(sell_indexes[0], buy_index, new_cash, new_history)

    def sell(sell_index, buy_index, cash, old_history):
        new_cash = (data[sell_index]/data[buy_index])*(1-commision)*cash
        new_transaction = {sell_index: {'type': 'SELL', 'price': data[sell_index], 'cash': new_cash}}
        new_history = {**old_history, **new_transaction}
        buy_indexes = [index for index in buy_points if index > sell_index]
        if len(buy_indexes) == 0:
            return new_cash, new_history
        return buy(buy_indexes[0], new_cash, new_history)

    return buy(buy_points[0], init_cash, history)
