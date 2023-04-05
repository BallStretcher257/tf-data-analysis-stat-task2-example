import math

import pandas as pd
import numpy as np

from scipy.stats import chi2

chat_id = 625760313  # Ваш chat ID, не меняйте название переменной


def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    loc = x.mean()*4802
    return (loc - (2401 + 4802 * math.log(p))), \
        (loc + (2401 + 4802 * math.log(p)))
