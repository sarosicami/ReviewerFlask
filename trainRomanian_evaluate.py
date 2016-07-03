import pycrfsuite
import extract
import evaluate
import labelType
from sklearn.preprocessing import MultiLabelBinarizer

def reviewsAspectData(reviews):
    # reviews_withoutStop = extract.reviewsWithoutStopWords(reviews)
    train_reviews = reviews[0:175]
    test_reviews = reviews[175:len(reviews)]
    X_train = [extract.review_features_romanian(text, labelType.Label.aspect) for (text, label) in train_reviews]
    Y_train = []
    for i in range(len(train_reviews)):
        features_length = len(X_train[i])
        (text, label) = train_reviews[i]
        y_train = []
        for i in range(features_length):
            y_train.append(label)
        Y_train.append(y_train)
    # print(len(X_train[0]))
    # print(X_train[0])
    # print(X_train[1])
    # print(X_train[2])
    # print(len(Y_train[0]))
    # print(Y_train[0])


    X_test = [extract.review_features_romanian(text, labelType.Label.aspect) for (text, label) in test_reviews]
    Y_test = []
    for i in range(len(test_reviews)):
        features_length = len(X_test[i])
        (text, label) = test_reviews[i]
        y_test = []
        for i in range(features_length):
            y_test.append(label)
        Y_test.append(y_test)

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

    trainer.train('Laptops.crfsuite')
    tagger = pycrfsuite.Tagger()
    tagger.open('Laptops.crfsuite')

    # print("Predicted:", ' '.join(tagger.tag(extract.review_features_romanian('nice keyboard', labelType.Label.aspect))))
    # print("Correct1:  ", ' '.join(extract.review_labels(('este usor', 'Laptop#General'))))

    Y_pred = [tagger.tag(xseq) for xseq in X_test]

    Y_test_final = []
    for y_test in Y_test:
        Y_test_final.append(y_test[0])
    Y_pred_final = []
    for y_pred in Y_pred:
        Y_pred_final.append(y_pred[0])
    print(Y_test_final)
    print(Y_pred_final)
    # print(len(set(Y_test_final)))
    # print(len(set(Y_pred_final)))
    print(evaluate.classification_report(Y_test_final, Y_pred_final))


def reviewsAttributeData(reviews):
    # reviews_withoutStop = extract.reviewsWithoutStopWords(reviews)
    train_reviews = reviews[0:175]
    test_reviews = reviews[175:len(reviews)]
    # test_reviews = [('best laptop ever', 'LAPTOP#GENERAL')]
    X_train = [extract.review_features_romanian(text, labelType.Label.attribute) for (text, label) in train_reviews]
    Y_train = []
    for i in range(len(train_reviews)):
        features_length = len(X_train[i])
        (text, label) = train_reviews[i]
        y_train = []
        for i in range(features_length):
            y_train.append(label)
        Y_train.append(y_train)
    # print(len(X_train[0]))
    # print(X_train[0])
    # print(X_train[1])
    # print(X_train[2])
    # print(len(Y_train[0]))
    # print(Y_train[0])


    X_test = [extract.review_features_romanian(text, labelType.Label.attribute) for (text, label) in test_reviews]
    Y_test = []
    for i in range(len(test_reviews)):
        features_length = len(X_test[i])
        (text, label) = test_reviews[i]
        y_test = []
        for i in range(features_length):
            y_test.append(label)
        Y_test.append(y_test)

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

    trainer.train('Laptops.crfsuite')
    tagger = pycrfsuite.Tagger()
    tagger.open('Laptops.crfsuite')

    # print("Predicted:", ' '.join(tagger.tag(extract.review_features_romanian('nice keyboard', labelType.Label.attribute))))
    # print("Correct1:  ", ' '.join(extract.review_labels(('este usor', 'Laptop#General'))))

    Y_pred = [tagger.tag(xseq) for xseq in X_test]

    Y_test_final = []
    for y_test in Y_test:
        Y_test_final.append(y_test[0])
    Y_pred_final = []
    for y_pred in Y_pred:
        Y_pred_final.append(y_pred[0])
    print(Y_test_final)
    print(Y_pred_final)
    # print(len(set(Y_test_final)))
    # print(len(set(Y_pred_final)))
    print(evaluate.classification_report(Y_test_final, Y_pred_final))


def reviewsPolarityData(reviews):
    # reviews_withoutStop = extract.reviewsWithoutStopWords(reviews)
    train_reviews = reviews[0:175]
    test_reviews = reviews[175:len(reviews)]
    # test_reviews = [('best laptop ever', 'LAPTOP#GENERAL')]
    X_train = [extract.review_features_romanian(text, labelType.Label.polarity) for (text, label) in train_reviews]
    Y_train = []
    for i in range(len(train_reviews)):
        features_length = len(X_train[i])
        (text, label) = train_reviews[i]
        y_train = []
        for i in range(features_length):
            y_train.append(label)
        Y_train.append(y_train)
    # print(len(X_train[0]))
    # print(X_train[0])
    # print(X_train[1])
    # print(X_train[2])
    # print(len(Y_train[0]))
    # print(Y_train[0])


    X_test = [extract.review_features_romanian(text, labelType.Label.polarity) for (text, label) in test_reviews]
    Y_test = []
    for i in range(len(test_reviews)):
        features_length = len(X_test[i])
        (text, label) = test_reviews[i]
        y_test = []
        for i in range(features_length):
            y_test.append(label)
        Y_test.append(y_test)

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

    trainer.train('Laptops.crfsuite')
    tagger = pycrfsuite.Tagger()
    tagger.open('Laptops.crfsuite')

    # print("Predicted:", ' '.join(tagger.tag(extract.review_features_romanian('nice keyboard', labelType.Label.polarity))))
    # print("Correct1:  ", ' '.join(extract.review_labels(('este usor', 'Laptop#General'))))

    Y_pred = [tagger.tag(xseq) for xseq in X_test]

    Y_test_final = []
    for y_test in Y_test:
        Y_test_final.append(y_test[0])
    Y_pred_final = []
    for y_pred in Y_pred:
        Y_pred_final.append(y_pred[0])
    print(Y_test_final)
    print(Y_pred_final)
    # print(len(set(Y_test_final)))
    # print(len(set(Y_pred_final)))
    print(evaluate.classification_report(Y_test_final, Y_pred_final))


def reviewsEmotionData(reviews):
    # reviews_withoutStop = extract.reviewsWithoutStopWords(reviews)
    train_reviews = reviews[0:175]
    test_reviews = reviews[175:len(reviews)]
    # test_reviews = [('best laptop ever', 'LAPTOP#GENERAL')]
    X_train = [extract.review_features_romanian(text, labelType.Label.emotion) for (text, label) in train_reviews]
    Y_train = []
    for i in range(len(train_reviews)):
        features_length = len(X_train[i])
        (text, label) = train_reviews[i]
        y_train = []
        for i in range(features_length):
            y_train.append(label)
        Y_train.append(y_train)
    # print(len(X_train[0]))
    print(X_train[0])
    # print(X_train[1])
    # print(X_train[2])
    # print(len(Y_train[0]))
    print(Y_train[0])


    X_test = [extract.review_features_romanian(text, labelType.Label.emotion) for (text, label) in test_reviews]
    Y_test = []
    for i in range(len(test_reviews)):
        features_length = len(X_test[i])
        (text, label) = test_reviews[i]
        y_test = []
        for i in range(features_length):
            y_test.append(label)
        Y_test.append(y_test)

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

    trainer.train('Laptops.crfsuite')
    tagger = pycrfsuite.Tagger()
    tagger.open('Laptops.crfsuite')

    # print("Predicted:", ' '.join(tagger.tag(extract.review_features_romanian('nice keyboard', labelType.Label.emotion))))
    # print("Correct1:  ", ' '.join(extract.review_labels(('este usor', 'Laptop#General'))))

    Y_pred = [tagger.tag(xseq) for xseq in X_test]

    Y_test_final = []
    for y_test in Y_test:
        Y_test_final.append(y_test[0])
    Y_pred_final = []
    for y_pred in Y_pred:
        Y_pred_final.append(y_pred[0])
    print(Y_test_final)
    print(Y_pred_final)
    # print(len(set(Y_test_final)))
    # print(len(set(Y_pred_final)))
    print(evaluate.classification_report(Y_test_final, Y_pred_final))