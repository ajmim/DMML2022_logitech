'''
Mohamed:
This file contains all the functions we need to run basing and repetitive code.
e.g. load, accuracy, ...
'''
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline

def create_and_train_pipeline(classifier, X_train, y_train):
    pipe = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', classifier()),
    ])

    pipe.fit(X_train, y_train)
    return pipe


def evaluate_clf(clf, X_test, y_test, labels, full=False):
    predicted = clf.predict(X_test)
    if full:
        return classification_report(y_test, predicted, target_names=labels)
    else:
        return np.mean(y_test == predicted)
