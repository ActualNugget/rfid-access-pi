# Check if the RFID is in the Authorised Users Sheet

class Auth:
    def check_auth(rfid, authdf):
        return rfid in authdf.loc[:,'Decimal'].tolist()

    def create(rfid, userName, authSheet):
        row = authSheet.find(userName).row
        authSheet.update('B{0}'.format(row), rfid)
