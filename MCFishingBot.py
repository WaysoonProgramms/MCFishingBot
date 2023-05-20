import time
import cv2
import mss
import numpy as np
import pyautogui

# Функция эмуляции клика
def click():
    pyautogui.mouseDown(button='right')
    time.sleep(0.01)
    pyautogui.mouseUp(button='right')


# Подключение MSS модуля
title = "Minecraft Auto-Fishing Bot Previewer"
sct = mss.mss()

# Задержка перед запуском
print("СТАРТ через 15 секунд! Подготовьтесь...")
time.sleep(15)
print("ЗАПУСК")

# Первый бросок
print("Удочка заброшена ...")
click()
last_time = time.time()

# Цикл работы бота
while True:
    if time.time() - last_time < 2:
        continue

    # Область захвата экрана
    mon = {"top": 40, "left": 0, "width": 600, "height": 500}
    img = np.asarray(sct.grab(mon))

    # Поиск цвета
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    lower_red = np.array([204, 51, 51])
    upper_red = np.array([204, 51, 51])
    mask0 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([135, 20, 20])
    upper_red = np.array([135, 20, 20])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    mask = mask0 + mask1

    hasRed = np.sum(mask)
    if hasRed > 0:
        pass
    else:
        print("Улов! ...")
        time.sleep(0.3)
        click()

        time.sleep(3)
        print("Удочка заброшена ...")
        click()

        last_time = time.time()
