import gui
import winreg
from sys import platform
import json
import os
import schedule
from time import sleep
import datetime

def backup():
	# Backing up
	now = datetime.datetime.now()
	for f in app.folders:
		zipname = str(os.path.basename(f)).replace(" ", "") + str(now.strftime("%Y-%m-%d-%H")) + ".zip"
		app.backup(zipname, f)
	# Backup complete!

	# Remove zipped files
	os.remove(zipname)

def setSchedule():
	temp_dictonary = {}
	for day_data in options["days"]:
		temp_dictonary.update(day_data)

	if temp_dictonary["monday"] == True:
		schedule.every().monday.do(backup).tag('day')
	if temp_dictonary["tuesday"] == True:
		schedule.every().tuesday.do(backup).tag('day')
	if temp_dictonary["wednesday"] == True:
		schedule.every().wednesday.do(backup).tag('day')
	if temp_dictonary["thursday"] == True:
		schedule.every().thursday.do(backup).tag('day')
	if temp_dictonary["friday"] == True:
		schedule.every().friday.do(backup).tag('day')
	if temp_dictonary["saturday"] == True:
		schedule.every().saturday.do(backup).tag('day')
	if temp_dictonary["sunday"] == True:
		schedule.every().sunday.do(backup).tag('day')


if __name__ == '__main__':

	app = gui.App()

	while True:

		# Get JSON Options
		with open('options.json') as data_file:    
			options = json.load(data_file)

		# First Time Run
		if options["options"]["setupcomplete"] == False:

			# Windows
			if platform == "win32":
				# TODO: Add startup
				app.p3.logbox.add_msg("Windows OS detected")

			# Mac
			elif platform == "darwin":
				# TODO: Add startup
				app.p3.logbox.add_msg("Mac OS detected")

			# Linux
			if platform == "linux" or platform == "linux2":
				# TODO: Add startup
				app.p3.logbox.add_msg("Linux OS detected")

			# Update JSON for setupcomplete
			options["options"]["setupcomplete"] == True
			with open('options.json', 'w') as f:
				f.write(json.dumps(options, sort_keys=True, indent=4, separators=(',', ': ')))

			# Start GUI
			app.root.mainloop()
			setSchedule()
			options["options"]["setupcomplete"] = True # Setup Complete

			# Save updated JSON
			with open('options.json', 'w') as f:
				f.write(json.dumps(options, sort_keys=True, indent=4, separators=(',', ': ')))
		
		else: 
			last_json_change = os.stat('options.json').st_mtime

			# Schedule Backups
			setSchedule()

			# Idle
			while True:
				schedule.run_pending()
				sleep(5)

				file_modify = os.stat('options.json').st_mtime

				if last_json_change != file_modify:
					# Get JSON Options
					last_json_change = file_modify
					with open('options.json') as data_file:    
						options = json.load(data_file)
					schedule.clear('day')
					setSchedule()
