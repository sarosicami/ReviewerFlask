import xml.etree.ElementTree as ET

def getProducts(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    products = list()
    products_info = list()
    reviews = list()
    for product in root.iter('Product'):
        # print(product)
        for elem in product:
            if elem.tag == 'brand':
                brand = elem.text
            if elem.tag == 'model':
                model = elem.text
            if elem.tag == 'processor':
                processor = elem.text
            if elem.tag == 'display':
                display = elem.text
            if elem.tag == 'RAM_memory':
                RAM_memory = elem.text
            if elem.tag == 'memory_speed':
                memory_speed = elem.text
            if elem.tag == 'hard_drive':
                hard_drive = elem.text
            if elem.tag == 'video_card':
                video_card = elem.text
            if elem.tag == 'card_description':
                card_description = elem.text
            if elem.tag == 'battery_life':
                battery_life = elem.text
            if elem.tag == 'item_weight':
                item_weight = elem.text
            if elem.tag == 'housing_material':
                housing_material = elem.text
            if elem.tag == 'color':
                color = elem.text
            if elem.tag == 'operating_system':
                operating_system = elem.text
        products_info.append((brand, model, processor, display, RAM_memory, memory_speed, hard_drive, video_card, card_description, battery_life, item_weight, housing_material, color, operating_system))
    for reviews_list in root.iter('Reviews'):
        product_reviews = list()
        for review in reviews_list:
            sentences = list()
            for elem in review:
                if elem.tag == 'user':
                    reviewUser = elem.text
                if elem.tag == 'text':
                    reviewText = elem.text
                if elem.tag == 'sentences':
                    for sentence in elem:
                        for subelem in sentence:
                            if subelem.tag == 'text':
                                sentenceText = subelem.text
                            if subelem.tag == 'Opinion':
                                aspect = subelem.attrib['aspect']
                                attribute = subelem.attrib['attribute']
                                emotion = subelem.attrib['emotion']
                                polarity = subelem.attrib['polarity']
                        sentences.append((sentenceText, aspect, attribute, emotion, polarity))
            product_reviews.append((reviewUser, reviewText, sentences))

        reviews.append(product_reviews)
    # print(reviews)

    for i in range(len(products_info)):
        products.append({'info': products_info[i], 'reviews':reviews[i]})

    return products

def trainAspectData(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    train_data = list()
    # for product in root.iter('Product'):
    #     print(product)
    for reviews_list in root.iter('Reviews'):
        product_reviews = list()
        for review in reviews_list:
            sentences = list()
            for elem in review:
                if elem.tag == 'user':
                    reviewUser = elem.text
                if elem.tag == 'text':
                    reviewText = elem.text
                if elem.tag == 'sentences':
                    for sentence in elem:
                        for subelem in sentence:
                            if subelem.tag == 'text':
                                sentenceText = subelem.text
                            if subelem.tag == 'Opinion':
                                aspect = subelem.attrib['aspect']
                                train_data.append((sentenceText, aspect))
    return train_data

def trainAttributeData(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    train_data = list()
    # for product in root.iter('Product'):
    #     print(product)
    for reviews_list in root.iter('Reviews'):
        product_reviews = list()
        for review in reviews_list:
            sentences = list()
            for elem in review:
                if elem.tag == 'user':
                    reviewUser = elem.text
                if elem.tag == 'text':
                    reviewText = elem.text
                if elem.tag == 'sentences':
                    for sentence in elem:
                        for subelem in sentence:
                            if subelem.tag == 'text':
                                sentenceText = subelem.text
                            if subelem.tag == 'Opinion':
                                attribute = subelem.attrib['attribute']
                                train_data.append((sentenceText, attribute))
    return train_data

def trainEmotionData(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    train_data = list()
    # for product in root.iter('Product'):
    #     print(product)
    for reviews_list in root.iter('Reviews'):
        product_reviews = list()
        for review in reviews_list:
            sentences = list()
            for elem in review:
                if elem.tag == 'user':
                    reviewUser = elem.text
                if elem.tag == 'text':
                    reviewText = elem.text
                if elem.tag == 'sentences':
                    for sentence in elem:
                        for subelem in sentence:
                            if subelem.tag == 'text':
                                sentenceText = subelem.text
                            if subelem.tag == 'Opinion':
                                emotion = subelem.attrib['emotion']
                                train_data.append((sentenceText, emotion))
    return train_data


def trainPolarityData(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    train_data = list()
    # for product in root.iter('Product'):
    #     print(product)
    for reviews_list in root.iter('Reviews'):
        product_reviews = list()
        for review in reviews_list:
            sentences = list()
            for elem in review:
                if elem.tag == 'user':
                    reviewUser = elem.text
                if elem.tag == 'text':
                    reviewText = elem.text
                if elem.tag == 'sentences':
                    for sentence in elem:
                        for subelem in sentence:
                            if subelem.tag == 'text':
                                sentenceText = subelem.text
                            if subelem.tag == 'Opinion':
                                polarity = subelem.attrib['polarity']
                                train_data.append((sentenceText, polarity))
    return train_data