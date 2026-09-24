from src.sevices.googlesheets_client import GoogleSheetsClient
from src.sevices.googlesheets_info import GoogleSheetsInfo
import os


def main():
  
    print('Github action start running')
  
    google_client = GoogleSheetsClient(service_account_json = os.environ['GOOGLE_SERVICE_ACCOUNT'], spreadsheet_id = os.environ['GOOGLE_SPREADSHEET_ID'])
    work_sheet = google_client.get_worksheet('pinterest')

    google_sheet = GoogleSheetsInfo(work_sheet)
    pinterest_videos = google_sheet.get_videos()

    print(f'ID: {pinterest_videos[0].id}')
    print(f'Pinterest link: {pinterest_videos[0].pinterest_link}')


if __name__ == '__main__':
    main()
