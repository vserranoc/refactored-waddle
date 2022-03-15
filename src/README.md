# Kind of process and technologies
The process is an ETL.

## Technologies:
- Bigquery

# Summary
This ETL make calls to twitter API for each topic, then each payload is unpacked into a row for a table.
Before loading data into bigquery a new columns is created as "clean_tweet", this columns contains the clean tweet.
After getting all the data, the columns are separeted into two tables, tweets and users.
Finally, both tables are loaded into bigquery.