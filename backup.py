from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import zipfile
import os
import sys
import datetime

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
folders = []

def zipFolder(foldername, target_dir):            
    zipobj = zipfile.ZipFile(foldername + '.zip', 'w', zipfile.ZIP_DEFLATED)
    rootlen = len(target_dir) + 1
    for base, dirs, files in os.walk(target_dir):
        for file in files:
            fn = os.path.join(base, file)
            zipobj.write(fn, fn[rootlen:])

def uploadZip(target_dir):
	file1 = drive.CreateFile({'title': 'test.zip'}) 
	file1.SetContentFile(target_dir);
	file1.Upload()

folders.append("F:\\Pictures\\logos")
folders.append("F:\\Pictures\\Uplay")

now = datetime.datetime.now()
for f in folders:
	zipname = str(os.path.basename(f)).replace(" ", "") + str(now.strftime("%Y-%m-%d-%H"))
	zipFolder(zipname, f)	
	uploadZip(zipname)