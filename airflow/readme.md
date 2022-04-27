# DAG description
## ELT

DAG used to extract tweets using **tweepy** from Twitter API and load them into BigQuery. Consists of 2 tasks (so far):
-  Task1: Extract JetBlue tweets to BQ
-  Task2: Extract SouthwestAir tweets to BQ

BigQuery:
- [JetBlue tweets](https://console.cloud.google.com/bigquery?hl=es&project=refactored-waddle&ws=!1m5!1m4!4m3!1srefactored-waddle!2stweets_extraction!3sJetBlue)
-  [SouthwestAir tweets](https://console.cloud.google.com/bigquery?hl=es&project=refactored-waddle&ws=!1m10!1m4!4m3!1srefactored-waddle!2stweets_extraction!3sJetBlue!1m4!4m3!1srefactored-waddle!2stweets_extraction!3sSouthwestAir)
