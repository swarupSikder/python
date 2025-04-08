import pyautogui
from time import sleep

# input
n = int(input())

# wait 4 seconds for processing
sleep(4)

for i in range(1, n+1):
    pyautogui.write('#' *i, interval=0.25)
    pyautogui.press('enter')

# check output here by clicking on last line (within 4 seconds)
# just after giving user input


