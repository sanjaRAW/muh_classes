import keyboard
import pyautogui
import win32api
import win32con
from pyautogui import *


# x 447: y 459
# x 504: y 459
# x 587: y 459
# x 658: y 459
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)  # пауза
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


print("press q to stop")

while not keyboard.is_pressed('q'):
    if pyautogui.pixel(500, 406)[2] == 0:
        click(500, 421)
    if pyautogui.pixel(574, 406)[2] == 0:
        click(574, 421)
    if pyautogui.pixel(649, 406)[2] == 0:
        click(649, 421)
    if pyautogui.pixel(726, 406)[2] == 0:
        click(726, 421)
