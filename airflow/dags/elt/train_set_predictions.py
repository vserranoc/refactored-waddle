import pandas as pd
import gspread
import pandas_gbq
from google.oauth2 import service_account
import gspread_dataframe as gd



credentials = service_account.Credentials.from_service_account_info({},)

# define the scope
scopes = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/bigquery']
scoped_credentials = credentials.with_scopes(scopes)

query = """
SELECT * FROM train.train_set_predictions
"""
df = pd.read_gbq(query,credentials=credentials).sort_values('id')

gc = gspread.authorize(scoped_credentials)
ws = gc.open("tweets_train_label").sheet1
ws.clear()
gd.set_with_dataframe(ws, df)


