# DAGs description

In this section we describe the process to execute the DAGs (Directed Acyclic Graph), which are the core concept of Airflow. This collecting tasks together, organized with dependencies and relationships to say how they should run.


![image](https://user-images.githubusercontent.com/66652832/166189712-b0000add-c5d0-4c45-aa69-cc9ba3912b0b.png)


## DAG ELT

DAG used to combine manual labeling in Google Sheets with tweets extraction using **tweepy** from Twitter API to finally upload the result into BigQuery and back to Google Sheets. Consists of 5 tasks:
- Task1: Connect to label information in Google Sheets and upload it to BQ.
[train set](https://console.cloud.google.com/bigquery?hl=es&project=refactored-waddle&ws=!1m25!1m4!1m3!1srefactored-waddle!2sbquxjob_22d9a46_1806bae9885!3sUS!1m4!1m3!1srefactored-waddle!2sbquxjob_5f22cbb3_1807602833e!3sUS!1m4!1m3!1srefactored-waddle!2sbquxjob_3d952062_18076003e3c!3sUS!1m4!1m3!1srefactored-waddle!2sbquxjob_25f571a3_18075ff846c!3sUS!1m4!4m3!1srefactored-waddle!2strain!3strain_set)
-  Task2: Extract JetBlue tweets to BQ
[JetBlue tweets](https://console.cloud.google.com/bigquery?hl=es&project=refactored-waddle&ws=!1m30!1m4!1m3!1srefactored-waddle!2sbquxjob_22d9a46_1806bae9885!3sUS!1m4!1m3!1srefactored-waddle!2sbquxjob_5f22cbb3_1807602833e!3sUS!1m4!1m3!1srefactored-waddle!2sbquxjob_3d952062_18076003e3c!3sUS!1m4!1m3!1srefactored-waddle!2sbquxjob_25f571a3_18075ff846c!3sUS!1m4!4m3!1srefactored-waddle!2strain!3strain_set!1m4!4m3!1srefactored-waddle!2stweets_extraction!3sJetBlue)
-  Task3: Extract SouthwestAir tweets to BQ
[Southwest Air tweets](https://console.cloud.google.com/bigquery?hl=es&project=refactored-waddle&ws=!1m35!1m4!1m3!1srefactored-waddle!2sbquxjob_22d9a46_1806bae9885!3sUS!1m4!1m3!1srefactored-waddle!2sbquxjob_5f22cbb3_1807602833e!3sUS!1m4!1m3!1srefactored-waddle!2sbquxjob_3d952062_18076003e3c!3sUS!1m4!1m3!1srefactored-waddle!2sbquxjob_25f571a3_18075ff846c!3sUS!1m4!4m3!1srefactored-waddle!2strain!3strain_set!1m4!4m3!1srefactored-waddle!2stweets_extraction!3sJetBlue!1m4!4m3!1srefactored-waddle!2stweets_extraction!3sSouthwestAir)
-  Task4: Sample 50 tweets for every airline (unlabeled) and join them with existing label data in BQ for model training and predictions.
[train set predictions](https://console.cloud.google.com/bigquery?hl=es&project=refactored-waddle&ws=!1m40!1m4!1m3!1srefactored-waddle!2sbquxjob_22d9a46_1806bae9885!3sUS!1m4!1m3!1srefactored-waddle!2sbquxjob_5f22cbb3_1807602833e!3sUS!1m4!1m3!1srefactored-waddle!2sbquxjob_3d952062_18076003e3c!3sUS!1m4!1m3!1srefactored-waddle!2sbquxjob_25f571a3_18075ff846c!3sUS!1m4!4m3!1srefactored-waddle!2strain!3strain_set!1m4!4m3!1srefactored-waddle!2stweets_extraction!3sJetBlue!1m4!4m3!1srefactored-waddle!2stweets_extraction!3sSouthwestAir!1m4!4m3!1srefactored-waddle!2strain!3strain_set_predictions)

-  Task5: Upload train set back to Google Sheets for labeling.
[train set in Google Sheets](https://docs.google.com/spreadsheets/d/1x7g65pMlxbpwqACzdsbXW4_PiCbHJVCZ0C_1ln4i-Z8/edit#gid=0)

![image](https://user-images.githubusercontent.com/66652832/166336146-7f48ca55-7f54-49ba-b701-a6ce20ffb1d5.png)

## DAG MLOPs

This DAG loads the previous task, cleans the data, vectorizes the core, runs the model and finally obtains the scoring. The tasks are distributed in 3 tasks:

- Task 1. Generates alert when the DAG ELT has been completed

- Task 2. Scoring:
  - Load data
  - Load artifacts
  - Clean data
  - Transform the data (generate sparse matrix)
  - Scoring sentiment
  - Save scoring in big query

![image](https://user-images.githubusercontent.com/66652832/166336074-5483e09a-8e0d-4d68-b4b8-2034cb1fb156.png)



