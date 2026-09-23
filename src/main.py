from src.sevices.googlesheets_client import GoogleSheetsClient
from src.sevices.pinterest_info import PinterestInfo
import os


def main():
  
    print('Github action start running')
  
    google_client = GoogleSheetsClient(service_account_json = os.environ['GOOGLE_SERVICE_ACCOUNT_JSON'], spreadsheet_id = os.environ['GOOGLE_SPREADSHEET_ID'])
    pinterest_sheet = google_client.get_worksheet('pinterest')

    pinterest_info = PinterestInfo(pinterest_sheet)
    pinterest_videos = pinterest_info.get_videos()

    print(f'ID: {pinterest_videos[0].id}')
    print(f'Pinterest link: {pinterest_videos[0].pinterest_link}')


if __name__ == '__main__':
    main()
