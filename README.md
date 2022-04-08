# Arquitectura de Producto de Datos
## Team name: Serverless

### Team members:
|**Name**|**User**|
| ------------------ | ------------ |
|Luis Alberto Valdez Ibarra |@LuisValdez07|
|Paulina Hernández Trejo|@pautrejo|
|Jesús Enrique Miranda Blanco |@jesusmb230795|
|Valeria Serrano Cote |@vserranoc|

### **About team**
We think that we are an awesome team because we have mutual respect, common and aligned goals, open communication, patience, tolerance, everyone contributes, support each other, we complement each other, has fun, and overall, appreciates and encourages diverse thinking, learning, and adaptation.


# Which american Low Cost Carriers is better for you: Jet Blue or SouthwestAir
## Sentiment Analysis in Twitter about american airlines

 We offer a product that helps helps you decide between two low-cost airlines with similar prices and routes. Users' perception of airline service is a relevant  variable that would help compare the service provided by airlines and facilitate users' decisions. 
Our application allows knowing the feeling of users regarding the service of these airlines, which allows them to make an informed decision. Beyond the features listed below, which we assume are known to users.

| Feature | Southewst Airlines | JetBlue |
| --------------------------------------------- | --------------------------------------------------------- | ----------------------------------------------------- |
| Aircraft |738 aircraft | 265  | 
| Type aircraft | Boeing 737 | A320, A321 and Embraer ERJ-190 |
|Average cost|$153|$180|
|Strategy|Cost-efficiency and customer satisfaction from efficient operations|Charging higher prices for a packaged service|
|Seat pitch|32 to 33 inches|	32 to 35 inches|
|Seat width|17.8 at most, the average is as low as 17 inches|17.8 to 18.5 inches|
|Model| the point-to-point model, flying nonstop |the hub-and-spoke set-up, or  focus cities, mixing in point-to-point |
|Hawaii|It flies to Hawaii|It does have a codeshare with Hawaiian Airlines from Boston|
|International coverage|Southwest's network does not stretch further than Central America|JetBlue has services to several cities in south America and Caribbean. JetBlue flies transatlantic to London|
|National coverage|It has a vast flight network covering a majority of the United States|It is focused primarily on the eastern half – although they do fly from coast to coast |
|Frequent flyer program|Rapid Rewards| TrueBlue |
|Seat reservation|No|Open seating policy (meaning that there are no seat reservations)|You can pay more for a better seat|
|Seating amenities|No|Their seats are simple	Video screens and Power ports|
|Food|Complementary drink and a bag of snack mix|Complementary drink and a bag of sack mix.  Also, there’s a food for purchase menu| 

Source: Own elaboration based on  [Southwest Vs. JetBlue - Which American LCC is Better For You?](https://simpleflying.com/southwest-vs-jet-blue/) and  [Southwest vs JetBlue: which airline is likely to give you less heartburn?](https://www.sanspotter.com/southwest-vs-jetblue/)

We want to provide users with additional information to that presented in the table, what our sentiment analysis will yield is a subjetive variable of the feling of  users about service, that would help the undecided to lean towards one of the two airlines.
We want to toast travel agencies with useful tools to make recommendations to their clients, since the characteristics of the flights offered by airlines could be insufficient, considering the feelings of users to make their recommendations could help them make their advice objective

### **Sentiment Analisys**
Sentiment analysis is the extraction and processing of the subjective content of texts, which are usually classified into positive, negative and neutral content. This technique is part of Natural Language Processing or NLP [Natural Language Processing](https://www.sas.com/es_ar/insights/analytics/what-is-natural-language-processing-nlp.html).
There are two popular methods for analyzing the text of tweets. The first one uses the [machine-learning approach](https://en.wikipedia.org/wiki/Machine_learning) and the second one uses [lexical dictionaries](https://en.wikipedia.org/wiki/Lexical_analysis).

### **Data**
We analyze the sentiments obtained from the conversations that occur in Twitter, the social networks that is the most popular in the world. [Twitter](https://es.wikipedia.org/wiki/Twitter) had more than 330 million monthly active users, at the beginning of 2019. 
With Twitter, people can send and spread messages of up to 140 characters, known as tweets. Through this subjective information of various aspects of daily life is generated. Twitter is used by various purposes: politics, journalism, science, entertainment, popular culture, business, etc.
For this reason, several industries extract the opinions of this social network to know the pulse of products or services.

On Twitter, it is possible to identify topics with the use of hashtags or tags, which begin with the # character and a string of characters that follows, made up of one or more words together. These labels are used to group tweets tagged in the same way, which allows users to quickly obtain results on the same topic.

The social network allows us to extract the tweets of users, which we use as an object of study. Specifically we do the following:

1. We extract the tweets that users leave towards airlines. As users of the social network, we request the developer account in the link: https://developer.twitter.com/en/apps.
2. Once the account is approved, an app is created, only the data is filled in and the created app is registered.
3. We access the “keys and Access Tokens” tab and click on the “Generate My Access Token and Token Secret” button, these are credentials to be able to access the Twitter API and extract the tweets that are needed.
4. The extraction of tweets is done with Python's Jupyter Notebook. The libraries we use to access the Twitter API are:
The following diagram illustrates the points indicated...


### **Model**
We use traditional models, some of these algorithms were selected because of their scalability. 
This alternative consists of taking a text sample, processing the piece of information until the model can predict with accuracy the sentiments of the tweet, then the text is the input for the classifier, and it will predict the sentiment as negative, neutral, or positive.

- Naive Bayes

  This probabilistic classifier will help us to learn about the pattern of an examined set of data previously categorized.
  
-Logistic regression

  It is a type of regression analysis, which is used to predict the outcome of a categorical variable, in our case sentiment (positive, negative or neutral), based on   the independent or predictor variables, for us this are the words that we obtein from twitter. 


### **Evaluation**
We evaluate model performance throught:

•	We would review the performance of the model based on different error measures MSE, MAE

•	During training we would take care of filtering validation data in the training set

•	We would try to use samples as similar as possible to the population we are trying to forecast

•	We would carefully analyze that the data used is not censored

•	We would use a validation sample large enough to be able to discriminate between what performs well or poorly

•	We will make cuts of different training/validation sizes and see what performance results from choosing a final model in a validation sample.

If application satisfies objectives: we would identify if the application solves the problem for which it was created, we would observe that its use implies low costs for users, it is quick and easy to consult. Also, we would analyze if the application provides added value and we would identify its benefits compared to other similar applications

### **Inference**

•	We use batch predictions because they increase the speed of the calculation as they are performed on blocks of data and not on each unit, for which we use CPU. 

•	We will need one or two CPU with the capacity to process 2000 tweets, obtained through the words: @JetBlue and @SouthwestAir

### **MVP (minimum viable product )**

We will extract tweets, calculate sentiment with the tools provided by Google and perform visualizations. 

How difficult is it to get there? :

• It could be a challenge to reach the MVP because we have few days from the ETL to select a model that allows us to maximize the advantages of the data and minimize the risks of a computationally expensive model. Furthermore, in this period resilience is required in order not to abandon the model easily after having failed attempts. Therefore, using the simplest and at the same time adequate model could help us a lot.

**Pre-Mortems**

Reasons for the project to fail:

• Lack of time to choose the best model

• Knowing how to implement an interface

• Knowledge of configuring an orchestrator

• The potential biases in our selection of words

• Lack of data cleanliness

• There is information about the business that we are not considering





### References

*  [How to successfully invest in machine learning in an MVP](https://sennalabs.com/th/blogs/how-to-successfully-invest-in-machine-learning-in-an-mvp)
*  [Las GPU como pasado, presente y futuro de la computación](https://www.xataka.com/componentes/las-gpu-como-pasado-presente-y-futuro-de-la-computacion)
*  [Notas aprendizaje de máquina, 2021](https://github.com/felipegonzalez/aprendizaje-maquina-mcd-2021)
*  [Machine learning on mobile: on the device or in the cloud?](https://machinethink.net/blog/machine-learning-device-or-cloud/)
*  [Análisis de sentimiento en Twitter. Reputación de las principales aerolíneas europeas tras la crisis sanitaria del COVID-19](https://dspace.unia.es/handle/10334/5915)
*  [Sentiment Analysis in Social Networks through Topic Modeling](http://www.lrec-conf.org/proceedings/lrec2016/pdf/682_Paper.pdf)
*  [Análisis de Sentimientos en Twitter: Una Implementación sobre Cloudera](https://ria.utn.edu.ar/bitstream/handle/20.500.12272/4704/An%C3%A1lisis_de_Sentimientos_en_Twitter_%28167%29.pdf?sequence=1)





