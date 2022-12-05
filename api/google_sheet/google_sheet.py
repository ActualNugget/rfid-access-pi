import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('./assets/credentials.json', SCOPES)
client = gspread.authorize(credentials)

# To create a sheet (<name=string>)
# sheet = client.create('')

# Share sheet created (<name=string>, perm_type=<string>, role=<string>)
# sheet.share('', perm_type='', role='')

sheet = client.open('Makers 3d Printer')
authSheet = sheet.get_worksheet(0)
logSheet = sheet.get_worksheet(1)

