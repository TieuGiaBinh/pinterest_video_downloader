from pathlib import Path

import requests


class HttpVideoDownloader:

    def __init__(self, timeout: int = 30):
        self.timeout = timeout

    def download(self, video_url: str, output_path: Path) -> Path:

        response = requests.get(video_url, timeout=self.timeout, stream=True)

        response.raise_for_status()

        output_path.parent.mkdir(parents=True, exist_ok=True)

        with output_path.open("wb") as file:

            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)

        return output_path
