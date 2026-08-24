from pathlib import Path
from typing import Protocol
from src.models.video import Video


class GoogleSheetsClient(Protocol):

    def get_pending_videos(self) -> list[Video]:
        ...

    def mark_as_uploaded(self, video: Video,vdropbox_path: str) -> None:
        ...

    def mark_as_failed(self, video: Video, error_message: str) -> None:
        ...


class PinterestDownloader(Protocol):

    def download(self, video: Video) -> Path:
        ...


class DropboxClient(Protocol):

    def upload(self, file_path: Path, destination: str) -> str:
        ...
