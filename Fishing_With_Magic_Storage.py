#this was created for a specific modpack that added infinite bait after a certain threshold and magic storage (duh). It is a slight bit janky but it works!
import time
import pyautogui
def click():
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
def right_click():
    pyautogui.mouseDown(button='right')
    time.sleep(0.1)
    pyautogui.mouseUp(button='right')
pyautogui.FAILSAFE = True
response = input("Would you like to take a snapshot of the deposit all button's coords? (y/n): ")
if response == "y":
    print("Please hover over the 'Deposit All' button in your magic storage.")
    time.sleep(5)
    deposit_all_coords = pyautogui.position()
response2 = input("Would you like to take a snapshot of the fishing line's coords? (y/n): ")
if response2 == "y":
    print("Please hover over the location where you want your mouse to be when casting the line.")
    time.sleep(10)
    fishing_line_coords = pyautogui.position()
print("Coordinates for 'Deposit All' button recorded at:", deposit_all_coords)
print("Coordinates for fishing line recorded at:", fishing_line_coords)
number_of_reps = int(input("Enter the number of repetitions to run the macro: "))
print("Starting the macro in 15 seconds. Please switch to Terraria. You can always abort by moving your mouse to the top-left corner of the screen.")
time.sleep(15)
for x in range(number_of_reps):
    pyautogui.moveTo(fishing_line_coords)
    time.sleep(0.1)
    click()
    time.sleep(4)
    click()
    time.sleep(0.5)
    pyautogui.moveTo(deposit_all_coords)
    time.sleep(0.1)
    click()
dropper = input("Would you like to drop the items after depositing? (y/n): ")
if dropper == "y":
    number_of_items = int(input("Enter the number of items to drop, take all crates out of the storage and favorite them: "))
    dropper_input = input("Please hover over the first slot in the magic storage interface. Enter y when you are ready.")
    if dropper_input == "y":
        print("Please hover over the first slot in the magic storage interface.")
        time.sleep(5)
        first_slot_coords = pyautogui.position()
        dropper_location = input("Please hover over an empty part of the screen where you want to drop the items. Enter y when you are ready.")
        if dropper_location == "y":
            print("Please hover over the desired drop location.")
            time.sleep(5)
            drop_location_coords = pyautogui.position()
            print("Coordinates for drop location recorded at:", drop_location_coords)
            for y in range(number_of_items):
                pyautogui.moveTo(first_slot_coords)
                time.sleep(0.1)
                click()
                time.sleep(0.1)
                pyautogui.moveTo(drop_location_coords)
                time.sleep(0.1)
                right_click()
                time.sleep(0.1)
