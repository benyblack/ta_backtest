import talib
import numpy as np
import pandas as pd

def can_buy(data: [float], index: int):
    df = pd.DataFrame(data=data[0:index+1])
    arr = np.array(df[0], dtype=np.dtype('d'))
    rsi = talib.RSI(arr, 14)
    return rsi[-1]<30

def can_sell(data: [float], index: int):
    df = pd.DataFrame(data=data[0:index+1])
    arr = np.array(df[0], dtype=np.dtype('d'))
    rsi = talib.RSI(arr, 14)
    return rsi[-1]>70