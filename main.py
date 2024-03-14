""" 
NOVA - Neural Operative Virtual Assistant
Created by Spencer Boggs
"""

import os
import tkinter as tk
import threading
import time

import required.voice_recognition as voice_recognition
import required.video_recognition as video_recognition
import required.voice_output as voice_output
import required.gui as gui

import modules.open_file as open_file
import modules.start_app as start_app
import modules.run_script as run_script
import modules.stop_app as stop_app

ALL_MODULES_ACTIVE = True

modules = ["open_file", "start_app", "run_script", "stop_app"]
active_modules = []
if ALL_MODULES_ACTIVE:
    active_modules = modules

os.system("cls")
print("\033[1;31m")

print("███╗░░██╗░█████╗░██╗░░░██╗░█████╗░")
print("████╗░██║██╔══██╗██║░░░██║██╔══██╗")
print("██╔██╗██║██║░░██║╚██╗░██╔╝███████║")
print("██║╚████║██║░░██║░╚████╔╝░██╔══██║")
print("██║░╚███║╚█████╔╝░░╚██╔╝░░██║░░██║")
print("╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝")
print("Neural Operative Virtual Assistant")
print("\033[0m")


# create the gui
nova_gui = gui.GUI()
#nova_gui.update_text("NOVA - Neural Operative Virtual Assistant")
print("Done")
#nova_gui.update_text("Initializing...")


if ALL_MODULES_ACTIVE == False:
    for module in modules:
        if os.path.exists(f"modules/{module}.py"):
            voice_output.speak(f"Would you like to activate the {module} module?")
            activate_module = voice_recognition.main(f"ACTIVATE {module.upper()} MODULE? (YES/NO):")
            if activate_module == "yes":
                active_modules.append(module)
                voice_output.speak(f"{module} module activated")
                print(f"\033[1;32m{module} module activated\033[0m")
            else:
                voice_output.speak(f"{module} module not activated")
                print(f"\033[1;31m{module} module not activated\033[0m")

            """ activate_module = input(f"Activate {module} module? (y/n): ")
            if activate_module.lower() == "y":
                active_modules.append(module) """

def check_module(module_name):
    if module_name in active_modules:
        return True

def main():
    command = voice_recognition.main()
    # nova_gui.update_text(command)

    # RUN SCRIPT
    run_script_keywords = ["run", "execute"]
    if any(keyword in command for keyword in run_script_keywords):
        if not check_module("run_script"):
            print("run_script module is not active")
            return
        
        # the script name should be all of the words after a keyword connected by _
        script_name = command.split(" ") 
        script_name = [word.replace("-", "_") for word in script_name]
        # join all but the first word together with _
        script_name = "_".join(script_name[1:])
        run_script.main(script_name)

    # OPEN FILE
    open_file_keywords = ["open", "edit", "read", "write"]
    file_found = False
    if any(keyword in command for keyword in open_file_keywords):
        if not check_module("open_file"):
            print("open_file module is not active")
            return
        
        file_name = command.split(" ")[-1]
        file_found = open_file.main(file_name)
        
    # START APP
    start_app_keywords = ["open", "start", "launch", "begin"]
    if any(keyword in command for keyword in start_app_keywords) and file_found == False:
        if not check_module("start_app"):
            print("start_app module is not active")
            return
        
        app_name = command.split(" ")[-1]
        start_app.main(app_name)

    # STOP APP
    stop_app_keywords = ["close", "stop", "end"]
    if any(keyword in command for keyword in stop_app_keywords) and command != "stop listening":
        app_name = command.split(" ")[-1]
        stop_app.main(app_name)

    # EXIT
    if command == "stop listening":
        print("Exiting...")
        return
    
    else:
        pass

    main()
    
main()