from api.storage.store import Store
from utils.auth import Auth

rfid_access_log = Store.read()
print(rfid_access_log)

# rfid_access_log is a variable that gives you a pandas dataframe, figure out what the data is and how to manipulate the data
# Under utils --> auth.py --> there is a class called Auth with a method known as check_auth()
# You can access the method via the below statement
# Auth.check_auth()
# Edit the method in the auth.py file to access the data in rfid_access_log and check if the ID passed in the method is in the UID data field in rfid_access_log