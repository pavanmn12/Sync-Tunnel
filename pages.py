from tkinter import *
from tkinter import filedialog
import tkinter.scrolledtext as tkst
from PIL import Image, ImageTk
from itertools import count
from enum import Enum
import datetime


# Image Button for Selection
class StorageBanner(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent)
        self.img = PhotoImage(*args, **kwargs)
        self.button = Button(self, image = self.img, compound=CENTER, bg="white")
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

# Enum used for storing weekday within the DayButton
class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

# Button for each day, eg Monday, Tuesday, etc
class DayButton(Button):
	def __init__(self, parent, day, *args, **kwargs):
		Button.__init__(self, parent, *args, **kwargs)
		self.day = day
		self.syncing = False

	def toggleSync(self):
		self.syncing = not self.syncing
		if self.syncing:
			self.configure(text = "Syncing")
		else:
			self.configure(text = "Not Syncing")

class Logbox(tkst.ScrolledText):
	def __init__(self, parent, *args, **kwargs):
		tkst.ScrolledText.__init__(self, parent, *args, **kwargs)
		self.configure(state=DISABLED)

	def add_msg(self, msg):
		now = datetime.datetime.now()
		self.configure(state = NORMAL)
		self.insert(INSERT, msg + " - " + now.strftime("%H:%M %d-%m-%y"))
		self.configure(state = DISABLED)

# Page where the cloud service is selected
class SelectPage(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, bg = 'white')
		self.text = Label(self, text="One time setup...", bg='white')
		self.text = Label(self, text="One time setup...", bg='white')
		self.gdrive = StorageBanner(self, file = "logos\\Google\\gdrive-banner.png")
		self.onedrive = StorageBanner(self, file = "logos\\OneDrive\\onedrive-banner.png")
		self.text.pack()
		self.gdrive.pack()
		self.onedrive.pack()

# Page where user logs into site via browser
class LoadingPage(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, bg = 'white')
		self.text = Label(self, text="Waiting for login in browser...", bg='white')
		self.loading_circle = ImageLabel(self, bg='white')
		self.loading_circle.load("logos\\loading.gif")
		self.text.pack()
		self.loading_circle.pack()

# Main page, users can utilise the software here
class MainPage(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, bg = 'white')
		self.buttons = []


		self.logbox = Logbox(self)
		self.logbox.place(relx=0.07, rely=0.05, relheight=0.19, relwidth=0.83)
		self.logbox.configure(background="#808080")
		self.logbox.configure(font=("Arial", 12))
		self.logbox.configure(foreground="#ffffff")
		self.logbox.configure(highlightbackground="#d9d9d9")
		self.logbox.configure(highlightcolor="black")
		self.logbox.configure(insertbackground="black")
		self.logbox.configure(insertborderwidth="3")
		self.logbox.configure(selectbackground="#c4c4c4")
		self.logbox.configure(selectforeground="black")
		self.logbox.configure(undo="1")
		self.logbox.configure(width=10)
		self.logbox.configure(wrap=NONE)

		self.folders_label = Label(self)
		self.folders_label.place(relx=0.76, rely=0.35, height=31, width=84)
		self.folders_label.configure(activebackground="#f9f9f9")
		self.folders_label.configure(activeforeground="black")
		self.folders_label.configure(background="#ffffff")
		self.folders_label.configure(disabledforeground="#a3a3a3")
		self.folders_label.configure(foreground="#000000")
		self.folders_label.configure(highlightbackground="#d9d9d9")
		self.folders_label.configure(highlightcolor="black")
		self.folders_label.configure(text='''Folders''')
		self.folders_label.configure(font=("Arial", 15))

		self.add_button = Button(self)
		self.add_button.place(relx=0.87, rely=0.35, height=24, width=27)
		self.add_button.configure(activebackground="#d9d9d9")
		self.add_button.configure(activeforeground="#000000")
		self.add_button.configure(background="#d9d9d9")
		self.add_button.configure(disabledforeground="#a3a3a3")
		self.add_button.configure(foreground="#000000")
		self.add_button.configure(highlightbackground="#d9d9d9")
		self.add_button.configure(highlightcolor="black")
		self._img1 = PhotoImage(file="logos\\add_logo.png")
		self.add_button.configure(image=self._img1)
		self.add_button.configure(pady="0")

		self.accountdetails_frame = Frame(self)
		self.accountdetails_frame.place(relx=0.72, rely=0.6, relheight=0.36, relwidth=0.26)
		self.accountdetails_frame.configure(borderwidth="2")
		self.accountdetails_frame.configure(background="#ffffff")
		self.accountdetails_frame.configure(highlightbackground="#d9d9d9")
		self.accountdetails_frame.configure(highlightcolor="black")
		self.accountdetails_frame.configure(width=255)

		self.accountdetails_label = Label(self.accountdetails_frame)
		self.accountdetails_label.place(relx=0.16, rely=0.19, height=21, width=160)
		self.accountdetails_label.configure(activebackground="#f9f9f9")
		self.accountdetails_label.configure(activeforeground="black")
		self.accountdetails_label.configure(background="#ffffff")
		self.accountdetails_label.configure(disabledforeground="#a3a3a3")
		self.accountdetails_label.configure(foreground="#000000")
		self.accountdetails_label.configure(highlightbackground="#d9d9d9")
		self.accountdetails_label.configure(highlightcolor="black")
		self.accountdetails_label.configure(text='''Account Details:''')
		self.accountdetails_label.configure(font=("Arial", 15))

		self.cloudservice_label = Label(self.accountdetails_frame)
		self.cloudservice_label.place(relx=0.16, rely=0.33, height=21, width=84)
		self.cloudservice_label.configure(activebackground="#f9f9f9")
		self.cloudservice_label.configure(activeforeground="black")
		self.cloudservice_label.configure(background="#ffffff")
		self.cloudservice_label.configure(disabledforeground="#a3a3a3")
		self.cloudservice_label.configure(foreground="#000000")
		self.cloudservice_label.configure(highlightbackground="#d9d9d9")
		self.cloudservice_label.configure(highlightcolor="black")
		self.cloudservice_label.configure(text='''Cloud Service:''')

		self.accountname_label = Label(self.accountdetails_frame)
		self.accountname_label.place(relx=0.16, rely=0.42, height=21, width=92)
		self.accountname_label.configure(activebackground="#f9f9f9")
		self.accountname_label.configure(activeforeground="black")
		self.accountname_label.configure(background="#ffffff")
		self.accountname_label.configure(disabledforeground="#a3a3a3")
		self.accountname_label.configure(foreground="#000000")
		self.accountname_label.configure(highlightbackground="#d9d9d9")
		self.accountname_label.configure(highlightcolor="black")
		self.accountname_label.configure(text='''Account Name:''')

		self.freespace_label = Label(self.accountdetails_frame)
		self.freespace_label.place(relx=0.16, rely=0.51, height=21, width=68)
		self.freespace_label.configure(activebackground="#f9f9f9")
		self.freespace_label.configure(activeforeground="black")
		self.freespace_label.configure(background="#ffffff")
		self.freespace_label.configure(disabledforeground="#a3a3a3")
		self.freespace_label.configure(foreground="#000000")
		self.freespace_label.configure(highlightbackground="#d9d9d9")
		self.freespace_label.configure(highlightcolor="black")
		self.freespace_label.configure(text='''Free Space:''')

		self.logout_button = Button(self.accountdetails_frame)
		self.logout_button.place(relx=0.16, rely=0.79, height=24, width=69)
		self.logout_button.configure(activebackground="#d9d9d9")
		self.logout_button.configure(activeforeground="#000000")
		self.logout_button.configure(background="#d9d9d9")
		self.logout_button.configure(disabledforeground="#a3a3a3")
		self.logout_button.configure(foreground="#000000")
		self.logout_button.configure(highlightbackground="#d9d9d9")
		self.logout_button.configure(highlightcolor="black")
		self.logout_button.configure(pady="0")
		self.logout_button.configure(text='''Logout''')

		self.viewInWeb_button = Button(self.accountdetails_frame)
		self.viewInWeb_button.place(relx=0.51, rely=0.79, height=24, width=76)
		self.viewInWeb_button.configure(activebackground="#d9d9d9")
		self.viewInWeb_button.configure(activeforeground="#000000")
		self.viewInWeb_button.configure(background="#d9d9d9")
		self.viewInWeb_button.configure(disabledforeground="#a3a3a3")
		self.viewInWeb_button.configure(foreground="#000000")
		self.viewInWeb_button.configure(highlightbackground="#d9d9d9")
		self.viewInWeb_button.configure(highlightcolor="black")
		self.viewInWeb_button.configure(pady="0")
		self.viewInWeb_button.configure(text='''View In Web''')

		self.schedule_frame = Frame(self)
		self.schedule_frame.place(relx=0.07, rely=0.33, relheight=0.19, relwidth=0.57)
		self.schedule_frame.configure(relief=GROOVE)
		self.schedule_frame.configure(borderwidth="2")
		self.schedule_frame.configure(relief=GROOVE)
		self.schedule_frame.configure(background="#d9d9d9")
		self.schedule_frame.configure(highlightbackground="#d9d9d9")
		self.schedule_frame.configure(highlightcolor="black")
		self.schedule_frame.configure(width=575)

		self.monday_frame = Frame(self.schedule_frame)
		self.monday_frame.place(relx=0.02, rely=0.26, relheight=0.65, relwidth=0.13)
		self.monday_frame.configure(relief=GROOVE)
		self.monday_frame.configure(borderwidth="2")
		self.monday_frame.configure(relief=GROOVE)
		self.monday_frame.configure(background="#d9d9d9")
		self.monday_frame.configure(highlightbackground="#d9d9d9")
		self.monday_frame.configure(highlightcolor="black")
		self.monday_frame.configure(width=75)

		self.monday_button = DayButton(self.monday_frame, Weekday.MONDAY)
		self.monday_button.place(relx=0.0, rely=0.0, height=74, width=77)
		self.monday_button.configure(activebackground="#d9d9d9")
		self.monday_button.configure(activeforeground="#000000")
		self.monday_button.configure(background="#d9d9d9")
		self.monday_button.configure(disabledforeground="#a3a3a3")
		self.monday_button.configure(foreground="#000000")
		self.monday_button.configure(highlightbackground="#d9d9d9")
		self.monday_button.configure(highlightcolor="black")
		self.monday_button.configure(pady="0")
		self.monday_button.configure(relief=GROOVE)
		self.monday_button.configure(text='''Not Syncing''')
		self.monday_button.configure(command = self.monday_button.toggleSync)
		self.buttons.append(self.monday_button)

		self.tuesday_frame = Frame(self.schedule_frame)
		self.tuesday_frame.place(relx=0.16, rely=0.26, relheight=0.65, relwidth=0.13)
		self.tuesday_frame.configure(relief=GROOVE)
		self.tuesday_frame.configure(borderwidth="2")
		self.tuesday_frame.configure(relief=GROOVE)
		self.tuesday_frame.configure(background="#d9d9d9")
		self.tuesday_frame.configure(highlightbackground="#d9d9d9")
		self.tuesday_frame.configure(highlightcolor="black")
		self.tuesday_frame.configure(width=75)

		self.tuesday_button = DayButton(self.tuesday_frame, Weekday.TUESDAY)
		self.tuesday_button.place(relx=0.0, rely=0.0, height=74, width=77)
		self.tuesday_button.configure(activebackground="#d9d9d9")
		self.tuesday_button.configure(activeforeground="#000000")
		self.tuesday_button.configure(background="#d9d9d9")
		self.tuesday_button.configure(disabledforeground="#a3a3a3")
		self.tuesday_button.configure(foreground="#000000")
		self.tuesday_button.configure(highlightbackground="#d9d9d9")
		self.tuesday_button.configure(highlightcolor="black")
		self.tuesday_button.configure(pady="0")
		self.tuesday_button.configure(relief=GROOVE)
		self.tuesday_button.configure(text='''Not Syncing''')
		self.tuesday_button.configure(command = self.tuesday_button.toggleSync)
		self.buttons.append(self.tuesday_button)

		self.wednsday_frame = Frame(self.schedule_frame)
		self.wednsday_frame.place(relx=0.3, rely=0.26, relheight=0.65, relwidth=0.13)
		self.wednsday_frame.configure(relief=GROOVE)
		self.wednsday_frame.configure(borderwidth="2")
		self.wednsday_frame.configure(relief=GROOVE)
		self.wednsday_frame.configure(background="#d9d9d9")
		self.wednsday_frame.configure(highlightbackground="#d9d9d9")
		self.wednsday_frame.configure(highlightcolor="black")
		self.wednsday_frame.configure(width=75)

		self.wednsday_button = DayButton(self.wednsday_frame, Weekday.WEDNESDAY)
		self.wednsday_button.place(relx=0.0, rely=0.0, height=74, width=77)
		self.wednsday_button.configure(activebackground="#d9d9d9")
		self.wednsday_button.configure(activeforeground="#000000")
		self.wednsday_button.configure(background="#d9d9d9")
		self.wednsday_button.configure(disabledforeground="#a3a3a3")
		self.wednsday_button.configure(foreground="#000000")
		self.wednsday_button.configure(highlightbackground="#d9d9d9")
		self.wednsday_button.configure(highlightcolor="black")
		self.wednsday_button.configure(pady="0")
		self.wednsday_button.configure(relief=GROOVE)
		self.wednsday_button.configure(text='''Not Syncing''')
		self.wednsday_button.configure(command = self.wednsday_button.toggleSync)
		self.buttons.append(self.wednsday_button)

		self.thursday_frame = Frame(self.schedule_frame)
		self.thursday_frame.place(relx=0.43, rely=0.26, relheight=0.65, relwidth=0.13)
		self.thursday_frame.configure(relief=GROOVE)
		self.thursday_frame.configure(borderwidth="2")
		self.thursday_frame.configure(relief=GROOVE)
		self.thursday_frame.configure(background="#d9d9d9")
		self.thursday_frame.configure(highlightbackground="#d9d9d9")
		self.thursday_frame.configure(highlightcolor="black")
		self.thursday_frame.configure(width=75)

		self.thursday_button = DayButton(self.thursday_frame, Weekday.THURSDAY)
		self.thursday_button.place(relx=0.0, rely=0.0, height=74, width=77)
		self.thursday_button.configure(activebackground="#d9d9d9")
		self.thursday_button.configure(activeforeground="#000000")
		self.thursday_button.configure(background="#d9d9d9")
		self.thursday_button.configure(disabledforeground="#a3a3a3")
		self.thursday_button.configure(foreground="#000000")
		self.thursday_button.configure(highlightbackground="#d9d9d9")
		self.thursday_button.configure(highlightcolor="black")
		self.thursday_button.configure(pady="0")
		self.thursday_button.configure(relief=GROOVE)
		self.thursday_button.configure(text='''Not Syncing''')
		self.thursday_button.configure(command = self.thursday_button.toggleSync)
		self.buttons.append(self.thursday_button)

		self.friday_frame = Frame(self.schedule_frame)
		self.friday_frame.place(relx=0.57, rely=0.26, relheight=0.65, relwidth=0.13)
		self.friday_frame.configure(relief=GROOVE)
		self.friday_frame.configure(borderwidth="2")
		self.friday_frame.configure(relief=GROOVE)
		self.friday_frame.configure(background="#d9d9d9")
		self.friday_frame.configure(highlightbackground="#d9d9d9")
		self.friday_frame.configure(highlightcolor="black")
		self.friday_frame.configure(width=75)

		self.friday_button = DayButton(self.friday_frame, Weekday.FRIDAY)
		self.friday_button.place(relx=0.0, rely=0.0, height=74, width=77)
		self.friday_button.configure(activebackground="#d9d9d9")
		self.friday_button.configure(activeforeground="#000000")
		self.friday_button.configure(background="#d9d9d9")
		self.friday_button.configure(disabledforeground="#a3a3a3")
		self.friday_button.configure(foreground="#000000")
		self.friday_button.configure(highlightbackground="#d9d9d9")
		self.friday_button.configure(highlightcolor="black")
		self.friday_button.configure(pady="0")
		self.friday_button.configure(relief=GROOVE)
		self.friday_button.configure(text='''Not Syncing''')
		self.friday_button.configure(command = self.friday_button.toggleSync)
		self.buttons.append(self.friday_button)

		self.saturday_frame = Frame(self.schedule_frame, )
		self.saturday_frame.place(relx=0.71, rely=0.26, relheight=0.65, relwidth=0.13)
		self.saturday_frame.configure(relief=GROOVE)
		self.saturday_frame.configure(borderwidth="2")
		self.saturday_frame.configure(relief=GROOVE)
		self.saturday_frame.configure(background="#d9d9d9")
		self.saturday_frame.configure(highlightbackground="#d9d9d9")
		self.saturday_frame.configure(highlightcolor="black")
		self.saturday_frame.configure(width=75)

		self.saturday_button = DayButton(self.saturday_frame, Weekday.SATURDAY)
		self.saturday_button.place(relx=0.0, rely=0.0, height=74, width=77)
		self.saturday_button.configure(activebackground="#d9d9d9")
		self.saturday_button.configure(activeforeground="#000000")
		self.saturday_button.configure(background="#d9d9d9")
		self.saturday_button.configure(disabledforeground="#a3a3a3")
		self.saturday_button.configure(foreground="#000000")
		self.saturday_button.configure(highlightbackground="#d9d9d9")
		self.saturday_button.configure(highlightcolor="black")
		self.saturday_button.configure(pady="0")
		self.saturday_button.configure(relief=GROOVE)
		self.saturday_button.configure(text='''Not Syncing''')
		self.saturday_button.configure(command = self.saturday_button.toggleSync)
		self.buttons.append(self.saturday_button)

		self.sunday_frame = Frame(self.schedule_frame)
		self.sunday_frame.place(relx=0.85, rely=0.26, relheight=0.65, relwidth=0.13)
		self.sunday_frame.configure(relief=GROOVE)
		self.sunday_frame.configure(borderwidth="2")
		self.sunday_frame.configure(relief=GROOVE)
		self.sunday_frame.configure(background="#d9d9d9")
		self.sunday_frame.configure(highlightbackground="#d9d9d9")
		self.sunday_frame.configure(highlightcolor="black")
		self.sunday_frame.configure(width=75)

		self.sunday_button = DayButton(self.sunday_frame, Weekday.SUNDAY)
		self.sunday_button.place(relx=0.0, rely=0.0, height=74, width=77)
		self.sunday_button.configure(activebackground="#d9d9d9")
		self.sunday_button.configure(activeforeground="#000000")
		self.sunday_button.configure(background="#d9d9d9")
		self.sunday_button.configure(disabledforeground="#a3a3a3")
		self.sunday_button.configure(foreground="#000000")
		self.sunday_button.configure(highlightbackground="#d9d9d9")
		self.sunday_button.configure(highlightcolor="black")
		self.sunday_button.configure(pady="0")
		self.sunday_button.configure(relief=GROOVE)
		self.sunday_button.configure(text='''Not Syncing''')
		self.sunday_button.configure(command = self.sunday_button.toggleSync)
		self.buttons.append(self.sunday_button)

		self.monday_label = Label(self.schedule_frame)
		self.monday_label.place(relx=0.03, rely=0.09, height=21, width=50)
		self.monday_label.configure(activebackground="#f9f9f9")
		self.monday_label.configure(activeforeground="black")
		self.monday_label.configure(background="#d9d9d9")
		self.monday_label.configure(disabledforeground="#a3a3a3")
		self.monday_label.configure(foreground="#000000")
		self.monday_label.configure(highlightbackground="#d9d9d9")
		self.monday_label.configure(highlightcolor="black")
		self.monday_label.configure(text='''Monday''')

		self.tuesday_label = Label(self.schedule_frame)
		self.tuesday_label.place(relx=0.19, rely=0.09, height=21, width=50)
		self.tuesday_label.configure(activebackground="#f9f9f9")
		self.tuesday_label.configure(activeforeground="black")
		self.tuesday_label.configure(background="#d9d9d9")
		self.tuesday_label.configure(disabledforeground="#a3a3a3")
		self.tuesday_label.configure(foreground="#000000")
		self.tuesday_label.configure(highlightbackground="#d9d9d9")
		self.tuesday_label.configure(highlightcolor="black")
		self.tuesday_label.configure(text='''Tuesday''')

		self.wednsday_label = Label(self.schedule_frame)
		self.wednsday_label.place(relx=0.31, rely=0.09, height=21, width=61)
		self.wednsday_label.configure(activebackground="#f9f9f9")
		self.wednsday_label.configure(activeforeground="black")
		self.wednsday_label.configure(background="#d9d9d9")
		self.wednsday_label.configure(disabledforeground="#a3a3a3")
		self.wednsday_label.configure(foreground="#000000")
		self.wednsday_label.configure(highlightbackground="#d9d9d9")
		self.wednsday_label.configure(highlightcolor="black")
		self.wednsday_label.configure(text='''Wednsday''')

		self.thursday_label = Label(self.schedule_frame)
		self.thursday_label.place(relx=0.45, rely=0.09, height=21, width=55)
		self.thursday_label.configure(activebackground="#f9f9f9")
		self.thursday_label.configure(activeforeground="black")
		self.thursday_label.configure(background="#d9d9d9")
		self.thursday_label.configure(disabledforeground="#a3a3a3")
		self.thursday_label.configure(foreground="#000000")
		self.thursday_label.configure(highlightbackground="#d9d9d9")
		self.thursday_label.configure(highlightcolor="black")
		self.thursday_label.configure(text='''Thursday''')

		self.friday_label = Label(self.schedule_frame)
		self.friday_label.place(relx=0.61, rely=0.09, height=21, width=38)
		self.friday_label.configure(activebackground="#f9f9f9")
		self.friday_label.configure(activeforeground="black")
		self.friday_label.configure(background="#d9d9d9")
		self.friday_label.configure(disabledforeground="#a3a3a3")
		self.friday_label.configure(foreground="#000000")
		self.friday_label.configure(highlightbackground="#d9d9d9")
		self.friday_label.configure(highlightcolor="black")
		self.friday_label.configure(text='''Friday''')

		self.saturday_label = Label(self.schedule_frame)
		self.saturday_label.place(relx=0.73, rely=0.09, height=21, width=54)
		self.saturday_label.configure(activebackground="#f9f9f9")
		self.saturday_label.configure(activeforeground="black")
		self.saturday_label.configure(background="#d9d9d9")
		self.saturday_label.configure(disabledforeground="#a3a3a3")
		self.saturday_label.configure(foreground="#000000")
		self.saturday_label.configure(highlightbackground="#d9d9d9")
		self.saturday_label.configure(highlightcolor="black")
		self.saturday_label.configure(text='''Saturday''')

		self.sunday_label = Label(self.schedule_frame)
		self.sunday_label.place(relx=0.87, rely=0.09, height=21, width=45)
		self.sunday_label.configure(activebackground="#f9f9f9")
		self.sunday_label.configure(activeforeground="black")
		self.sunday_label.configure(background="#d9d9d9")
		self.sunday_label.configure(disabledforeground="#a3a3a3")
		self.sunday_label.configure(foreground="#000000")
		self.sunday_label.configure(highlightbackground="#d9d9d9")
		self.sunday_label.configure(highlightcolor="black")
		self.sunday_label.configure(text='''Sunday''')


