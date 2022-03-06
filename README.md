# Arquitectura de Producto de Datos
## Team name: Serverless

## Team members:

|**Name**|**User**|
| ------------------ | ------------ |
|Luis|@LuisValdez07|
|Paulina Hernández Trejo|@pautrejo|
|Jesús Enrique Miranda Blanco |@jesusmb230795|
|Valeria|@vserranoc|
## About team
We think that we are an awesome team because we have mutual respect,common and aligned goals, open communication, patience, tolerance, everyone contributes, support each other, we complement each other, have fun, and overall, appreciate and encourage diverse thinking, learning and adaptation.

**##ABOUT THE PROJECT**


**OBJECTIVE**

One of the most relevant topics our days is sentiment analysis, with this tool we analyzed the sentiments derived from the conversations that occur on Twitter. Sentiment Analysis is a field from Natural Language Processing with the objective to learn and identify behaviors on the social network Twitter. This process works with three types of sentiments (positive, negative, or neutral opinions) about products, services, persons, organizations, or any other kind of entity about a specific text. With this tool, the user will be able to evaluate the content from trending topics or tweets. Also, will be able to filter, and order according to the feeling about one product.

For this project we will be applying:

Supervised Learning

**CLIENT**

This tool is focused on MKT agencies, businesses that want to monitor the reputation or brand image of their products, or any other user that wants to know about trends or product behaviors.
The client can order in-depth customized reports about any specific topic or product. The reports will contain current and trend charts, key concepts, associated with the requested topic. These reports will be broken by days, weeks, months.

![image](https://user-images.githubusercontent.com/72115928/156930736-bb1f9720-70e0-4563-9249-a246a5665bb9.png)

**DATA**

All the data is public and will be obtained from the social network API Twitter. 

**MODELING**

For this project, we will be using machine learning algorithms under supervision. As we need to train our model with many sample passages until the model can predict with accuracy the sentiments of the tweet, then the text is the input for the classifier and it will predict the sentiment as negative, neutral, or positive. We will be using traditional models and we selected these models because they are capable of scalability.

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

  
