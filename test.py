import keyboard

# Define a listener for the F9 key press
def on_f9_key_event(event):
    if event.name == 'f9':
        if event.event_type == keyboard.KEY_DOWN:
            print("F9 Key Pressed")
        elif event.event_type == keyboard.KEY_UP:
            print("F9 Key Released")

# Start listening for key events
keyboard.hook(on_f9_key_event)

print("Listening for F9 key press or release... Press ESC to stop.")

# Block the program to keep listening
keyboard.wait('esc')
