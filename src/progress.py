from tqdm import tqdm
from colorama import Fore

import time

# Настройка внешнего вида прогресс бара
bar_format = "{l_bar}%s{bar}%s{r_bar}" % (Fore.GREEN, Fore.RESET)

# Длительность выполнения задачи
duration = 20

# Создание прогресс бара
with tqdm(total=duration, bar_format=bar_format) as progress_bar:
    for _ in range(duration):
        time.sleep(1)  # Имитация выполнения задачи
        progress_bar.update(1)  # Обновление прогресса
