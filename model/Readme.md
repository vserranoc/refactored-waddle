# :airplane: :seat: The Models 

# Which airline is better for users or which airline is worse?
# Description of models

## 1. Data

We extract 6404 tweets mentioning @JetBlue and  @SouthwestAir from the [Twitter API](https://developer.twitter.com/en) for a day on march 2022.  We filter out retweets during this part of the process. After removing duplicates and cleaning the database we create a dataset with 2712 tweets, of which 2009 are negative and 703 are positive. 

During extraction we define the following variables: 

* **user** : Twitter user account originating the tweet
* **text** :  Full text content in each tweet
* **followers** :  Number of user accounts that follow the given user
* **location** :  Geographic location from the given user
* **verified** :  Indicator equal 1 if the account has this condition

Then,  team member manually tagged tweets into two categories:

* **1** Positive perception towards the airline
* **0** Negative perception towards the airline

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


## 2. Feature engineering

  Word count

We found that tweets with an extension of less than 40 words predominate. Those who manifest in a negative way commonly use more words than positive manifestations. We look at two sets of tweets, those with a median of 20 words and a maximum of 40 words, and those with a median of 50 words and a maximum of 60. The first set is larger in magnitude than the second.

  Word density

When measuring the density of tweets, that is, the number of words per total number of characters, we find that the words written in the tweets are usually short, even the words used in the positive tweets are shorter than those used in the tweets. negatives. The length of the words used in the tweets may be associated with the abbreviations that are commonly used in the tweets and with the time spent writing tweets.

  Score count

The analyzed tweets use few punctuation marks. The highest frequency of these signs goes from 1 to 5, while with less frequency we have tweets with more than 20 punctuation marks.
The use of punctuation marks is scarce, probably because they are written in English, a language where accents, for example, are not used.

Detailed description at **[EDA](https://github.com/vserranoc/refactored-waddle/blob/main/model/EDA.ipynb)


## 3. Preprocessing

Prior to modeling, we generate a Sparse Matrix, which is built from vectorizing the frequency of the unique words that we have in the entire core. In other words, a dictionary of unique words is generated, from which a matrix is built that only contains numbers, which in turn correspond to the frequency of each word in each of the tweets. To build this matrix automatically, we use CountVectorizer, which is a tool provided by the scikit-learn library in Python. More about it [here](https://www.geeksforgeeks.org/using-countvectorizer-to-extracting-features-from-text/#:~:text=CountVectorizer%20is%20a%20great%20tool,occurs%20in%20the%20entire%20text).

As part of the preprocessing, we generate a word weight that gives stopwords such as the, you, of, will, etc. a lower weight. For this we use a tf-idf, which allows us to calculate the weight of the words according to their frequency and apply the inverse of this. Thus, the rarest words will receive the highest weight. The Python tool used to do this is [tfidf](https://www.freecodecamp.org/news/how-to-process-textual-data-using-tf-idf-in-python-cd2bbc0a94a3/).


We consider the following methods:

## 4. Algorithm

### Logistic Regression

Logistic regression is a classification algorithm used to assign observations to a discrete set of classes.

* Logistic Regression is a Machine Learning algorithm which is used for the classification problems, it is a predictive analysis algorithm and based on the concept of probability. 

* The Logistic Regression uses a more complex cost function than the Linear Regression model, this cost function can be defined as the ‘Sigmoid function’ or also known as the ‘logistic function’.

* One of the main characteristics of logistic regression is that it bound the cost function to be between 0 and 1, which fails to hold under linear functions. 

* To guarantee the cost function to be optimized (global minima), it is defined as a convex combination of the cost function when y = 1 and y = 0. 

This intuition can be easiliy extended for more than two categories, by using the multinomial logistic regression. 

<img src="/model/image/ZOnIK.png">

### Naive Bayes Algorithm

This model applies Bayes theorem with a Naive assumption of no relationship between different features. According to Bayes theorem:
Posterior = likelihood * proposition/evidence 

or 

P(A|B) = P(B|A) * P(A)/P(B)

Naive Bayes Model works particularly well with text classification and spam filtering. Advantages of working with NB algorithm are:

* Requires a small amount of training data to learn the parameters
* Can be trained relatively fast compared to sophisticated models

The main disadvantage of NB Algorithm is:

* It’s a decent classifier but a bad estimator
* It works well with discrete values but won’t work with continuous values (can’t be used in a regression)

See more at [Sentiment Analysis: An Introduction to Naive Bayes Algorithm](https://towardsdatascience.com/sentiment-analysis-introduction-to-naive-bayes-algorithm-96831d77ac91)



## 5. ML metrics

In order to evaluate the performance of each of the models, we used the metrics: recall, accuracy, F1_ score, and AUC.

Recall. This metric allows us to observe the number of positives correctly identified by the model. In the confusion matrix, the recall is the ratio of true positives vs. the sum of true positives and false negatives.

Accuracy. Accuracy is one metric for evaluating classification models. It gives us the proportion of predictions our model got right. In other words, accuracy is the ratio: number of correct predictions/total number of predictions. Or, (True Positives + True Negatives)/ (True Positives + True Negatives + False Positives + False Negatives).

The F1 score. It is the combination of Precision and Recall, its goal is “combine the precision and recall metrics into a single metric. At the same time, the F1 score has been designed to work well on imbalanced data”. When F! is high, both Precision and Recall are high. For its part, what a low indicates is that both Precision and Recall are low. Finally, if a model has a medium F1 score, it implies that Precision or Recall is low and the other is high. More about [here](https://towardsdatascience.com/the-f1-score-bec2bbc38aa6).

AUC. This metric measures the area under the ROC curve.
The curve ROC is the graph resulting from representing, for each threshold value, the sensitivity and specificity measurements of the diagnostic test. Sensitivity is the proportion of individuals who present the event of interest and who are classified by the test as carriers of said event. While, the specificity quantifies the proportion of individuals that do not present it and are classified by the test as such. 

We consider the [ROC](https://es.wikipedia.org/wiki/Curva_ROC) curve in each model in order to observe the graph of the ratio or proportion of true positives (VPR = Ratio of True Positives) against the ratio or proportion of false positives (FPR = Ratio of False Positives) also according to the discrimination threshold varies (value from which we decide that a case is positive). In addition, the ROC curve allows us to observe the sensitivity of VPR and FPR when modifying the decision threshold.
More about this metric here: https://arize.com/blog/what-is-auc/


## 6. Results 


Detailed description at [Model](https://github.com/vserranoc/refactored-waddle/blob/main/model/modelling.ipynb)


## 7. Conclusion 
There is a large number of negative words associated with airline services, in general users are dissatisfied with these LCC, however, the opinion of JetBlue users is worse than that of SouthwestAir.
The model used with the Naive Bayes method seems to be better for this exercise.


## References

- [Sentiment Analysis: An Introduction to Naive Bayes Algorithm](https://towardsdatascience.com/sentiment-analysis-introduction-to-naive-bayes-algorithm-96831d77ac91)
- [Introduction to Logistic Regression](https://towardsdatascience.com/introduction-to-logistic-regression-66248243c148)
- [Sentiment Analysis of Twitter Data Using Machine Learning Approaches and Semantic Analysis](file:///C:/Users/valsc/Downloads/16_Sentimentanalysisoftwitterdatausingmachinelearningapproachesandsemanticanalysis.pdf)
- [Twitter Sentiment Analysis Using Supervised Machine Learning](file:///C:/Users/valsc/Downloads/Twitter_Sentiment_Ana_e.Proofing_Springer_NikhilYadav%20(1).pdf)
- [Sentiment Analysis of Twitter Data: A Survey of Techniques](https://arxiv.org/ftp/arxiv/papers/1601/1601.06971.pdf)
- [A Comparative Analysis of Machine Learning Classifiers for Twitter Sentiment Analysis](https://rcs.cic.ipn.mx/2016_110/A%20Comparative%20Analysis%20of%20Machine%20Learning%20Classifiers%20for%20Twitter%20Sentiment%20Analysis.pdf)
- [Curvas ROC (Receiver-Operating-Characteristic)y sus aplicaciones](https://idus.us.es/bitstream/handle/11441/63201/Valle%20Benavides%20Ana%20Roc%C3%ADo%20del%20TFG.pdf?sequence=1&isAllowed=y)
