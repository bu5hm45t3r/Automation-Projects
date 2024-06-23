# MDAS is the sequence for math in any programming language. Multiplication, Division, Addition and Subtraction. And parenthasis overrides the multiplication (2+3)*6 in this 2+3 will be added first than multiplication.
import time
import pyautogui


"""
a = input("Hi there.. I am new to this world, but first can you name me?  ")
print("..." * 3)
print("So my name is"+' ' + a + ". Thank you..!\n")
time.sleep(2)
b = input(a +": So what is your name??  ")
time.sleep(2)
print("\n")
print(a+": Hello" + ' ' + b + ' ' + "Whatssup..?")

"""

"""
# Prints the display resolution
print(pyautogui.size())
time.sleep(2)

# Gives current mouse position on Display
print(pyautogui.position())
# pyautogui.scroll(500)

# Moves mouse to particular location and clicks at that area for 1 time
#pyautogui.moveTo(1341, 6, 0.4)
#pyautogui.click(1341, 6, 1)

time.sleep(6)

pyautogui.mouseUp(200, 300, button="left")
pyautogui.moveTo()
time.sleep(2)
pyautogui.mouseDown(400, 600, button="left")

"""


time.sleep(3)

pyautogui.dragRel(420,0,0.1,button="left")
pyautogui.dragRel(0,410,0.1,button="left")
pyautogui.dragRel(-420,0,0.1,button="left")
pyautogui.dragRel(0,-410,0.1,button="left")
pyautogui.moveRel(10,10,0.2)

time.sleep(1)
dist = 400
while dist > 0:
    pyautogui.dragRel(dist, 0, 0.03, button="left")
    dist = dist -10
    pyautogui.dragRel(0, dist, 0.03, button="left")
    pyautogui.dragRel(-dist, 0, 0.03, button="left")
    dist = dist -10
    pyautogui.dragRel(0, -dist, 0.03, button="left")
time.sleep(0.5)
#print(pyautogui.position())
pyautogui.moveTo(928,85)
pyautogui.click(928,85)
time.sleep(1)
pyautogui.moveTo(304, 85)
pyautogui.click(304,85)
pyautogui.moveTo(308,200)
pyautogui.click(308,200)
pyautogui.moveTo(432,335)
pyautogui.click(432,335)

"""
time.sleep(3)
print(pyautogui.position())
time.sleep(6)
print(pyautogui.position())


"""
