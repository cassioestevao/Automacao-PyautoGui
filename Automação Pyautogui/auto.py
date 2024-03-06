import pyautogui
import time

time.sleep(2)
pyautogui.PAUSE = 0.5

pyautogui.click(x=654, y=747)
time.sleep(1)
pyautogui.click(x=248, y=63)
pyautogui.write('https://github.com/cassioestevao')
time.sleep(1)
pyautogui.press('enter')
time.sleep(3)
