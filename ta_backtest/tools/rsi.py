import talib
import numpy as np


def rsi(data: [float]):
    arr = np.array(data, dtype=np.dtype('d'))
    return talib.RSI(arr, 14)


def last_rsi(data: [float]):
    return rsi(data)[-1]
