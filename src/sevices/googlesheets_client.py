import gspread
from google.oauth2.service_account import Credentials
import json


class GoogleSheetsClient:
  
    SCOPES = ['https://www.googleapis.com/auth/spreadsheet']

  
    def __init__(self, service_account_json: str, spreadsheet_id: str):
      
        self.service_account_json = service_account_json
        self.spreadsheet_id = spreadsheet_id
      

    def get_worksheet(self, worksheet_name: str):
      
        service_account_info = json.load(self.service_account_json)
        credentials = Credentials.from_service_account_info(service_account_info, scopes = self.SCOPES)
        client = gspread.authorize(credentials)
        spreadsheet = client.open_by_key(self.spreadsheet_id)

        return spreadsheet.worksheet(worksheet_name)
