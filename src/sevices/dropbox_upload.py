import os
from pathlib import Path
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError


class DropboxUpload:

    CHUNK_SIZE = 4 * 1024 * 1024  #4MB

    def __init__(self, access_token, local_file, dropbox_path):
        self.dropbox_client = dropbox.Dropbox(access_token)
        self.local_file = local_file
        self.dropbox_path = dropbox_path


    def upload_small_file(self):
        pass


    def upload_large_file(self):
        pass


    def upload_file(self):
        pass


    def precondtion_upload_check(self):
        if not Path(self.local_file).exists():
            raise FileNotFoundError(f'File is not found at path {self.local_file}')
