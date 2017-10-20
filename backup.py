from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import zipfile
import os
import datetime

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
folders = []


def zip_folder(folder_name, target_dir):
    zipobj = zipfile.ZipFile(folder_name + '.zip', 'w', zipfile.ZIP_DEFLATED)
    rootlen = len(target_dir) + 1
    for base, dirs, files in os.walk(target_dir):
        for file in files:
            fn = os.path.join(base, file)
            zipobj.write(fn, fn[rootlen:])


def upload_zip(target_dir):
    file1 = drive.CreateFile({'title': 'test.zip'})
    file1.SetContentFile(target_dir);
    file1.Upload()


folders.append("F:\\Pictures\\logos")
folders.append("F:\\Pictures\\Uplay")

now = datetime.datetime.now()
for f in folders:
    zipname = str(os.path.basename(f)).replace(" ", "") + str(now.strftime("%Y-%m-%d-%H"))
    zip_folder(zipname, f)
    upload_zip(zipname)
