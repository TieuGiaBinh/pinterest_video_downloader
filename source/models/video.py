from enum import Enum
from dataclasses import dataclass

class VideoStatus(Enum):
  PENDING = "Pending"
  DOWNLOADED = "Downloaded"
  UPLOADED = "Uploaded"
  FAIL = "Fail"

@dataclass
class Video:
  id: str
  pinterest_url: str
  status: VideoStatus
  dropbox_path: str | None = None
  error_msg: str | None = None
  
