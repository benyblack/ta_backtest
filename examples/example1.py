import sys
sys.path.append("..")
from ta_backtest.strategy import simple_rsi
from ta_backtest.tools import data_loader as loader
from ta_backtest.tools.rsi import rsi as rsi
import ta_backtest.chart as chart
import ta_backtest.strategy.percent_jump as percent


data = loader.from_csv('./1h-BTCUSDT.csv')
close_data = [x for x in data.Close]
date_data = [x for x in data.DateTime]
cash = 1
commision = 0.001

# Strategy:
#
# cash, trade_history = simple_rsi.do_trades(data.Close, cash, commision)
cash, trade_history = percent.do_trades(data.Close, cash, commision)

# Indicator(s)
oscillator_data = [{'title': 'RSI 14', 'data': rsi(close_data)}]

# Make and show chart
plot, oscillator, trades = chart.make_chart("BTC_USDT", close_data, date_data, oscillator_data, trade_history)
chart.show_plot(plot, oscillator, trades)
