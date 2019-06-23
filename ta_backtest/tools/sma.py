import talib
import numpy as np


def sma(data: [float], period: int):
    arr = np.array(data, dtype=np.dtype('d'))
    return talib.SMA(arr, period)


def last_sma(data: [float], period: int):
    return sma(data, period)[-1]
