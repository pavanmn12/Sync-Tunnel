from tkinter import *
from PIL import Image, ImageTk
from itertools import count


# Image Button for Selection
class StorageBanner(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent)
        self.img = PhotoImage(*args, **kwargs)
        self.button = Button(self, image=self.img, compound=CENTER, bg="white")
        self.button.image = self.img
        self.button.pack()


# Label that displays images, and plays them if they are gifs
class ImageLabel(Label):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []
        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100
        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)


# Page where the cloud service is selected
class SelectPage(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent)
        self.text = Label(self, text="One time setup...", bg='white')
        self.text = Label(self, text="One time setup...", bg='white')
        self.gdrive = StorageBanner(self, file="logos\\Google\\gdrive-banner.png")
        self.onedrive = StorageBanner(self, file="logos\\OneDrive\\onedrive-banner.png")
        self.text.pack()
        self.gdrive.pack()
        self.onedrive.pack()


# Page where user logs into site via browser
class LoadingPage(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent)
        self.text = Label(self, text="Waiting for login in browser...", bg='white')
        self.loading_circle = ImageLabel(self, bg='white')
        self.loading_circle.load("logos\\loading.gif")
        self.loading_circle.pack()
        self.text.pack()


# Main page, users can utilise the software here
class MainPage(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent)
        self.text = Label(self, text="You are logged in!", bg='white')
        self.text.pack()
