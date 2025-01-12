import mouse
import time

def perform_clicks():
    # Left click
    print("Left clicking...")
    mouse.click(button='left')
    time.sleep(1)  # Wait for 1 second

    # Right click
    print("Right clicking...")
    mouse.click(button='right')
    time.sleep(1)  # Wait for 1 second

    # Middle click
    print("Middle clicking...")
    mouse.click(button='middle')
    time.sleep(1)  # Wait for 1 second

if __name__ == "__main__":
    perform_clicks()
