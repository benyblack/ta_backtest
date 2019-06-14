import ta_backtest.tools.rsi as rsi


def can_buy(rsi_list: [float], index: int):
    return rsi_list[index] < 30


def can_sell(rsi_list: [float], index: int):
    return rsi_list[index] > 70


def do_trades(data: [], init_cash: float) -> (float, {}):
    rsi_list = rsi.rsi(data)
    buy_points = [index for index, val in enumerate(data) if can_buy(rsi_list, index)]
    if len(buy_points) == 0:
        return init_cash
    sell_points = [index for index, val in enumerate(data) if can_sell(rsi_list, index)]
    history = {}

    def buy(buy_index, cash, old_history):
        new_transaction = {buy_index: {'type': 'BUY', 'price': data[buy_index], 'cash': cash}}
        new_history = {**old_history, **new_transaction}
        sell_indexes = [index for index, val in enumerate(sell_points) if index > buy_index]
        if len(sell_indexes) == 0:
            return cash, new_history
        return sell(sell_indexes[0], buy_index, cash, new_history)

    def sell(sell_index, buy_index, cash, old_history):
        new_transaction = {buy_index: {'type': 'SELL', 'price': data[buy_index], 'cash': cash}}
        new_history = {**old_history, **new_transaction}
        buy_indexes = [index for index, val in enumerate(buy_points) if index > sell_index]
        if len(buy_indexes) == 0:
            return cash, new_history
        return buy(buy_indexes[0], (data[sell_index]/data[buy_index])*cash, new_history)

    return buy(buy_points[0], init_cash, history)
