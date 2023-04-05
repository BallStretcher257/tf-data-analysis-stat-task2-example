import pandas as pd
import numpy as np

from scipy.stats import chi2

chat_id = 625760313  # Ваш chat ID, не меняйте название переменной


def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = x.mean()
    scale = 1 / (2 * x.sum())
    return loc + scale * chi2.ppf(alpha / 2, 2 * len(x)),\
        loc + scale * chi2.ppf(1 - alpha / 2, 2 * len(x))