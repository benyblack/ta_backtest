import ta_backtest.tools.rsi as rsi


def can_buy(rsi_list: [float], index: int):
    return rsi_list[index] < 30


def can_sell(rsi_list: [float], index: int):
    return rsi_list[index] > 70


def do_trades(data: [], init_cash: float, commision: float) -> (float, {}):
    rsi_list = rsi.rsi(data)
    buy_points = [index for index, val in enumerate(data) if can_buy(rsi_list, index)]
    if len(buy_points) == 0:
        return init_cash
    sell_points = [index for index, val in enumerate(data) if can_sell(rsi_list, index)]
    history = {}

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
