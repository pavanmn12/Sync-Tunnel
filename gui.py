from tkinter import *
from pages import *
from cloudservices import *
import threading
from enum import Enum
import json


# Google Drive Option
def on_click_1():
	p1.pack_forget()
	p2.pack()
	cloud = GDrive()
	p2.pack_forget()
	root.geometry("1000x600")
	p3.pack(expand=True, fill='both')
	p3.logbox.add_msg("Google Drive Authenticated")

def callback(self):
	t = threading.Thread(target=on_click_1)
	t.start()

def update_syncdays(self):
	for button in p3.buttons:
		if button.day == Weekday.MONDAY:
			weekday_sync['monday'] = button.syncing

		elif button.day == Weekday.TUESDAY:
			weekday_sync['tuesday'] = button.syncing

		elif button.day == Weekday.WEDNESDAY:
			weekday_sync['wednesday'] = button.syncing

		elif button.day == Weekday.THURSDAY:
			weekday_sync['thursday'] = button.syncing

		elif button.day == Weekday.FRIDAY:
			weekday_sync['friday'] = button.syncing

		elif button.day == Weekday.SATURDAY:
			weekday_sync['saturday'] = button.syncing

		elif button.day == Weekday.SUNDAY:
			weekday_sync['sunday'] = button.syncing

		# Save updated JSON
		with open('syncdays.json', 'w') as f:
			f.write(json.dumps(weekday_sync))


if __name__ == '__main__':
	root = Tk()
	root.title("Backup Software")
	root.geometry("500x300")
	root.configure(bg='white')

	folders = []

	# load JSON
	with open('syncdays.json') as data_file:    
		weekday_sync = json.load(data_file)

	p1 = SelectPage(root)
	p2 = LoadingPage(root)
	p3 = MainPage(root)

	p1.gdrive.button.bind("<Button-1>", callback)
	root.bind("<Button-1>", update_syncdays)
	p1.pack()
	root.mainloop()