from pathlib import Path
from source.clients.dropbox import DropboxAPIClient
from source.clients.google_sheets import GoogleSheetsAPIClient
from source.clients.pinterest_downloader import HttpVideoDownloader
from source.config.settings import Settings
from source.services.video_processor import VideoProcessingService


def main():

    settings = Settings.from_environment()

    sheets = GoogleSheetsAPIClient(spreadsheet_id=settings.google_spreadsheet_id, credentials_file=Path(settings.google_service_account_file))

    dropbox = DropboxAPIClient(access_token=settings.dropbox_access_token)

    # Pinterest implementation sẽ được inject ở đây.
    pinterest = HttpVideoDownloader()

    service = VideoProcessingService(sheets=sheets, pinterest=pinterest, dropbox=dropbox)

    service.process_pending_videos()


if __name__ == "__main__":
    main()
