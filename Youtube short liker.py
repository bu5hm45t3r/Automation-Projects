# Youtube Shorts liker...!
import time
import pyautogui

time.sleep(3)
#print(pyautogui.position())

# Like position Point(x=982, y=335)
# move to position and scroll Point(x=797, y=405)

for i in range(10):
    pyautogui.click(982,335,1,button="left")
    time.sleep(1)
    #pyautogui.click(1318,497,1,button="left")
    pyautogui.scroll(-20)
    time.sleep(1)