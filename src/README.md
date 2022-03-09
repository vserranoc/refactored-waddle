# Kind of process and technologies

The process made it is an ELT.

## Technologies:
- Bigquery

# Summary
This ELT make call to twitter API for each topic, then each payload is unpackage into row for two tables, tweets and users. 
Finally, both tables are loaded into bigquery.