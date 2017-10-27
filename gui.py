from tkinter import *
from pages import *
from cloudservices import *
import threading
from enum import Enum
import json
import webbrowser

class App:
	def __init__(self):
		self.root = Tk()
		self.root.title("Backup Software")
		self.root.geometry("500x300")
		self.root.configure(bg='white')

		self.folders = []
		self.cloud = None

		# load JSON
		with open('syncdays.json') as data_file:    
			self.weekday_sync = json.load(data_file)

		self.p1 = SelectPage(self.root)
		self.p2 = LoadingPage(self.root)
		self.p3 = MainPage(self.root)

		self.p1.gdrive.button.bind("<Button-1>", self.callback)
		self.p1.pack()

		# Make buttons have the JSON saved states
		for button in self.p3.buttons:
			if button.day == Weekday.MONDAY and button.syncing != self.weekday_sync['monday']:
				button.toggleSync()

			elif button.day == Weekday.TUESDAY  and button.syncing != self.weekday_sync['tuesday']:
				button.toggleSync()

			elif button.day == Weekday.WEDNESDAY  and button.syncing != self.weekday_sync['wednesday']:
				button.toggleSync()

			elif button.day == Weekday.THURSDAY  and button.syncing != self.weekday_sync['thursday']:
				button.toggleSync()

			elif button.day == Weekday.FRIDAY  and button.syncing != self.weekday_sync['friday']:
				button.toggleSync()

			elif button.day == Weekday.SATURDAY  and button.syncing != self.weekday_sync['saturday']:
				button.toggleSync()

			elif button.day == Weekday.SUNDAY  and button.syncing != self.weekday_sync['sunday']:
				button.toggleSync()

		self.root.mainloop()

	# Google Drive Option
	def gdrive_mousedown(self):
		self.p1.pack_forget()
		self.p2.pack()
		self.cloud = GDrive()
		self.p2.pack_forget()
		self.root.geometry("1000x600")
		self.p3.pack(expand=True, fill='both')
		self.p3.logbox.add_msg("Google Drive Authenticated")
		self.p3.viewInWeb_button.configure(command = self.view_in_web)
		self.root.bind("<Button-1>", self.update_syncdays)

	def callback(self, event):
		t = threading.Thread(target=self.gdrive_mousedown)
		t.start()

	def view_in_web(self):
		webbrowser.open(self.cloud.homepage, new=2)

	def update_syncdays(self, event):
		for button in self.p3.buttons:
			if button.day == Weekday.MONDAY:
				self.weekday_sync['monday'] = button.syncing

			elif button.day == Weekday.TUESDAY:
				self.weekday_sync['tuesday'] = button.syncing

			elif button.day == Weekday.WEDNESDAY:
				self.weekday_sync['wednesday'] = button.syncing

			elif button.day == Weekday.THURSDAY:
				self.weekday_sync['thursday'] = button.syncing

			elif button.day == Weekday.FRIDAY:
				self.weekday_sync['friday'] = button.syncing

			elif button.day == Weekday.SATURDAY:
				self.weekday_sync['saturday'] = button.syncing

			elif button.day == Weekday.SUNDAY:
				self.weekday_sync['sunday'] = button.syncing

			# Save updated JSON
			with open('syncdays.json', 'w') as f:
				f.write(json.dumps(self.weekday_sync))


if __name__ == '__main__':
	app = App()