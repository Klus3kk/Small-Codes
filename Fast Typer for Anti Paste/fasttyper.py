import pyautogui
import keyboard
import time

def super_fast_typing(text):
    for word in text.split():  
        pyautogui.write(word, interval=0)  
        pyautogui.write(" ")  

def on_paste_hotkey():
    text_to_type = """Answer"""
    
    time.sleep(1)  
    super_fast_typing(text_to_type)

# Set up the hotkey
keyboard.add_hotkey("alt+k", on_paste_hotkey)

print("Press ALT+K to type LaTeX code instantly after a 1-second delay")
keyboard.wait("esc")  # ESC to exit
