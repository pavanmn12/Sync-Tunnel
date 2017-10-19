from tkinter import *
from pages import *
from cloudservices import *
import threading

# Google Cloud Option
def onClick1():
	p1.pack_forget()
	p2.pack()
	cloud = GDrive()
	p2.pack_forget()
	p3.pack()

def thread_test(self):
	t = threading.Thread(target=onClick1)
	t.start()

if __name__ == '__main__':
	root = Tk()
	root.title("Backup Software")
	root.geometry("500x300")
	root.configure(bg='white')
	frame = Frame(root)

	p1 = SelectPage(root)
	p2 = LoadingPage(root)
	p3 = MainPage(root)

	p1.gdrive.button.bind("<Button-1>", thread_test)
	p1.pack()
	root.mainloop()