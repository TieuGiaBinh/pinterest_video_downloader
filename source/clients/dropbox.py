from pathlib import Path
import dropbox
from dropbox.exceptions import ApiError


class DropboxAPIClient:

    def __init__(self, access_token: str):
        self.client = dropbox.Dropbox(access_token)

    def upload(self, file_path: Path, destination: str) -> str:

        with file_path.open("rb") as file:
            self.client.files_upload(file.read(), destination, mode=dropbox.files.WriteMode.overwrite)

        return destination
