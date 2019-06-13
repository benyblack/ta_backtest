import ta_backtest.tools.rsi as rsi


def can_buy(rsi_list: [float], index: int):
    return rsi_list[index] < 30


def can_sell(rsi_list: [float], index: int):
    return rsi_list[index] > 70


def do_iterate(data: [], init_cash: float):
    rsi_list = rsi.rsi(data)
    buy_points = [index for index, val in enumerate(data) if can_buy(rsi_list, index)]
    if len(buy_points) == 0:
        return init_cash
    sell_points = [index for index, val in enumerate(data) if can_sell(rsi_list, index)]

    def buy(buy_index, cash):
        print(f'buy: {buy_index}: {data[buy_index]}')
        sell_indexes = [index for index, val in enumerate(sell_points) if index > buy_index]
        if len(sell_indexes) == 0:
            return cash
        return sell(sell_indexes[0], buy_index, cash)

    def sell(sell_index, buy_index, cash):
        print(f'sell: {sell_index}: {data[sell_index]}')
        buy_indexes = [index for index, val in enumerate(buy_points) if index > sell_index]
        if len(buy_indexes) == 0:
            return cash
        return buy(buy_indexes[0], (data[sell_index]/data[buy_index])*cash)

    print(buy(buy_points[0], init_cash))
