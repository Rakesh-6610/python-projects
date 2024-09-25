import pygame as game
import sys
import pyautogui

game.init()
game.joystick.init()

count = game.joystick.get_count()
joy_count = 0
delay = 10
sensitivity = 10
pyautogui.FAILSAFE = False

if count == 0:
    sys.exit("No joysticks found")
else:
    joystick = game.joystick.Joystick(0)
    joystick.init()
    print(f"Detected {joystick.get_name()}")

    running = True
    while running:
        for event in game.event.get():
            if event.type == game.QUIT:
                running = False

            elif event.type == game.JOYBUTTONDOWN:
                print(f"Button {event.button} pressed")            
                if event.button == 0:
                    sensitivity -= 1
                elif event.button == 1:
                    sensitivity += 1
                elif event.button == 2:
                    delay -= 1
                elif event.button == 3:
                    delay += 1
                elif event.button == 8:
                    sys.exit("exited")

                print(f"Delay: {delay}ms, Sensitivity: {sensitivity}")

            x_axis = joystick.get_axis(0)
            y_axis = joystick.get_axis(1)

            print(f"X: {x_axis}, Y: {y_axis}")
            if (abs(x_axis) > 0.1 or abs(y_axis) > 0.1) and joy_count % delay == 0:
                dx = x_axis * sensitivity
                dy = y_axis * sensitivity
                pyautogui.moveRel(dx, dy)
                print(f"Moved {dx}x, {dy}y")
            joy_count += 1
game.quit()