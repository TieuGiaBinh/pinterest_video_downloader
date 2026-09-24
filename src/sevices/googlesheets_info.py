from src.models.video import Video
from src.interfaces.googlesheets_interfaces import GoogleSheetsInterfaces


class GoogleSheetsInfo (GoogleSheetsInterfaces):
  
    def __init__(self, worksheet):
      
        self.worksheet = worksheet


    def get_pending_videos(self) -> list[Video]:
      
        records = self.worksheet.get_all_records()
      
        videos = []
      
        for record in records:
          
            if record['Download Status'] != 'Pending':
                continue

            video = Video(
              id = str(record['ID']),
              pinterest_link = record['Pinterest Link'],
              download_status = record['Dowload Status'],
              drobox_uploaded = record['Drobox Uploaded'],
              remark = record['Remark'],
            )

            videos.append(video)

        return videos
              
