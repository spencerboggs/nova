# Stop a currently running application
# Usage: stop_app <app_name>

import os
import subprocess
import sys
import psutil
import time

def stop_app(app_name):
    # make sure it cannot stop itself or important system processes
    if app_name.lower() in ["stop_app", "python", "cmd", "powershell", "explorer", "taskmgr"]:
        print("\033[31mCannot stop this process.\033[0m")
        return
    
    try:
        for process in psutil.process_iter(attrs=['pid', 'name']):
            if app_name.lower() in process.info['name'].lower():
                pid = process.info['pid']
                process = psutil.Process(pid)
                process.terminate()
                print(f"\033[33mClosing {app_name}...\033[0m")
                time.sleep(1) 

        print(f"\033[31mClosed all instances of {app_name}.\033[0m")

    except Exception as e:
        print(f"Error closing the app: {e}")


def main(app_name):
    stop_app(app_name)