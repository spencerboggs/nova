# Start an app through windows start menu

import os
import subprocess
import sys
import pyautogui

def start_app(app_name):
    try:
        pyautogui.hotkey("win")
        pyautogui.typewrite(app_name)
        pyautogui.press("enter")

    except Exception as e:
        print(f"\033[31mError opening the app: {e}\033[0m")

def main(app_name):
    start_app(app_name)