'''
Mohamed:
This file contains all the functions we need to run basing and repetitive code.
e.g. load, accuracy, ...
'''


from sklearn.preprocessing import LabelEncoder

import library_modules

def load_data(url):
    data = pd.read_csv(url, index_col=0,
                       dtype=str)
    data.sentence = data.sentence.apply(lambda s: s.replace("'", ' '))
    labels = data.difficulty.unique()
    num_labels = len(labels)
    data.difficulty = LabelEncoder().fit_transform(data.difficulty)
