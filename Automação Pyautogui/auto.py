import pyautogui
import time

time.sleep(5)
pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('bloco de notas')
pyautogui.press('enter')

time.sleep(2)
pyautogui.write('Tarefa 1 :')
pyautogui.press('enter')

time.sleep(0.9)
pyautogui.write('Tarefa 2 :')
pyautogui.press('enter')

time.sleep(0.9)
pyautogui.write('tarefa 3 :')
pyautogui.press('enter')
