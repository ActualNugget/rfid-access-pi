# Logging all user access
import pandas as pd
import time

class Log:
    def create(rfid, authdf, logdf):
        currentTime = time.asctime()
        if rfid in authdf.loc[:,'Decimal'].tolist():
            authorised = True
            entry = authdf.loc[authdf['Decimal'] == rfid]
            user = entry.loc[:,'Name'].tolist()[0]
        else:
            authorised = False
            user = ''
        df = pd.DataFrame([[currentTime, rfid, authorised, user]], columns=['Time', 'RFID', 'Authorised', 'User'])
        logdf = pd.concat([logdf, df], ignore_index=True)
        return logdf
