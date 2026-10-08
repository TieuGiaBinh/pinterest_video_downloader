from src.models.video import Video
from src.interfaces.googlesheets_interfaces import GoogleSheetsInterfaces


class GoogleSheetsInfo (GoogleSheetsInterfaces):
  
    def __init__(self, worksheet):
      
        self.worksheet = worksheet


    def get_pending_videos(self) -> list[Video]:
      
        records = self.worksheet.get_all_records()
      
        videos = []
      
        for record in records:
          
            if record['Download Status'].lower() != 'pending':
                continue

            video = Video(
              id = str(record['ID']),
              pinterest_link = record['Pinterest Link'],
              download_status = record['Download Status'],
              dropbox_uploaded = record['Dropbox Uploaded'],
              remark = record['Remark'],
            )

            videos.append(video)

        return videos


    def update_googlesheets(self, video: Video):
        records = self.worksheet.get_all_records()

        for row_number, row in enumerate(records, start = 2):
            if str(row['ID']) == video.id:
                self.worksheet.update(f'C{row_number}:D{row_number}',[[video.download_status, video.dropbox_uploaded]])
                print('googlesheets was updated')
                break
              
