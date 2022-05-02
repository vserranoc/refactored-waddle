from google.oauth2 import service_account

import pandas_gbq
import pandas as pd
import joblib
from src.scoring_pipeline import predict_sentiment   

# Load artifacts
final_model = joblib.load('./artifacts/final_model.joblib')
best_preprocessing = joblib.load('./artifacts/feature_extractor.joblib')

# Credentials
credentials = service_account.Credentials.from_service_account_info({},)

# define the scope
scopes = ['https://www.googleapis.com/auth/bigquery']
scoped_credentials = credentials.with_scopes(scopes)

query = """
SELECT * FROM train.train_set_predictions
"""
df = pd.read_gbq(query,credentials=credentials).sort_values('id')

# Scoring
df['sentiment'] = df.text.apply(lambda x: predict_sentiment(x))

# Database persistance in bq¡
destination = 'scoring.scoring_v1'
pandas_gbq.to_gbq(df,destination_table = destination,credentials=scoped_credentials,if_exists='replace')