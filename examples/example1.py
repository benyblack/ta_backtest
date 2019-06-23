import sys
sys.path.append("..")
from ta_backtest.strategy import simple_rsi
from ta_backtest.tools import data_loader as loader
from ta_backtest.tools.rsi import rsi as rsi
import ta_backtest.chart as chart
import ta_backtest.strategy.percent_jump as percent
import ta_backtest.strategy.trader as trader
import ta_backtest.tools.sma as sma
import ta_backtest.strategy.sma_crossover as sma_crossover


data = loader.from_csv('./1d-BTCUSDT.csv')
close_data = [x for x in data.Close]
date_data = [x for x in data.DateTime]
cash = 1
commision = 0.001

# Strategy:
# 1. Simple RSI
# potential_trades = simple_rsi.potential_trades(data.Close)
# cash, trade_history = trader.do_trades(data.Close, potential_trades, cash, commision)

# 2. Percent jump
# potential_trades = percent.potential_trades(data.Close)
# cash, trade_history = trader.do_trades(data.Close, potential_trades, cash, commision)

# 3. SMA cross-over
potential_trades = sma_crossover.potential_trades(data.Close)
new_cash, trade_history = trader.do_trades(data.Close, potential_trades, cash, commision)

# Indicator(s)
oscillator_data = [{'title': 'RSI 14', 'data': rsi(close_data)}]

# Make and show chart
plot, oscillator, trades = chart.make_chart("BTC_USDT", close_data, date_data, oscillator_data, trade_history)

# Add SMA 10, 20 for the third example
plot = chart.add_line_to_plot(plot, "SMA 10", date_data, sma.sma(close_data, 10), "blue")
plot = chart.add_line_to_plot(plot, "SMA 20", date_data, sma.sma(close_data, 20), "maroon")

# Show the plot in the browser
chart.show_plot(plot, oscillator, trades)
