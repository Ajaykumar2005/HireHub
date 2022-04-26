#import Tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk, ImageOps, ImageDraw

class App():
    def __init__(self, master, image_path):
        self.orig_img = Image.open(image_path)
        self.tk_img  = ImageTk.PhotoImage(self.orig_img)

        w, h = self.orig_img.size
        self.canvas = Canvas(master, width=w, height=h)
        self.canvas.pack()

        self.canvas.create_image(0, 0, image=self.tk_img, anchor='nw')
        self.canvas.bind_all("<MouseWheel>", self.zoom)
        self.canvas.bind_all("<Motion>", self.crop)

        self.create_mask()
        self.zoomValue = 0
        self.zimg_id = None

    def create_mask(self):
        self.mask = Image.new('L', (200,200), 0)
        draw = ImageDraw.Draw(self.mask) 
        draw.ellipse((0, 0) + self.mask.size, fill=255)        

    def zoom(self, event):
        if(event.delta > 0):
            if self.zoomValue != 4 : self.zoomValue += 1
        elif(event.delta < 0):
            if self.zoomValue != 0 : self.zoomValue -= 1
        self.crop(event)

    def crop(self, event):
        if self.zimg_id: self.canvas.delete(self.zimg_id)

        if (self.zoomValue) != 0:
            x, y = event.x, event.y
            if self.zoomValue == 1:
                tmp = self.orig_img.crop((x-45, y-30, x+45, y+30))
            elif self.zoomValue == 2:
                tmp = self.orig_img.crop((x-30, y-20, x+30, y+20))
            elif self.zoomValue == 3:
                tmp = self.orig_img.crop((x-15, y-10, x+15, y+10))
            elif self.zoomValue == 4:
                tmp = self.orig_img.crop((x-6, y-4, x+6, y+4))

            output = ImageOps.fit(tmp, self.mask.size, centering=(0.5, 0.5))
            output.putalpha(self.mask)
            self.zimg = ImageTk.PhotoImage(output)
            self.zimg_id = self.canvas.create_image(event.x, event.y, image=self.zimg)

root = Tk()
App(root, r'C:\Users\user\Desktop\AGE1.png')
root.mainloop()