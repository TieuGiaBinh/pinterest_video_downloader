from pathlib import Path
from src.clients.interfaces import (DropboxClient, GoogleSheetsClient, PinterestDownloader)


class VideoProcessingService:

    def __init__(self, sheets: GoogleSheetsClient, pinterest: PinterestDownloader, dropbox: DropboxClient):
        self.sheets = sheets
        self.pinterest = pinterest
        self.dropbox = dropbox

    def process_pending_videos(self) -> None:

        videos = self.sheets.get_pending_videos()

        for video in videos:
            self._process_video(video)

    def _process_video(self, video) -> None:

        file_path: Path | None = None

        try:

            # 1. Download
            file_path = self.pinterest.download(video)

            # 2. Validate
            self._validate_file(file_path)

            # 3. Upload
            dropbox_path = self._build_dropbox_path(video.id)

            uploaded_path = self.dropbox.upload(file_path, dropbox_path)

            # 4. Update Google Sheets
            self.sheets.mark_as_uploaded(video, uploaded_path)

        except Exception as error:

            self.sheets.mark_as_failed(video, str(error))

        finally:

            # 5. Cleanup
            self._cleanup(file_path)

    @staticmethod
    def _build_dropbox_path(video_id: str) -> str:

        return f"/videos/{video_id}.mp4"

    @staticmethod
    def _validate_file(file_path: Path) -> None:

        if not file_path.exists():
            raise RuntimeError("Downloaded file does not exist")

        if file_path.stat().st_size == 0:
            raise RuntimeError("Downloaded file is empty")

    @staticmethod
    def _cleanup(file_path: Path | None) -> None:

        if file_path is not None:
            file_path.unlink(missing_ok=True)
