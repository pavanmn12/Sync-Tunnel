from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import zipfile
import os

class CloudService(object):
    def zipFolder(self, zipname, directory):            
    	zipobj = zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED)
    	rootlen = len(directory) + 1
    	for base, dirs, files in os.walk(directory):
        	for file in files:
        		fn = os.path.join(base, file)
        		zipobj.write(fn, fn[rootlen:])


# Google Drive Module
class GDrive(CloudService):
	def __init__(self):
		CloudService.__init__(self)
		self.homepage = r"https://drive.google.com/drive/u/"
		# Login
		self.gauth = GoogleAuth()
		self.gauth.LoadCredentialsFile("credentials.json")
		if self.gauth.credentials is None:
   			self.gauth.LocalWebserverAuth()
		elif self.gauth.access_token_expired:
			self.gauth.Refresh()
		else:
			self.gauth.Authorize()
		self.gauth.SaveCredentialsFile("credentials.json")
		self.drive = GoogleDrive(self.gauth)

	def upload(self, uploadname):
		file = self.drive.CreateFile({'title': uploadname}) 
		file.SetContentFile(uploadname);
		file.Upload()
