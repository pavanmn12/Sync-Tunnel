from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth


class CloudService:
    def upload(self, directory): raise NotImplementedError


# Google Drive Module
class GDrive(CloudService):
    def __init__(self):
        gauth = GoogleAuth()
        gauth.LoadCredentialsFile("user_creds.txt")

        if gauth.credentials is None:
            gauth.LocalWebserverAuth()

        elif gauth.access_token_expired:
            gauth.Refresh()

        else:
            gauth.Authorize()

        gauth.SaveCredentialsFile("user_creds.txt")
        drive = GoogleDrive(gauth)

    def upload(self, directory):
        file = drive.CreateFile({'title': 'test.zip'})
        file.SetContentFile(target_dir)
        file.Upload()
