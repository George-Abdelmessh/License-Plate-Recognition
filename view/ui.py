import tkinter
from tkinter import *
from tkinter import ttk
import sys
import os
from PIL import ImageTk, Image  

sys.path.append(f'{os.getcwd()}/controller')
import ui_helper


class Root:

    root = ''

    def begin(self):
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
        # TODO MAKE TIME 3000
        self.splash_root.after(1, self.main_window)
        self.splash_root.mainloop()

    def main_window(self):
        self.splash_root.destroy()
        self.root = Tk()
        self.root.title('License Plate Recognition')
        self.root.config(background='#1d3557')
        self.root.geometry("1024x800+320+0")

        self.browse = Button(self.root, text="Browse", fg='#f1faee', bg='#e63946', width=9, bd=1,
                            font=("Helvetica", 14), command=self.show_img)
        self.browse.place(x=20, y=110)
        self.start = Button(self.root, text="Start", fg='#f1faee', bg='#e63946', width=9, bd=1,
                            font=("Helvetica", 14), command=self.helper.start)
        self.start.place(x=20, y=155)

        self.root.mainloop()

    def show_img(self):
        self.path = self.helper.fileDialog()
        self.load = Image.open(self.path)
        self.render = ImageTk.PhotoImage(self.load)
        self.img = Label(self.root, image=self.render, width= 800, height=600)
        self.img.image = self.render
        self.img.place(x=0, y=0)
