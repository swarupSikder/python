import pyautogui
from time import sleep

sleep(4)

for i in range(0,4):
    print(i)

pyautogui.write('I love you python', interval=0.25)
pyautogui.press('enter')




