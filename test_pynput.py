from pynput.keyboard import Listener, Key

# Define the callback function for key press events
def on_press(key):
    try:
        # Check if the pressed key is F9
        if key == Key.f9:
            print("F9 Key Pressed")
    except AttributeError:
        pass

# Define the callback function for key release events
def on_release(key):
    # Check if the released key is F9
    if key == Key.f9:
        print("F9 Key Released")
    # Stop listener if ESC is pressed
    if key == Key.esc:
        return False

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    print("Listening for F9 key press or release... Press ESC to stop.")
    listener.join()
