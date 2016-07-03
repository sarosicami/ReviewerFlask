import pycrfsuite
import extract
import evaluate
import labelType
from sklearn.preprocessing import MultiLabelBinarizer

def reviewsAspectData(test_reviews):
    # trainer.train('Laptops.crfsuite')
    tagger = pycrfsuite.Tagger()
    tagger.open('Aspects.crfsuite')

    X_test = [extract.review_features_romanian(text, labelType.Label.aspect) for text in test_reviews]
    Y_pred = [tagger.tag(xseq) for xseq in X_test]

    Y_pred_final = []
    for y_pred in Y_pred:
        Y_pred_final.append(y_pred[0])

    return Y_pred_final


def reviewsAttributeData(test_reviews):
    tagger = pycrfsuite.Tagger()
    tagger.open('Attributes.crfsuite')

    X_test = [extract.review_features_romanian(text, labelType.Label.attribute) for text in test_reviews]
    Y_pred = [tagger.tag(xseq) for xseq in X_test]

    Y_pred_final = []
    for y_pred in Y_pred:
        Y_pred_final.append(y_pred[0])

    return Y_pred_final


def reviewsPolarityData(test_reviews):
    tagger = pycrfsuite.Tagger()
    tagger.open('Polarities.crfsuite')

    X_test = [extract.review_features_romanian(text, labelType.Label.polarity) for text in test_reviews]
    Y_pred = [tagger.tag(xseq) for xseq in X_test]

    Y_pred_final = []
    for y_pred in Y_pred:
        Y_pred_final.append(y_pred[0])

    return Y_pred_final


def reviewsEmotionData(test_reviews):
    tagger = pycrfsuite.Tagger()
    tagger.open('Emotions.crfsuite')

    X_test = [extract.review_features_romanian(text, labelType.Label.emotion) for text in test_reviews]
    Y_pred = [tagger.tag(xseq) for xseq in X_test]

    Y_pred_final = []
    for y_pred in Y_pred:
        Y_pred_final.append(y_pred[0])

    return Y_pred_final