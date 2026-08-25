from pathlib import Path
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from source.models.video import Video, VideoStatus


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets"
]


class GoogleSheetsAPIClient:

    def __init__(self, spreadsheet_id: str, credentials_file: Path):

        self.spreadsheet_id = spreadsheet_id

        credentials = Credentials.from_service_account_file(credentials_file, scopes=SCOPES)

        self.service = build("sheets", "v4", credentials=credentials)

    def get_pending_videos(self) -> list[Video]:

        response = (self.service.spreadsheets().values().get(spreadsheetId=self.spreadsheet_id, range="Videos!A2:E").execute())

        rows = response.get("values", [])

        videos = []

        for row in rows:

            if len(row) < 3:
                continue

            video_id = row[0]
            pinterest_url = row[1]
            status = row[2]

            if status != VideoStatus.PENDING.value:
                continue

            videos.append(
                Video(
                    id=video_id,
                    pinterest_url=pinterest_url,
                    status=VideoStatus.PENDING,
                    dropbox_path=row[3] if len(row) > 3 else None,
                    error_message=row[4] if len(row) > 4 else None,
                )
            )

        return videos
