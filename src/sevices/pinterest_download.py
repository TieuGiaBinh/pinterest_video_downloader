from pathlib import Path
import yt_dlp
from src.interfaces.pinterest_download_interfaces import PinterestDownloadInterfaces


class PinterestDownload(PinterestDownloadInterfaces):

    def __init__(self, video: Video):
      
        self.url = video.pinterest_link
        self.id = video.id
        self.output_dir = 'download'


    def download_with_yt_dlp(self) -> str:

        output_path = Path(self.output_dir)
        output_path.mkdir(parents = True, exist_ok = True)

        filename = f'{self.id}_%(id)s.%(ext)s'
        yt_dlp_opts = {
        "outtmpl": str(output_path / filename),
        "format": (
            "bestvideo[ext=mp4]+bestaudio[ext=m4a]/"
            "best[ext=mp4]/"
            "best"
            ),
        "merge_output_format": "mp4",
        "noplaylist": True,
        }
        with yt_dlp.YoutubeDL(yt_dlp_opts) as dlp:
          info = dlp.extract_info(self.url, download = True)
          downloaded_file = dlp.prepare_filename(info)

        downloaded_path = Path(downloaded_file)

        if downloaded_path.suffix != '.mp4':
          mp4_path = downloaded_path.with_suffix('.mp4')

          if mp4_path.exist():
            return mp4_path

        return downloaded_path
        
