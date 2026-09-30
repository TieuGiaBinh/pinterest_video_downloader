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


    def upload_small_file(self, file, file_size):
        if file_size <= self.CHUNK_SIZE:
            chunk = file.read(self.CHUNK_SIZE)
            self.dropbox_client.files_upload(chunk, self.dropbox_path, mode = WriteMode.overwrite)
            print('upload successful')


    def upload_large_file(self, file, file_size):
        chunk = file.read(self.CHUNK_SIZE)
        session_start = self.dropbox_client.files_upload_session_start(chunk)
        session_id = session_start.session_id
        offset = len(chunk)

        while offset < file_size:
            chunk = file.read(self.CHUNK_SIZE)
            
            if not chunk:
                break

            if offset + len(chunk) >= file_size:
                cursor = dropbox.files.UploadSessionCursor(session_id = session_id, offset = offset)
                commit = dropbox.files.CommitInfo(path = self.dropbox_path, mode = WriteMode.overwrite)
                self.dropbox_client.files_upload_session_finish(chunk, cursor, commit)
                offset += len(chunk)
            else:
                cursor = dropbox.
            


    def upload_file(self):
        pass


    def precondtion_upload_check(self):
        if not Path(self.local_file).exists():
            raise FileNotFoundError(f'File is not found at path {self.local_file}')
