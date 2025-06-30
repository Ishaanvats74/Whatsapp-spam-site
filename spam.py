import pywhatkit
import pyautogui
import time
import sys

mobile_number = sys.argv[1]
message = sys.argv[2]
Count = int(sys.argv[3])

pywhatkit.sendwhatmsg_instantly(f"+91{mobile_number}", message ,wait_time=10)
time.sleep(8)
pyautogui.press("enter")
for i in range(Count-1):
    pyautogui.write(message)
    pyautogui.press("enter")
    time.sleep(0.5)



    