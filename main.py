# from api.local.store import Store
from api.google_sheet.google_sheet import authSheet, logSheet
from gspread_dataframe import set_with_dataframe
import pandas as pd
from utils.auth import Auth
from utils.log import Log
from pi.scan import scan
from pi.lock import open
import time

authdf = pd.DataFrame(authSheet.get_all_records())
logdf = pd.DataFrame(logSheet.get_all_records())

def access(rfid):
    if Auth.check_auth(rfid, authdf):
        open(40)
    newLogdf = Log.create(rfid, authdf, logdf)
    set_with_dataframe(logSheet, newLogdf)

def updateAuthSheet(rfid):
    userName = input('Enter name: ')
    userList = authSheet.findall(userName)
    if len(userList) == 0:
        print ('User <{0}> not found'.format(userName))
    elif len(userList) > 1:
        print(userList)
        print('Resolve repeated names in the Google Sheet')
    else:
        Auth.create(rfid, userName, authSheet)

while True:
    rfid = scan()
    access(rfid)
    time.sleep(5)