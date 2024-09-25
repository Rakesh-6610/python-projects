import keyboard
import pyautogui


sensitivity = 10

while True:
    match keyboard.read_key():
        case "space":
            break
        case "up":
            pyautogui.move(0, -sensitivity)
            print("moving up")
        case "down":
            pyautogui.move(0, sensitivity)
            print("moving down")
        case "left":
            pyautogui.move(-sensitivity, 0)
            print("moving left")
        case "right":
            pyautogui.move(sensitivity, 0)
            print("moving right")
        case "[":
            if not sensitivity <= 0:
                sensitivity -= 1
        case "]":
            sensitivity += 1

    print(keyboard.read_key())