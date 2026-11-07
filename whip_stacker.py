# Perfect for anyone with a skill issue (I can relate!)
import time
import pyautogui
import keyboard
def click():
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
print("This macro will allow you to whip stack. Press Num1 to begin and Del to stop press Num9 to quit the program, this button only works after starting the macro at least once.")
number_whips = int(input("Enter the number of whips to stack (have default keybinds and whips in the slots going from left to right): "))
input_list = []
for x in range(number_whips):
    input_list.append(x+1)
print(f"The following inputs will be used: {input_list}")
macro_active = 0
def Begin_Macro():
    print("Macro Started")
    global macro_active
    macro_active = 1
    
def End_Macro():
    print("Macro Stopped")
    global macro_active
    macro_active = 0

keyboard.add_hotkey('num 1', lambda: Begin_Macro())
keyboard.add_hotkey('del', lambda: End_Macro())

keyboard.wait('num 1')

if macro_active == 1:
    while macro_active == 1:
        for i in input_list:
            keyboard.press(str(i))
            time.sleep(0.1)
            keyboard.release(str(i))
            time.sleep(0.1)
            click()


keyboard.wait('num 9')
time.sleep(0.1)
quit()
