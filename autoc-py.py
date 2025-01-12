import json
import time
import device_mgr
import keyboard

# Load configuration from JSON file
def load_config():
    try:
        with open("config.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []



        self.trigger_key = trigger_key
        self.click_type = click_type
        self.frequency = frequency
        self.randomize = randomize


# Initialize and load configurations
configs = load_config()
keys = {
    "right": device_mgr.right,
    "middle": device_mgr.middle,
    "left": device_mgr.left,
}

def on_key_event(event):
    cfg_keys = configs.keys()
    if event.name in cfg_keys:
        if event.event_type == keyboard.KEY_DOWN:
            info = cfg_keys[event.name]
            clk_type = info["click_type"]
            if clk_type in keys.keys():
                keys[clk_type]()


keyboard.hook(on_key_event)
print("Listening for F9 key press or release... Press ESC to stop.")
keyboard.wait('esc')
