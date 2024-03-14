# open the file in notepad

import os
import subprocess
import sys

def open_file(file_name):
    if "." not in file_name:
        for extension in ["json", "txt", "py", "csv"]:
            if os.path.exists(f"{file_name}.{extension}"):
                file_name = f"{file_name}.{extension}"
                break

    if os.path.exists(file_name):
        os.system(f"notepad {file_name}")

    else:
        return False

def main(file_name):
    return open_file(file_name)
