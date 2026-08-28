import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:

    google_spreadsheet_id: str
    google_service_account_file: str
    dropbox_access_token: str

    @classmethod
    def from_environment(cls):

        return cls(
            google_spreadsheet_id=os.environ[
                "GOOGLE_SPREADSHEET_ID"
            ],
            google_service_account_file=os.environ[
                "GOOGLE_SERVICE_ACCOUNT_FILE"
            ],
            dropbox_access_token=os.environ[
                "DROPBOX_ACCESS_TOKEN"
            ],
        )
