# :airplane: :seat: The Models 

# Description of models

## 1. Data

We extract 1,000 tweets mentioning @JetBlue and 1,000 mentioning @SouthwestAir from the [Twitter API](https://developer.twitter.com/en) for a day on march 2022.  We filter out retweets during this part of the process.
During extraction we define the following variables: 

* **user** : Twitter user account originating the tweet
* **text** :  Full text content in each tweet
* **followers** :  Number of user accounts that follow the given user
* **location** :  Geographic location from the given user
* **verified** :  Indicator equal 1 if the account has this condition

Then, each team member manually tagged 500 tweets into three categories

* **1** Positive perception towards the airline
* **-1** Negative perception towards the airline
* **0** Neutral perception towards the airline


We also verify for [Twitterbots](https://es.wikipedia.org/wiki/Twitterbot) by XXXX

## 2. Feature engineering

We clean the tweets by:

- [x] Convert text to lowercase
- [x] Remove all URLs
- [x] Remove Twitter accounts (@)
- [x] Remove specific names
- [x] Trim blank spaces
- [x] Remove punctuations, symbols and numbers
- [x] Remove non-English tweets
- [x] Remove stop words
- [x] Remove hastags (#)

## 3. Algorithm

We consider the following methods


## Naive Bayes Algorithm



## Logistic Regression


## References

- [Sentiment Analysis: An Introduction to Naive Bayes Algorithm](https://towardsdatascience.com/sentiment-analysis-introduction-to-naive-bayes-algorithm-96831d77ac91)
- [Introduction to Logistic Regression](https://towardsdatascience.com/introduction-to-logistic-regression-66248243c148)
- [Sentiment Analysis of Twitter Data Using Machine Learning Approaches and Semantic Analysis](file:///C:/Users/valsc/Downloads/16_Sentimentanalysisoftwitterdatausingmachinelearningapproachesandsemanticanalysis.pdf)
- [Twitter Sentiment Analysis Using Supervised Machine Learning](file:///C:/Users/valsc/Downloads/Twitter_Sentiment_Ana_e.Proofing_Springer_NikhilYadav%20(1).pdf)
- [Sentiment Analysis of Twitter Data: A Survey of Techniques](https://arxiv.org/ftp/arxiv/papers/1601/1601.06971.pdf)
- [A Comparative Analysis of Machine Learning Classifiers for Twitter Sentiment Analysis](https://rcs.cic.ipn.mx/2016_110/A%20Comparative%20Analysis%20of%20Machine%20Learning%20Classifiers%20for%20Twitter%20Sentiment%20Analysis.pdf)
