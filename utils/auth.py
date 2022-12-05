# Check if the RFID is in the Authorised Users Sheet

class Auth:
    def check_auth(rfid, authdf):
        return rfid in authdf.loc[:,'RFID'].tolist()