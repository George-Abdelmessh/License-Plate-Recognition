from tkinter import *
from tkinter import ttk
import sys
sys.path.append('E:/SU IT/4.1/Image proccessing/License-Plate-Recognition/controller')
import ui_helper


class Root:

    def __init__(self):
        self.helper = ui_helper.UiHelper()
        self.splash_root = Tk()
        self.splash_root.title('Splash Screen')
        self.splash_root.config(background='#1d3557')
        self.splash_root.geometry("500x250+500+250")
        self.splash_root.overrideredirect(True)
        self.splashLabel = Label(self.splash_root, text="License Plate Recognition", 
                                foreground='#f1faee', background='#1d3557', 
                                font=("Helvetica", 30))
        self.splashLabel.pack(pady=90)

        self.splash_root.after(3000, self.main_window)
        self.splash_root.mainloop()


    def main_window(self):
        self.splash_root.destroy()
        self.root = Tk()
        self.root.title('License Plate Recognition')
        self.root.config(background='#1d3557')
        self.root.geometry("800x600+320+70")

        self.root.mainloop()
