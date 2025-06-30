import pywhatkit
import pyautogui
import time

mobile_number = int(input())
message = input()
loop = int(input())

pywhatkit.sendwhatmsg_instantly(f"+91{mobile_number}", message ,wait_time=6)
pyautogui.press("enter")
for i in range(loop-1):
    pyautogui.write(message)
    pyautogui.press("enter")
    time.sleep(0.5)
