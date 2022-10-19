# Code for the authentication of the RFID UID

class Auth:
    def check_auth(uid, log):
        #uid will be the id that is scanned, log is the data which contains all the RFID ids that are tracked in the excel
        return None # Return true if the uid is present in the excel data, else return false