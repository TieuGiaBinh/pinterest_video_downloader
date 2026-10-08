import os
from pathlib import Path
from src.sevices.googlesheets_client import GoogleSheetsClient
from src.sevices.googlesheets_info import GoogleSheetsInfo
from src.sevices.pinterest_download import PinterestDownload
from src.sevices.dropbox_upload import DropboxUpload


def main():
  
    print('Github action start running')
  
    google_client = GoogleSheetsClient(service_account_json = os.environ['GOOGLE_SERVICE_ACCOUNT'], spreadsheet_id = os.environ['GOOGLE_SPREADSHEET_ID'])
    work_sheet = google_client.get_worksheet('pinterest')

    google_sheet = GoogleSheetsInfo(work_sheet)
    pinterest_videos = google_sheet.get_pending_videos()

    for video in pinterest_videos:
      #pinterest_dl = PinterestDownload(video)
      #video_path = pinterest_dl.download_with_yt_dlp()

      #dropbox_path = f'/Debug/Pinterest/{video_path.name}'
      #dropbox_ul = DropboxUpload(os.environ['DROPBOX_REFRESH_TOKEN'], os.environ['DROPBOX_APP_KEY'], os.environ['DROPBOX_APP_SECRET'], video_path, dropbox_path)
      #dropbox_ul.upload_file()

      video.download_status = 'success'
      video.dropbox_uploaded = 'uploaded'
      google_sheet.update_googlesheets(video)
      
      print(f'video path: {video_path}')
      print(f'ID: {video.id}')
      print(f'Pinterest url: {video.pinterest_link}')
      print(f'video name: {video_path.name}')


if __name__ == '__main__':
    main()
