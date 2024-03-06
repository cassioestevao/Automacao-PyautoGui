import pyautogui
import time

time.sleep(5)
pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('bloco de notas')
pyautogui.press('enter')

time.sleep(2)
pyautogui.write('k')
pyautogui.press('space')

time.sleep(0.9)
pyautogui.write('k')
pyautogui.press('space')

time.sleep(0.9)
pyautogui.write('k')
pyautogui.press('space')
