import os
from src.sevices.googlesheets_client import GoogleSheetsClient
from src.sevices.googlesheets_info import GoogleSheetsInfo
from src.sevices.pinterest_download import PinterestDownload


def main():
  
    print('Github action start running')
  
    google_client = GoogleSheetsClient(service_account_json = os.environ['GOOGLE_SERVICE_ACCOUNT'], spreadsheet_id = os.environ['GOOGLE_SPREADSHEET_ID'])
    work_sheet = google_client.get_worksheet('pinterest')

    google_sheet = GoogleSheetsInfo(work_sheet)
    pinterest_videos = google_sheet.get_pending_videos()

    for video in pinterest_videos:
      pinterest_dl = PinterestDownload(video)
      video_path = pinterest_dl.download_with_yt_dlp()

      print(f'video path: {video_path}')
      print(f'ID: {video.id}')
      print(f'Pinterest url: {video.pinterest_link}')


if __name__ == '__main__':
    main()
