from tkinter import *
import sys
import os
from PIL import ImageTk, Image  
import numpy as np


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
                        foreground='#f1faee', background='#1d3557',font=("Helvetica", 30))
        self.splashLabel.pack(pady=90)
        self.splash_root.after(3000, self.main_window)
        self.splash_root.mainloop()

    def main_window(self):
        self.splash_root.destroy()
        self.root = Tk()
        self.root.title('License Plate Recognition')
        self.root.config(background='#1d3557')
        self.root.geometry("1024x800+320+0")

        self.browse = Button(self.root, text="Browse", fg='#f1faee', bg='#e63946', width=9, bd=1,
                            font=("Helvetica", 14), command=self.show_img)
        self.browse.grid(row=1, column=1, pady= (80, 20))

        self.start = Button(self.root, text="Start", fg='#f1faee', bg='#e63946', width=9, bd=1,
                            font=("Helvetica", 14), command=self.start)
        self.start.grid(row=2, column=1, padx= 50, pady=0)

        self.root.mainloop()

    def show_img(self):
        self.path = self.helper.fileDialog()
        self.load = Image.open(self.path)
        self.resized_image= self.load.resize((800,600), Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.resized_image)
        self.img = Label(self.root, image=self.render)
        self.img.image = self.render
        self.img.grid(row=3, column=2)
    
    def start(self):
        self.output = self.helper.start()
        self.img1 = self.output[0]
        self.txt = self.output[1]
        self.img.destroy()
        Label(self.root,text=f'OutPut: {self.txt}', fg='#f1faee', bg='#1d3557', bd=1,
                            font=("Helvetica", 20),).grid(row=1, column=2) 
        self.img1 = Image.fromarray(self.img1, 'RGB')
        self.resized_image1 = self.img1.resize((800,600), Image.ANTIALIAS)
        self.render1 = ImageTk.PhotoImage(self.img1)
        self.img1 = Label(self.root, image=self.render1)
        self.img1.image = self.render1
        self.img1.grid(row=3, column=2)
        
