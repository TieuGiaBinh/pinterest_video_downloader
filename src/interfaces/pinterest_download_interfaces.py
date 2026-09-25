from abc import ABC, abstractmethod


class PinterestDownloadInterfaces(ABC):
    @abstractmethod
    def download_with_yt_dlp(self) -> str:
        pass
