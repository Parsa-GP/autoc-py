import json
import time
import device_mgr

# Load configuration from JSON file
def load_config():
    try:
        with open("config.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save configuration to JSON file
def save_config(config):
    with open("config.json", "w") as file:
        json.dump(config, file, indent=4)

# Mapping for mouse buttons
mouse_buttons = {
    "lmb": Button.left,
    "rmb": Button.right,
    "mmb": Button.middle,
}

class AutoClicker:
    def __init__(self, trigger_key, click_type, frequency, randomize):
        self.trigger_key = trigger_key
        self.click_type = click_type
        self.frequency = frequency
        self.randomize = randomize
        self.running = False
        self.mouse = mouse.Controller()

    def start(self):
        self.running = True
        print(f"AutoClicker started with trigger key '{self.trigger_key}'")

    def stop(self):
        self.running = False
        print(f"AutoClicker stopped for key '{self.trigger_key}'")

    def click_loop(self):
        delay = 1 / self.frequency
        if self.randomize:
            delay += (time.time() % 0.01)

        if self.click_type in mouse_buttons:
            self.mouse.click(mouse_buttons[self.click_type])
        else:
            self.press_key(self.click_type)

        time.sleep(delay)

    def press_key(self, key):
        with keyboard.Controller() as kb:
            kb.press(key)
            kb.release(key)

# Initialize and load configurations
configs = load_config()
instances = {}
active_keys = set()

def on_press(key):
    global configs, instances, active_keys
    try:
        key_name = key.char if hasattr(key, "char") else key.name
    except AttributeError:
        key_name = str(key)

    for config in configs:
        if config["trigger_key"] == key_name:
            if key_name not in active_keys:
                active_keys.add(key_name)
                if key_name not in instances:
                    instances[key_name] = AutoClicker(
                        config["trigger_key"],
                        config["click_type"],
                        config["frequency"],
                        config["randomize"]
                    )
                instances[key_name].start()
            else:
                active_keys.remove(key_name)
                if key_name in instances:
                    instances[key_name].stop()

def test_mouse_clicks():
    mouse = Controller()
    
    try:
        print("Testing left-click...")
        mouse.click(Button.left)
        print("Left-click tested successfully!")
        
        print("Testing right-click...")
        mouse.click(Button.right)
        print("Right-click tested successfully!")
        
        print("All tests completed!\n\n")
    except Exception as e:
        print(f"An error occurred during the test: {e}")

def run_auto_clicker():
    while True:
        for instance in instances.values():
            if instance.running:
                instance.click_loop()

with Listener(on_press=on_press) as listener:
    test_mouse_clicks()
    print("AutoClicker is running. Press your configured keys to toggle.")
    run_auto_clicker()
    listener.join()
