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
