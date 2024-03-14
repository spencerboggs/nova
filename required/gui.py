import tkinter as tk
import threading

class GUI:
    def __init__(self):
        master = tk.Tk()
        self.master = master
        master.title("NOVA - Neural Operative Virtual Assistant")
        master.geometry("1280x720")

        frame = tk.Frame(master)
        frame.pack(expand=True)

        # Create the label and center it within the frame
        self.title_label = tk.Label(frame, font=("Courier", 56), anchor="center")
        self.title_label.place(relx=0.5, rely=0.5, y=-50, anchor="center")
        self.title_label.pack(expand=True)

        self.subtitle_label = tk.Label(frame, font=("Courier", 24), anchor="center")
        self.subtitle_label.place(relx=0.5, rely=0.5, y=50, anchor="center")
        self.subtitle_label.pack(expand=True)

        # set initial title and subtitle to be NOVA and Neural Operative Virtual Assistant
        self.update_title("NOVA")
        self.update_subtitle("Neural Operative Virtual Assistant")

        # Create the label and center it within the frame
        self.label = tk.Label(frame, font=("Courier", 24), anchor="center")

        self.label.pack(expand=True)

    def update_text(self, text):
        self.label.config(text=text)
        self.label.update()
        self.master.update()
        self.master.update_idletasks()

    def update_title(self, title):
        self.title_label.config(text=title)
        self.title_label.update()
        self.master.update()
        self.master.update_idletasks()

    def update_subtitle(self, subtitle):
        self.subtitle_label.config(text=subtitle)
        self.subtitle_label.update()
        self.master.update()
        self.master.update_idletasks()



