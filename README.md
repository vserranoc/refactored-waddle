# Arquitectura de Producto de Datos
## Team name: Serverless

## Team members:

|**Name**|**User**|
| ------------------ | ------------ |
|Luis|@LuisValdez07|
|Paulina Hernández Trejo|@pautrejo|
|Jesús Enrique Miranda Blanco |@jesusmb230795|
|Valeria Serrano Cote |@vserranoc|
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

  **Evaluation** 
  
1.	Model performance, both during training and inference:
•	We would review the performance of the model based on different error measures MSE, MAE
•	During training we would take care of filtering validation data in the training set.
•	We would check that future information variables were filtered, that is, we would observe that the selected variables do not include the response that we are trying to predict
•	We would try to use samples as similar as possible to the population we are trying to forecast.
•	We would carefully analyze that the data used is not censored
•	We would use a validation sample large enough to be able to discriminate between what performs well or poorly.
•	We will make cuts of different training/validation sizes and see what performance results from choosing a final model in a validation sample.

2.	If application satisfies objectives
1. I would identify if the application solves the problem for which it was created
2. I would observe that its use implies low costs for users, it is quick and easy to consult.
3. I would analyze if the application provides added value
4. I would identify its benefits compared to other similar applications

**Inference**

•	We use batch predictions because they increase the speed of the calculation as they are performed on blocks of data and not on each unit.
•	Run through a server Because  the infrastructure used produces faster processing.
•	A server provides cheap computing power and could only be paid for what is required.
•	Multiple models could be trained and downloaded.
•	Due to the amount of data, it is convenient to use a GPU, because they are efficient to process.

**Compute **

To train the model we require a GPU due to the amount and type of data, in a CPU the processing could be very slow. We estimate that we would require XXX GPU hours.

We could make predictions on CPUs if we reduced the size of the database, however, we could have complications due to the reduced number of data. Which would cause an overfitting and little predictive capacity.

We need capacity to store and process XXX TEXT records. Which contains an extension of XXX characters by XXXX.

**MVP (minimum viable product ) **

• ……which will imply reducing costs in terms of:
o Utilize team skills to the fullest
o Reduces the complexity of the problem
o Increases model accuracy
o Consider data quality
o The time taken for its implementation is low
o We require few hyperparameters, which is easier to adjust than having a large number

• It could be a challenge to reach the MVP because we have 7 days from the ETL to select a model that allows us to maximize the advantages of the data and minimize the risks of a computationally expensive model. Furthermore, in this period resilience is required in order not to abandon the model easily after having failed attempts. Therefore, using the simplest and at the same time adequate model could help us a lot.

**10. Pre-mortems **

Reasons for the project to fail
•	Lack of time to choose the best model
•	knowing how to implement an interface
•	Knowledge of configuring an orchestrator
o	Limitations of your application:  Technical aspects
•	The potential biases in our application:
There is information about the business that we are not considering

### References
*  [How to successfully invest in machine learning in an MVP]( https://sennalabs.com/th/blogs/how-to-successfully-invest-in-machine-learning-in-an-mvp)
*  [Why Facebook and Twitter Opened the Door to NFTs(Why Facebook and Twitter Opened the Door to NFTs - Bloomberg)
*  [Manifiesto por el Desarrollo Ágil de Software](http://agilemanifesto.org/iso/es/manifesto.html)
*  [Las GPU como pasado, presente y futuro de la computación](https://www.xataka.com/componentes/las-gpu-como-pasado-presente-y-futuro-de-la-computacion)
*  [¿Éxito o fracaso? Indicadores para evaluar un proyecto](https://www.capterra.mx/blog/1114/exito-o-fracaso-indicadores-para-evaluar-un-proyecto)
*  [Notas aprendizaje de máquina, 2021](https://github.com/felipegonzalez/aprendizaje-maquina-mcd-2021)
*  [Machine learning on mobile: on the device or in the cloud?](https://machinethink.net/blog/machine-learning-device-or-cloud/)


