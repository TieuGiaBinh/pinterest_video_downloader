from abc import ABC, abstractmethod
from src.models.video import Video


class VideoInterfaces (ABC):
    @abstractmethod
    def get_pending_videos(self) -> list[Video]:
        pass
