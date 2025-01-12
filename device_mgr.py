import platform

if platform.system() == "Linux":
    # Linux Wayland-compatible
    from pynput.mouse import Button, Controller
    from pynput.keyboard import Controller as KeyboardController
    mouse = Controller()
    keyboard = KeyboardController()
else:
    # Windows compatible
    import pyautogui


def right():
    # Right-click (RMB)
    if platform.system() == "Linux":
        mouse.click(Button.right)
    elif platform.system() == "Windows":
        pyautogui.click(button="right")


def left():
    # Left-click (LMB)
    if platform.system() == "Linux":
        mouse.click(Button.left)
    elif platform.system() == "Windows":
        pyautogui.click(button="left")


def middle():
    # Middle-click (MMB)
    if platform.system() == "Linux":
        mouse.click(Button.middle)
    elif platform.system() == "Windows":
        pyautogui.click(button="middle")


def type(string):
    # Type something
    if platform.system() == "Linux":
        keyboard.type(string)
    elif platform.system() == "Windows":
        pyautogui.typewrite(string)


if __name__ == "__main__":
    type("fuck you")

