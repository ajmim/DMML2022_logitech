# README
**Github contributors**
Team Jeager
-	Mohamed Ajmi: mohamed.ajmi@unil.ch 
-	Maxime Pillard: maxime.pillard@unil.ch

### Description of the project
In the context of our Data Mining and Machine Learning course at the IS Master at HEC Lausanne, we worked on a language classification project.
The analysed data is composed of two columns, sentence and difficulty (labels).

In Part 1 of the project, we trained multiple models on the raw data (no cleaning or processing). The models were:
-	LogisticRegression
-	KNeighborsClassifier
-	DecisionTreeClassifier
-	RandomForestClassifier
-	XGBClassifier
In Part 2, we used the CamemBERT model to classify French sentences by language proficiency levels (A1, A2, B1, B2, C1, C2). We started by exploring the model and using the model documentation to understand its capabilities and how it works. However, we encountered some issues while implementing the model, so we adapted our code and explored the inner workings of the model to better understand it. Once we had a good understanding of the model, we were able to make improvements by adjusting some parameters.


### Summary table
[] ADD TABLE

### Link to video
[] ADD LINK

## Part 1
For each model, we run the accuracy, precision, f1 and recall score. We also used grid search to optimize the results.
To simplify our work, we used functions (create_and_train_pipeline & evaluate_clf) that automatically train and provide all required metrics.
The results are in the table obove. 

## Part 2
### Exploring the Model
Before we began using the CamemBERT model, we looked at other models, but none seemed to easily run French text. Additionally, this model was recommended by the teacher, which made us believe it is a good one.
At first, we tried to investigate how to implement a function using all the models we learned it our Part 1 (linear regression, Knn, tree, …), but to our surprises, we learned that the lighting model is already optimized to use them, and even tokenize, clean, and process the data for better results.
Then we familiarized ourselves with its documentation to understand its capabilities and how it could be trained. The CamemBERT model is a pre-trained language model based on the BERT architecture, which was trained on a large dataset of French language text. It is designed to perform well on a variety of natural language processing tasks, including sentence classification.
However, we run on some errors because we tried to manually create the dictionary used to create the 3 datasets (training, test, and validation). We thought that doing so would increase the speed of the model compared to loading it through an API (from Hugging Face). We fixed this issue by simply following the documentation and uploading our data to Hugging Face, that way we were sure that the format would be correct.

### Using the Model

To use the CamemBERT model for sentence classification, we followed the steps outlined in the documentation. We first loaded the model and prepared the input data by tokenizing and padding the sentences (done through the defined functions of the model). We then fed the input data into the model and used the output to predict the language proficiency level of each sentence. Our first result was looking great with an accuracy score around 5.5. We then focused on how to improve it.

### Exploring the Inner Workings of the Model and improving it

To improve the predictions, we focused on better understanding the model's behaviour, we examined the output at each step of the processing pipeline. We could understand the model thanks to 2 acquittances who explained how Pytorch and the LighteningModel worked.

To improve the model's performance, we experimented with adjusting:
-	The batch size. By increasing the batch size, we were able to process more input data at once. We noticed that the impact is worth spending a lot of time on it. The model seems to provide slightly less accuracy if the batch is decreased (batch size of 10 gave accuracy score of 5.4) and the same predictions if it is higher (we tested it up to batch size of 27). 
-	The number of iterations. We found that the training stopped between 5-12 iterations after finding that the model stopped improving its accuracy. Nevertheless, we tried to force it to go up to 20 and 50 noticing that this decreased the accuracy because of overfitting. We also tried to decrease the iteration giving us a score of 5.4 most of the time.
-	We increased the number of sentences in the training data set to better train the model. This allowed us to improve our accuracy up to 5.9.
-	Remove the shuffle on the training set, which resulted on the worth score so far: 1.9


### Conclusion

In this project, we used the CamemBERT model to classify sentences by language proficiency levels. We encountered some issues while implementing the model, but by exploring its inner workings and adjusting the batch size, iterations and adding data to the training dataset, we were able to improve its performance. Overall, the CamemBERT model proved to be a useful tool for language proficiency classification.
We have some ideas to further improve the model as:
-	Change gradient steps (lr parameter) into an even smaller one and change the weight decay. This has not been tested yet.
-	We could add more sentences with the condition of adding quality data (classification must match the sentence). From our testing, this could highly improve accuracy.
 

Vidéo avec slides et présentation (selon doc du prof)
Tables of progess over time à metrre dans le readme
•	Momo donne à Maxime ses résultats. Après Maxime se débrouille.

Le fichier de documentation. Finalement je crois qu'il faut expliquer nos choix et nos tests etc.
	momo
readme mini rapport et explications
Maxime et momo

- part 1 (je sais pas encore où tu en es)


