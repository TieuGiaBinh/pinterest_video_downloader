from src.clients.interfaces import (GoogleSheetsClient, PinterestDownloader, DropboxClient)


class VideoProcessingService:

    def __init__(self, sheets: GoogleSheetsClient, pinterest: PinterestDownloader, dropbox: DropboxClient):
        self.sheets = sheets
        self.pinterest = pinterest
        self.dropbox = dropbox

    def process_pending_videos(self) -> None:

        videos = self.sheets.get_pending_videos()

        for video in videos:

            try:
                file_path = self.pinterest.download(video)

                dropbox_path = self.dropbox.upload(file_path, f"/videos/{video.id}.mp4")

                self.sheets.mark_as_uploaded(video, dropbox_path)

            except Exception as error:

                self.sheets.mark_as_failed(video, str(error))
