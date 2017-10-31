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

		self.cloud = GDrive() # TODO: Add the selected option unstead of static GDrive
		self.folders = []
		# NOTICE: Add folders here for testing
		self.folders.append("Put test folder here!")

		# load JSON
		with open('options.json') as data_file:    
			self.options = json.load(data_file)

		self.weekday_sync = self.options["days"]

		self.p1 = SelectPage(self.root)
		self.p2 = LoadingPage(self.root)
		self.p3 = MainPage(self.root)

		self.p1.gdrive.button.bind("<Button-1>", self.callback)
		self.p1.pack()

		# Make buttons have the JSON saved states
		for button in self.p3.buttons:
			if button.day == Weekday.MONDAY and button.syncing != self.weekday_sync[0]:
				button.toggleSync()

			elif button.day == Weekday.TUESDAY  and button.syncing != self.weekday_sync[1]:
				button.toggleSync()

			elif button.day == Weekday.WEDNESDAY  and button.syncing != self.weekday_sync[2]:
				button.toggleSync()

			elif button.day == Weekday.THURSDAY  and button.syncing != self.weekday_sync[3]:
				button.toggleSync()

			elif button.day == Weekday.FRIDAY  and button.syncing != self.weekday_sync[4]:
				button.toggleSync()

			elif button.day == Weekday.SATURDAY  and button.syncing != self.weekday_sync[5]:
				button.toggleSync()

			elif button.day == Weekday.SUNDAY  and button.syncing != self.weekday_sync[6]:
				button.toggleSync()

	# Google Drive Option
	def gdrive_mousedown(self):
		self.p1.pack_forget()
		self.p2.pack()
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

	def backup(self, zipname, directory):
		self.cloud.zipFolder(zipname, directory)
		self.cloud.upload(zipname)

	def update_syncdays(self, event):
		for button in self.p3.buttons:
			if button.day == Weekday.MONDAY:
				self.options["days"][0]['monday'] = button.syncing

			elif button.day == Weekday.TUESDAY:
				self.options["days"][1]['tuesday'] = button.syncing

			elif button.day == Weekday.WEDNESDAY:
				self.options["days"][2]['wednesday'] = button.syncing

			elif button.day == Weekday.THURSDAY:
				self.options["days"][3]['thursday'] = button.syncing

			elif button.day == Weekday.FRIDAY:
				self.options["days"][4]['friday'] = button.syncing

			elif button.day == Weekday.SATURDAY:
				self.options["days"][5]['saturday'] = button.syncing

			elif button.day == Weekday.SUNDAY:
				self.options["days"][6]['sunday'] = button.syncing

			# Save updated JSON
			with open('options.json', 'w') as f:
				f.write(json.dumps(self.options, indent=4, separators=(',', ': ')))
