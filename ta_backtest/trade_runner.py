from strategy import simple_rsi as rsi
from tools import data_loader as loader


data = loader.from_csv('../../binance_data/data/BTCUSDT/4h-BTCUSDT.csv')
rsi.do_iterate(data.Close, 1)
