# DAG description
## ELT

DAG used to extract tweets using **tweepy** from Twitter API and load them into BigQuery. Consists of 3 tasks:
-  Task1: Install tweepy
-  Task2: Extract JetBlue tweets to BQ
-  Task3: Extract SouthwestAir tweets to BQ

BigQuery:
- [JetBlue tweets](https://console.cloud.google.com/bigquery?hl=es&project=refactored-waddle&d=tweets&p=refactored-waddle&t=JetBlue&page=table&ws=!1m5!1m4!4m3!1srefactored-waddle!2stweets!3sJetBlue)
-  [SouthwestAir tweets](https://console.cloud.google.com/bigquery?hl=es&project=refactored-waddle&d=tweets&p=refactored-waddle&t=SouthwestAir&page=table&ws=!1m10!1m4!4m3!1srefactored-waddle!2stweets!3sJetBlue!1m4!4m3!1srefactored-waddle!2stweets!3sSouthwestAir)
