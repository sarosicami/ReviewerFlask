import pycrfsuite
import extract
import evaluate
import labelType
from sklearn.preprocessing import MultiLabelBinarizer

def reviewsAspectData(train_reviews):
    X_train = [extract.review_features_romanian(text, labelType.Label.aspect) for (text, label) in train_reviews]
    Y_train = []
    for i in range(len(X_train)):
        features_length = len(X_train[i])
        # print(X_train[i])
        (text, label) = train_reviews[i]
        y_train = []
        for i in range(features_length):
            y_train.append(label)
        Y_train.append(y_train)

    trainer = pycrfsuite.Trainer(verbose=False)
    for xseq, yseq in zip(X_train, Y_train):
        trainer.append(xseq, yseq)
    trainer.set_params({
        'c1': 1.0,   # coefficient for L1 penalty
        'c2': 1e-3,  # coefficient for L2 penalty
        'max_iterations': 50,  # stop earlier
        #  include transitions that are possible, but not observed
        'feature.possible_transitions': True
    })

    trainer.train('Aspects.crfsuite')

def reviewsAttributeData(train_reviews):
    X_train = [extract.review_features_romanian(text, labelType.Label.attribute) for (text, label) in train_reviews]
    Y_train = []
    for i in range(len(X_train)):
        features_length = len(X_train[i])
        # print(X_train[i])
        (text, label) = train_reviews[i]
        y_train = []
        for i in range(features_length):
            y_train.append(label)
        Y_train.append(y_train)

    trainer = pycrfsuite.Trainer(verbose=False)
    for xseq, yseq in zip(X_train, Y_train):
        trainer.append(xseq, yseq)
    trainer.set_params({
        'c1': 1.0,   # coefficient for L1 penalty
        'c2': 1e-3,  # coefficient for L2 penalty
        'max_iterations': 50,  # stop earlier
        #  include transitions that are possible, but not observed
        'feature.possible_transitions': True
    })

    trainer.train('Attributes.crfsuite')

def reviewsPolarityData(train_reviews):
    X_train = [extract.review_features_romanian(text, labelType.Label.polarity) for (text, label) in train_reviews]
    Y_train = []
    for i in range(len(X_train)):
        features_length = len(X_train[i])
        # print(X_train[i])
        (text, label) = train_reviews[i]
        y_train = []
        for i in range(features_length):
            y_train.append(label)
        Y_train.append(y_train)

    trainer = pycrfsuite.Trainer(verbose=False)
    for xseq, yseq in zip(X_train, Y_train):
        trainer.append(xseq, yseq)
    trainer.set_params({
        'c1': 1.0,   # coefficient for L1 penalty
        'c2': 1e-3,  # coefficient for L2 penalty
        'max_iterations': 50,  # stop earlier
        #  include transitions that are possible, but not observed
        'feature.possible_transitions': True
    })

    trainer.train('Polarities.crfsuite')

def reviewsEmotionData(train_reviews):
    X_train = [extract.review_features_romanian(text, labelType.Label.emotion) for (text, label) in train_reviews]
    Y_train = []
    for i in range(len(X_train)):
        features_length = len(X_train[i])
        # print(X_train[i])
        (text, label) = train_reviews[i]
        y_train = []
        for i in range(features_length):
            y_train.append(label)
        Y_train.append(y_train)

    trainer = pycrfsuite.Trainer(verbose=False)
    for xseq, yseq in zip(X_train, Y_train):
        trainer.append(xseq, yseq)
    trainer.set_params({
        'c1': 1.0,   # coefficient for L1 penalty
        'c2': 1e-3,  # coefficient for L2 penalty
        'max_iterations': 50,  # stop earlier
        #  include transitions that are possible, but not observed
        'feature.possible_transitions': True
    })

    trainer.train('Emotions.crfsuite')