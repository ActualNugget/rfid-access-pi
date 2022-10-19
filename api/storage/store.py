import pandas as pd
import os

# Class to manage all the functions of storage (Create, Read, Update, Delete)
class Store:
    # Executes a pandas.read_excel, returns a pandas Dataframe
    def read(extension_path='/assets/rfid-access-list.xlsx'):
        absolute_path = os.path.abspath(os.path.dirname('Text.xlsx'))
        return pd.read_excel(absolute_path + extension_path, engine="openpyxl")