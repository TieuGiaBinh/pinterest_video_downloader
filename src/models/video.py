from dataclasses import dataclass


@dataclass
class Video:
    id: str
    pinterest_link: str
    download_status: str
    dropbox_uploaded: str
    remark: str
