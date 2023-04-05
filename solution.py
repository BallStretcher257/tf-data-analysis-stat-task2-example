import pandas as pd
import numpy as np

from scipy.stats import norm

chat_id = 625760313  # Ваш chat ID, не меняйте название переменной


def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    a = np.array([v/4802 for v in x])
    alpha = 1 - p
    return a.mean() - np.sqrt(np.var(a)) * norm.ppf(1 - alpha / 2) / np.sqrt(len(a)), \
           a.mean() - np.sqrt(np.var(a)) * norm.ppf(alpha / 2) / np.sqrt(len(a))