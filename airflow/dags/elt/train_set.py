import gspread
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
import pandas_gbq




credentials = service_account.Credentials.from_service_account_info({},)

# define the scope
scopes = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/bigquery']
scoped_credentials = credentials.with_scopes(scopes)

gc = gspread.authorize(scoped_credentials)


worksheet = gc.open('tweets_train_label').sheet1
rows = worksheet.get_all_values()
df = pd.DataFrame(rows)
df.columns = df.iloc[0]
df = df[1:]
df.dropna(inplace=True)

#save
#write to bq
destination = 'train.train_set'
pandas_gbq.to_gbq(df,destination_table = destination,credentials=scoped_credentials,if_exists='replace')