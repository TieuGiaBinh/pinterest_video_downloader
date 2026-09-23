from src.sevices.googlesheets_client import GoogleSheetsClient
from src.sevices.googlesheets_videos import GooglesheetsVideos


def main():
  
    print('Github action start running')
  
    google_client = GooglesheetsClient(service_account_json = os.environ['GOOGLE_SERVICE_ACCOUNT_JSON'], spreadsheet_id = os.enviro['GOOGLE_SPREADSHEET_ID'])
    pinterest_sheet = google_client.get_worksheet('pinterest')

    google_sheet = GoogleSheetsVideo(pinterest_sheet)
    pinterest_videos = google_sheet.get_videos()

    print(f'ID: {pinterest_videos[0].id}')
    print(f'Pinterest link: {pinterest_videos[0].pinterest_link}')


if __name__ == '__main__':
    main()
