# Arquitectura de Producto de Datos
## Team name: Serverless

## Team members:

|**Name**|**User**|
| ------------------ | ------------ |
|Luis Alberto Valdez Ibarra |@LuisValdez07|
|Paulina Hernández Trejo|@pautrejo|
|Jesús Enrique Miranda Blanco |@jesusmb230795|
|Valeria Serrano Cote |@vserranoc|

## About team
We think that we are an awesome team because we have mutual respect, common and aligned goals, open communication, patience, tolerance, everyone contributes, support each other, we complement each other, has fun, and overall, appreciates and encourages diverse thinking, learning, and adaptation.

**##ABOUT THE PROJECT**

One of the most relevant topics our days is sentiment analysis, with this tool we analyzed the sentiments derived from the conversations that occur on Twitter. Sentiment Analysis is a field from Natural Language Processing with the objective to learn and identify behaviors on social networks like Twitter. This process works with three types of sentiments (positive, negative, or neutral opinions) about products, services, persons, organizations, or any other kind of entity about a specific text.

**OBJECTIVE**
 
The main objective of this tool is to evaluate the content from trending topics or tweets about traveling. This will help our clients to create a more user-centered product. Also, they will be able to understand and act more proactively on customer issues.
Using this Machine Learning tool, we can extract information from the final customer tweets and understand their needs. In this case, our clients will be capable to filter, and ordering according to their feeling about their brands and products.

**CLIENT**

This tool is focused on traveling startups, MKT agencies, businesses that want to monitor the reputation or brand image of their products, or any other user that wants to know about trends or traveling product behaviors.
The client can order in-depth customized reports about any specific topic or product related to traveling. The reports will contain current and trend charts, key concepts, associated with the requested topic. These reports will be broken by days, weeks, months.

![Architecture](https://user-images.githubusercontent.com/72115928/156955964-05a45a54-7dce-44cd-8e7f-0984ae726942.png)

**DATA**

All the data is public and will be obtained from the social network API Twitter, processed with Bigquery, analyzed with the Natural Language Processing API provided by Google, at the end, all the results will be visualized through Data Studio by Google.
We will be processing batches of 1500 tweets per run, divided into topics like Travel, Airbnb, Booking, Hotel, Trivago, Travel Agency, Despegar, Destination, Vacation, Instatravel, Tourism, etc.

**MODELING**

For this project, we will be using the machine learning tool powered by Google. This tool called Natural Processing Language API, will help us to reveal the structure and the meaning of the text. This Google tool transforms the text into a comprehensible unit for the machine by using text vectorization. 
We have an alternative and we can use traditional models. Some of these algorithms were selected because of their scalability. This alternative consists of taking a text sample, processing the piece of information until the model can predict with accuracy the sentiments of the tweet, then the text is the input for the classifier, and it will predict the sentiment as negative, neutral, or positive.

- Naive Bayes
  This probabilistic classifier will help us to learn about the pattern of an examined set of data previously categorized.
  
  ![Naive Bayes](https://user-images.githubusercontent.com/72115928/156931898-70efd6e1-774f-450a-9a20-0c7b8370b310.jpeg)
  
![Naive Bayes 2](https://user-images.githubusercontent.com/72115928/156932393-389682e6-49dc-4106-b40e-136212a75638.png)
  
- Support Vector Machines
  This model will be defining the decision boundaries. It will take into count two vectors. The input data already classified will be converted into a class. The next step is to find a margin between the two classes. The objective of this is to maximize the margin to reduce indecisive decisions. Also, SVM will help us to identify and recognize all the factors to understand the model successfully.
  
  ![SVM](https://user-images.githubusercontent.com/72115928/156932505-66ca22b6-c62c-4271-a8d6-550b5a905aa0.png)

- _k_-nearest neighborgs
  This approach will assign sentiment labels by creating vectors for each example in the test set and during the training. 
  
![KNN](https://user-images.githubusercontent.com/72115928/156932917-4333d0b9-7122-4985-9d2d-f3a885a117e5.png)

**EVALUATION** 
  
The evaluation will be based mainly on the quality of the data, we will check the number of followers of the accounts where we select the tweets. We will verify that they are not automatic advertising accounts that take advantage of trending news.

We check if our aplication satisfies objectives if the application solves the problem for which it was created,  its use implies low costs for users, it is quick and easy to consult. Also, if the application provides added value and finally, if it has benefits compared to other similar applications.

**INFERENCE**

•	We use batch predictions because they increase the speed of the calculation as they are performed on blocks of data and not on each unit, for which we use CPU. 

**COMPUTE**

•	We will need one or two CPU with the capacity to process 1500 tweets, which have words like:'travel','booking','hotel','trivago','airbnb','travel agency','travelling','vacation','instatravel','tourism','traveller','trip','journey','tour','tourist'.

**MVP (minimum viable product )**

We will extract tweets, calculate sentiment with the tools provided by Google and perform visualizations. 

How difficult is it to get there? :

• It could be a challenge to reach the MVP because we have 7 days from the ETL to select a model that allows us to maximize the advantages of the data and minimize the risks of a computationally expensive model. Furthermore, in this period resilience is required in order not to abandon the model easily after having failed attempts. Therefore, using the simplest and at the same time adequate model could help us a lot.

**PRE-MORTEMS**

Reasons for the project to fail:

• Lack of time to choose the best model

• Knowing how to implement an interface

• Knowledge of configuring an orchestrator

• The potential biases in our selection of words

• Lack of data cleanliness

• There is information about the business that we are not considering

### References

*  [How to successfully invest in machine learning in an MVP](https://sennalabs.com/th/blogs/how-to-successfully-invest-in-machine-learning-in-an-mvp)
*  [Why Facebook and Twitter Opened the Door to NFTs](https://www.bloomberg.com/opinion/articles/2022-01-25/why-facebook-and-twitter-opened-the-door-to-nfts)
*  [Manifiesto por el Desarrollo Ágil de Software](http://agilemanifesto.org/iso/es/manifesto.html)
*  [Las GPU como pasado, presente y futuro de la computación](https://www.xataka.com/componentes/las-gpu-como-pasado-presente-y-futuro-de-la-computacion)
*  [¿Éxito o fracaso? Indicadores para evaluar un proyecto](https://www.capterra.mx/blog/1114/exito-o-fracaso-indicadores-para-evaluar-un-proyecto)
*  [Notas aprendizaje de máquina, 2021](https://github.com/felipegonzalez/aprendizaje-maquina-mcd-2021)
*  [Machine learning on mobile: on the device or in the cloud?](https://machinethink.net/blog/machine-learning-device-or-cloud/)


