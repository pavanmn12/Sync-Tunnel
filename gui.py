from tkinter import *
from pages import *
from cloudservices import *
import threading
from enum import Enum

# Google Drive Option
def on_click_1():
	p1.pack_forget()
	p2.pack()
	cloud = GDrive()
	p2.pack_forget()
	root.geometry("1000x600")
	p3.pack(expand=True, fill='both')
	p3.logbox.add_msg("Google Drive Authenticated")

def thread_start(self):
	t = threading.Thread(target=on_click_1)
	t.start()

if __name__ == '__main__':
	root = Tk()
	root.title("Backup Software")
	root.geometry("500x300")
	root.configure(bg='white')

	folders = []

	p1 = SelectPage(root)
	p2 = LoadingPage(root)
	p3 = MainPage(root)

	p1.gdrive.button.bind("<Button-1>", thread_start)
	p1.pack()
	root.mainloop()