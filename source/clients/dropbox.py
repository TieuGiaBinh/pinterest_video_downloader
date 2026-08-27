from pathlib import Path
import dropbox
from dropbox.files import CommitInfo
from dropbox.exceptions import ApiError


class DropboxAPIClient:

    CHUNK_SIZE = 4 * 1024 * 1024

    def __init__(self, access_token: str):
        self.client = dropbox.Dropbox(access_token)

    def upload(self, file_path: Path, destination: str) -> str:

        file_size = file_path.stat().st_size

        if file_size <= self.CHUNK_SIZE:
            return self._upload_small_file(file_path, destination)

        return self._upload_large_file(file_path, destination)

    def _upload_small_file(self, file_path: Path, destination: str) -> str:

        with file_path.open("rb") as file:
            self.client.files_upload(file.read(), destination, mode=dropbox.files.WriteMode.overwrite)

        return destination

    def _upload_large_file(self, file_path: Path, destination: str) -> str:

        with file_path.open("rb") as file:

            first_chunk = file.read(self.CHUNK_SIZE)

            session = self.client.files_upload_session_start(first_chunk)

            cursor = dropbox.files.UploadSessionCursor(session_id=session.session_id, offset=len(first_chunk))

            commit = dropbox.files.CommitInfo(path=destination, mode=dropbox.files.WriteMode.overwrite)

            while True:
    
                chunk = file.read(self.CHUNK_SIZE)
    
                if not chunk:
                    break
    
                self.client.files_upload_session_append_v2(chunk, cursor)
    
                cursor.offset += len(chunk)
    
            self.client.files_upload_session_finish(b"", cursor, commit)

        return destination
