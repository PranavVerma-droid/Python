import tkinter as tk
import colorama
from colorama import Fore, Style

def init_colorama():
    colorama.init()

def define_text():
    label = tk.Label(root, text="Hello, world!")
    label.pack()
    print(Fore.GREEN + "All text defined." + Style.RESET_ALL)

def define_buttons():
    button = tk.Button(root, text="Press Me!")
    button.pack()
    print(Fore.GREEN + "All buttons defined." + Style.RESET_ALL)

def define_icons():
    # TODO: Add some icons in this project.
    print(Fore.RED + "No icons defined in the source code." + Style.RESET_ALL)

def run_main_loop():
    root.mainloop()

if __name__ == "__main__":
    init_colorama()
    root = tk.Tk()

    define_text()
    define_buttons()
    define_icons() 

    run_main_loop()