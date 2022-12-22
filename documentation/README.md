# Documentation

## Introduction

In this project, we used the camamBERT model to classify sentences by language proficiency levels (A1, A2, B1, B2, C1, C2). We started by exploring the model and using the model documentation to understand its capabilities and how it works. However, we encountered some issues while implementing the model, so we adapted our code and explored the inner workings of the model to better understand it. Once we had a good understanding of the model, we were able to make improvements by adjusting the batch size and echo periods (iterations).

##Exploring the Model

Before we began using the camamBERT model, we familiarized ourselves with its documentation to understand its capabilities and how it was trained. The camamBERT model is a pre-trained language model based on the BERT architecture, which was trained on a large dataset of French language text. It is designed to perform well on a variety of natural language processing tasks, including sentence classification.

##Using the Model

To use the camamBERT model for sentence classification, we followed the steps outlined in the documentation. We first loaded the model and prepared the input data by tokenizing and padding the sentences. We then fed the input data into the model and used the output to predict the language proficiency level of each sentence.

##Encountering Issues

While implementing the model, we encountered some issues with the output. The model was not producing accurate predictions for some of the sentences, and we were not sure why. To troubleshoot the issue, we adapted our code to explore how the model was processing the input data and making predictions.

## Exploring the Inner Workings of the Model

To better understand the model's behavior, we examined the output at each step of the processing pipeline. We found that the model was having difficulty with sentences that contained uncommon or out-of-vocabulary words. These words were being represented by a special token called [UNK], which was causing the model to make incorrect predictions.

## Improving the Model

To improve the model's performance, we experimented with adjusting the batch size and echo periods (iterations). By increasing the batch size, we were able to process more input data at once, which helped the model make more accurate predictions. Similarly, increasing the number of echo periods allowed the model to process the input data more thoroughly, which also improved its performance.

## Conclusion

In this project, we used the camamBERT model to classify sentences by language proficiency levels. We encountered some issues while implementing the model, but by exploring its inner workings and adjusting the batch size and echo periods, we were able to improve its performance. Overall, the camamBERT model proved to be a useful tool for language proficiency classification.
