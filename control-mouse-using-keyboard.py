import keyboard
import pyautogui
from tabulate import tabulate


sensitivity = 10

print("Button control")
print(tabulate([ ["exit", "space"], ["mouse up", "arrow up"], ["mouse down", "arrow down"], ["mouse left", "arrow left"], ["mouse right", "arrow right"], ["mouse scroll up", "["], ["mouse scroll down", "]"]], headers=["action", "key"], tablefmt="heavy_grid"))
req = input("Press any key to continue...")
if req != "esc" or req == "":
    while True:
        match keyboard.read_key():
            case "space":
                break
            case "up":
                pyautogui.move(0, -sensitivity)
            case "down":
                pyautogui.move(0, sensitivity)
            case "left":
                pyautogui.move(-sensitivity, 0)
            case "right":
                pyautogui.move(sensitivity, 0)
            case "[":
                if not sensitivity <= 0: 
                    sensitivity -= 1
            case "]":
                sensitivity += 1 