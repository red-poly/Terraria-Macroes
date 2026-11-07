#this is just a little bit of code I use to create my macroes
import time
import pyautogui
def coordinate_finder():
    time.sleep(5)
    print(pyautogui.position())
def color_finder():
    time.sleep(5)
    (x, y) = pyautogui.position()
    print(pyautogui.pixel(x, y))
    print(f"({x}, {y})")
response = input("Would you like to use coordinate_finder (1) or color_finder (2): ")
if response == "1":
    coordinate_finder()
elif response == "2":
    color_finder()
