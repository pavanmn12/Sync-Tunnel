from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth


class CloudService:
    def zipFolder(self, zipname, directory):            
    	zipobj = zipfile.ZipFile(zipname + '.zip', 'w', zipfile.ZIP_DEFLATED)
    	rootlen = len(target_dir) + 1
    	for base, dirs, files in os.walk(target_dir):
        	for file in files:
        		fn = os.path.join(base, file)
        		zipobj.write(fn, fn[rootlen:])


# Google Drive Module
class GDrive(CloudService):
	def __init__(self):
		self.homepage = r"https://drive.google.com/drive/u/"
		# Login
		gauth = GoogleAuth()
		gauth.LoadCredentialsFile("credentials.json")
		if gauth.credentials is None:
   			gauth.LocalWebserverAuth()
		elif gauth.access_token_expired:
			gauth.Refresh()
		else:
			gauth.Authorize()
		gauth.SaveCredentialsFile("credentials.json")
		drive = GoogleDrive(gauth)

	def upload(self, directory):
		file = drive.CreateFile({'title': 'test.zip'}) 
		file.SetContentFile(target_dir);
		file.Upload()
