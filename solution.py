import pandas as pd
import numpy as np

from scipy.stats import erlang

chat_id = 625760313  # Ваш chat ID, не меняйте название переменной


def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргумент
    alpha = 1 - p
    loc = x.mean()
    n = len(x)
    scale = 1 / 4802
    return scale * (erlang.ppf(alpha / 2, n, loc=0, scale=(1 / n)) + loc - 1 / 2), \
           scale * (erlang.ppf(1 - alpha / 2, n, loc=0, scale=(1 / n)) + loc - 1 / 2)
