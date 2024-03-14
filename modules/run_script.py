# Open a command prompt and run a script

import os
import subprocess
import sys

def run_script(script_path):
    if not script_path.endswith(".py"):
        script_path += ".py"
    if os.path.exists(script_path):
        subprocess.run(["python", script_path])
    else:
        print(f"\033[31m{script_path} does not exist.\033[0m")

def main(file_name):
    # we want to go down into the /scripts directory
    script_path = os.path.join(os.getcwd(), "scripts", file_name)
    run_script(script_path)

    

    
    
