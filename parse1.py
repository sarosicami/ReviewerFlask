import xml.etree.ElementTree as ET

def trainAspectData(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    train_data = list()
    for review in root.iter('Review'):
        sentences = review[0]
        reviewText = ''
        for sentence in sentences:
            reviewAspectTerms = []
            reviewPolarities = []
            reviewPolarity = ''
            for elem in sentence:
                if elem.tag == 'text':
                    reviewText = elem.text
                if elem.tag == 'Opinions':
                    aspect = 'None'
                    for subelem in elem:
                        aspect = subelem.attrib['aspect']
                        train_data.append((reviewText, aspect))
    return train_data

def trainAttributeData(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    train_data = list()
    for review in root.iter('Review'):
        sentences = review[0]
        reviewText = ''
        for sentence in sentences:
            reviewAspectTerms = []
            reviewPolarities = []
            reviewPolarity = ''
            for elem in sentence:
                if elem.tag == 'text':
                    reviewText = elem.text
                if elem.tag == 'Opinions':
                    attribute = 'None'
                    for subelem in elem:
                        attribute = subelem.attrib['attribute']
                        train_data.append((reviewText, attribute))
    return train_data

def trainPolarityData(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    train_data = list()
    for review in root.iter('Review'):
        sentences = review[0]
        reviewText = ''
        for sentence in sentences:
            reviewAspectTerms = []
            reviewPolarities = []
            reviewPolarity = ''
            for elem in sentence:
                if elem.tag == 'text':
                    reviewText = elem.text
                if elem.tag == 'Opinions':
                    polarity = 'None'
                    for subelem in elem:
                        polarity = subelem.attrib['polarity']
                        train_data.append((reviewText, polarity))
    return train_data