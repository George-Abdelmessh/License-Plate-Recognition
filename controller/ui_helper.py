from tkinter import filedialog
from img_proc import Recognition


class UiHelper:
    
    def __init__(self):
        print("Helper called")

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select An Image", filetype =
        (("jpeg files","*.jpg"),("all files","*.*")) )
        self.img = Recognition(self.filename)
        return self.filename


    def start(self):
        x = self.img.processing()
        return x
