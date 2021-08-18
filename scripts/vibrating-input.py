import pyautogui
import time


while True:
    time.sleep(2)
    x, y = pyautogui.position()
    pyautogui.moveTo(x, y - 5,)
    pyautogui.click()
    pyautogui.moveTo(x, y + 5,)
