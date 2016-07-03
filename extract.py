from spacy.en import English
nlp = English()
from textblob import TextBlob
from nltk.corpus import stopwords
from spacy.parts_of_speech import VERB
from spacy.parts_of_speech import ADV
from spacy.parts_of_speech import ADJ
from spacy.parts_of_speech import NOUN
from spacy.parts_of_speech import DET
from spacy.parts_of_speech import CONJ
from spacy.parts_of_speech import PUNCT
import  nltk
from nltk.corpus import opinion_lexicon
import labelType

def review_words(reviewText):
    reviewText_TextBlob = TextBlob(reviewText)
    return reviewText_TextBlob.words

def review_sentences(reviewText):
    reviewText_TextBlob = TextBlob(reviewText)
    return reviewText_TextBlob.sentences

def reviewWordsList_withoutStopWords(review):
    new_words = [word for word in review_words(review) if word not in stopwords.words('english')]
    return new_words

def reviewsWithoutStopWords(reviews):
    for review in reviews:
        return [(reviewWordsList_withoutStopWords(review), attribute) for (review, attribute) in reviews]

def split_review_based_on_punctuation(reviewText):
    new_reviewText = reviewText.replace('\n', ' ')
    review_spacy = nlp(new_reviewText)

    new_sentences = []
    punct_positions = []
    for k in range(0, len(review_spacy)):
        # print(doc[k])
        if review_spacy[k].is_punct and not review_spacy[k].orth_ in ['-', ':']:
            punct_positions.append(k)
    start = 0
    if len(punct_positions) > 0:
        for p in range(0, len(punct_positions)):
            if p == len(punct_positions) - 1:
                new_sentences.append(review_spacy[start:len(review_spacy)].text)
            else:
                q = punct_positions[p]
                new_sentences.append(review_spacy[start:q].text)
                start = q + 1
                # while q < len(review_spacy):
                #     if review_spacy[q].is_punct:
                #         print('bla')
                #         print(review_spacy[start:q].text)
                #         new_sentences.append(review_spacy[start:q].text)
                #         start = q
                #         break
                #     q += 1
    else:
        new_sentences.append(reviewText)
    return new_sentences

def split_sentence_based_on_verbs(reviewText):
    review_spacy = nlp(reviewText)
    review_textblob = TextBlob(reviewText)
    if not review_textblob.detect_language() == 'en':
        review_textblob = review_textblob.translate(to='en')
        review_spacy = nlp(review_textblob.string)
    else:
        contains_romanian_words = 0

        for word in review_textblob.words:
            word_textblob = TextBlob(word)
            if len(word_textblob.string) >= 3 and word_textblob.detect_language() == 'ro':
                contains_romanian_words = 1
                break

        if contains_romanian_words == 1:
            new_reviewText = ''
            for word in review_spacy:
                word_textblob = TextBlob(word.orth_)
                if not word.is_title and len(word_textblob.string) >= 3:
                    if word_textblob.detect_language() != 'ro':
                        new_reviewText = new_reviewText + ' ' + word_textblob.string
                    else:
                        new_word = word_textblob.translate(to='en')
                        new_reviewText = new_reviewText + ' ' + new_word.string
                else :
                    new_reviewText = new_reviewText + ' ' + word_textblob.string
                    # only_english_words = 0
                    # break
            review_textblob = TextBlob(new_reviewText)
            review_spacy = nlp(review_textblob.string)

    new_sentences = []
    verbs_positions = []
    for k in range(0, len(review_spacy)):
        if review_spacy[k].pos == VERB and review_spacy[k].dep_ == 'ROOT':
            verbs_positions.append(k)
    start = 0
    if len(verbs_positions) > 0:
        for p in range(0, len(verbs_positions)):
            if p == len(verbs_positions) - 1:
                new_sentences.append(review_spacy[start:len(review_spacy)].text)
            else:
                q = verbs_positions[p] + 1
                while q < len(review_spacy):
                    if review_spacy[q].is_stop and ((review_spacy[q].pos == CONJ and (q < len(review_spacy)-1 and review_spacy[q-1].pos != review_spacy[q+1].pos)) or (review_spacy[q].pos == DET and review_spacy[q].lower_ in ['the', 'this', 'those', 'which', 'other', 'another']) or (review_spacy[q].pos == PUNCT and review_spacy[q] in [',', ';'])):
                        new_sentences.append(review_spacy[start:q].text)
                        start = q
                        break
                    q += 1
    else:
        new_sentences.append(reviewText)
    return new_sentences

def wordIsSubjectFeature(word):
    if 'subj' in word.dep_:
        return 1;
    return 0;

def wordIsAdjectiveFeature(word):
    if word.pos == ADJ:
        return 1;
    return 0;

def wordIsAdjectivePrecededByVerbFeature(word, review_spacy, i):
    if word.pos == ADJ and (i > 1 and review_spacy[i-1].pos == VERB):
            return 1;
    return 0;

def wordIsNounAndDirectObjAndPrecededByAdjectiveFeature(word, review_spacy, i):
    if word.pos == NOUN and word.dep_ == 'dobj' and (i > 1 and review_spacy[i-1].pos == ADJ):
        return 1;
    return 0;

def wordIsNounFollowedByVerbFollowedByAdjectiveFeature(word, review_spacy, i):
    if word.pos == NOUN and (i < len(review_spacy) -1 and review_spacy[i+1].pos == VERB) and (i < len(review_spacy) - 2 and review_spacy[i+1].pos == ADJ):
        return 1;
    return 0;

def wordSentenceContainsOpinionatedWords(review_spacy):
    for word in review_spacy:
        if word.orth_ in opinion_lexicon.positive() or word in opinion_lexicon.negative():
            return 1
    return 0

def wordSentenceContainsNounPhrases(review_textblob):
    if len(review_textblob.noun_phrases) > 0:
        return 1
    return 0

def nearestOpinionatedWord(review_spacy, word):
    # print(word)
    for i in range(len(review_spacy)):
        left_nearest_op_word = ''
        right_nearest_op_word = ''
        left_dist = 0
        right_dist = 0
        if review_spacy[i] == word:
            j = i - 1
            while j >= 0:
                word_spacy = review_spacy[j]
                # print('left')
                # print(TextBlob(word_spacy.orth_).sentiment.polarity)
                if TextBlob(word_spacy.orth_).sentiment.polarity != 0:
                    left_dist = i - j
                    left_nearest_op_word = word_spacy.orth_
                    break
                j = j - 1

            q = i + 1
            while q < len(review_spacy):
                word_spacy = review_spacy[q]
                # print('right')
                # print(TextBlob(word_spacy.orth_).sentiment.polarity)
                if TextBlob(word_spacy.orth_).sentiment.polarity != 0:
                    right_dist = q - i
                    right_nearest_op_word = word_spacy.orth_
                    break
                q = q + 1
        if left_dist > 0 and right_dist > 0:
            if left_dist < right_dist:
                # print('first '+left_nearest_op_word)
                return left_nearest_op_word
            else:
                # print('second '+right_nearest_op_word)
                return right_nearest_op_word
        elif left_dist > 0:
            # print('third '+left_nearest_op_word)
            return left_nearest_op_word
        elif right_dist > 0:
            # print('fourth '+right_nearest_op_word)
            return right_nearest_op_word
    return ''

def distanceToNearestOpinionatedWord(review_spacy, word):
    # print(word)
    for i in range(len(review_spacy)):
        left_dist = 0
        right_dist = 0
        if review_spacy[i] == word:
            j = i - 1
            while j >= 0:
                word_spacy = review_spacy[j]
                # print('left')
                # print(TextBlob(word_spacy.orth_).sentiment.polarity)
                if TextBlob(word_spacy.orth_).sentiment.polarity != 0:
                    left_dist = i - j
                    break
                j = j - 1

            q = i + 1
            while q < len(review_spacy):
                word_spacy = review_spacy[q]
                # print('right')
                # print(TextBlob(word_spacy.orth_).sentiment.polarity)
                if TextBlob(word_spacy.orth_).sentiment.polarity != 0:
                    right_dist = q - i
                    break
                q = q + 1
        if left_dist > 0 and right_dist > 0:
            if left_dist < right_dist:
                # print('first '+left_nearest_op_word)
                return left_dist
            else:
                # print('second '+right_nearest_op_word)
                return right_dist
        elif left_dist > 0:
            # print('third '+left_nearest_op_word)
            return left_dist
        elif right_dist > 0:
            # print('fourth '+right_nearest_op_word)
            return right_dist
    return 0


def distanceToNearestDomainWord(review_spacy, word):
    domain_words = ['laptop', 'computer', 'desktop', 'mac', 'pc', 'notebook', 'keyboard', 'mouse', 'battery', 'program', 'website', 'internet', 'software', 'hardware'
                    'display', 'audio', 'video', 'monitor', 'RAM', 'memory', 'os', 'operating system', 'operating', 'system', 'processor', 'hard drive',
                    'hard', 'drive', 'usb', 'flash memory', 'flash', 'wifi', 'touchscreen', 'application', 'app', 'price', 'color', 'material', 'weight', 'anti-virus', 'bug', 'cache'
                    'graphics card', 'graphics', 'card', 'internet', 'ipad', 'peripheral', 'windows', 'linux', 'ubuntu', 'algorithm', 'backup'
                    'browser', 'caps lock', 'caps', 'lock', 'cd', 'cloud', 'cpu', 'database', 'download', 'upload', 'performance', 'encrypt'
                    'firewall', 'firmware', 'login', 'logout', 'malware', 'media', 'moder', 'router', 'network', 'mutimedia', 'offline', 'online'
                    'username', 'password', 'web', 'website', 'camera', 'password', 'privacy', 'qwerty', 'resolution', 'screen', 'security', 'user interface',
                    'user', 'interface', 'install', 'virus', 'portability', 'buy', 'fast', 'slow', 'quality', 'design', 'problem', 'wireless', 'speed', 'machine', 'company'
                    'opinion', 'review', 'product', 'warranty', 'design', 'expensive', 'cheap', 'charger', 'purchase', 'size']
    # print(word)
    for i in range(len(review_spacy)):
        left_dist = 0
        right_dist = 0
        if review_spacy[i] == word:
            j = i - 1
            while j >= 0:
                word_spacy = review_spacy[j]
                # print('left')
                if word_spacy.lower_ or word_spacy.lower_.lemma_ in domain_words:
                    left_dist = i - j
                    break
                j = j - 1

            q = i + 1
            while q < len(review_spacy):
                word_spacy = review_spacy[q]
                # print('right')
                if word_spacy.lower_ or word_spacy.lower_.lemma_ in domain_words:
                    right_dist = q - i
                    break
                q = q + 1
        if left_dist > 0 and right_dist > 0:
            if left_dist < right_dist:
                # print('first '+left_nearest_op_word)
                return left_dist
            else:
                # print('second '+right_nearest_op_word)
                return right_dist
        elif left_dist > 0:
            # print('third '+left_nearest_op_word)
            return left_dist
        elif right_dist > 0:
            # print('fourth '+right_nearest_op_word)
            return right_dist
    return 0


def dependency_labels_to_root(token):
    '''Walk up the syntactic tree, collecting the arc labels.'''
    dep_labels = []
    while token.head is not token:
        dep_labels.append(token.dep_)
        token = token.head
    return dep_labels

def wordIsSentimentShifter(word):
    sentiment_shifters = ['no', 'not', 'never', 'would', 'should', 'could']
    if word.lower_ in sentiment_shifters:
        return 1
    return 0

def wordIsDomainWord(word):
    domain_words = ['laptop', 'computer', 'desktop', 'mac', 'pc', 'notebook', 'keyboard', 'mouse', 'battery', 'program', 'website', 'internet', 'software', 'hardware'
                    'display', 'audio', 'video', 'monitor', 'RAM', 'memory', 'os', 'operating system', 'operating', 'system', 'processor', 'hard drive',
                    'hard', 'drive', 'usb', 'flash memory', 'flash', 'wifi', 'touchscreen', 'application', 'app', 'price', 'color', 'material', 'weight', 'anti-virus', 'bug', 'cache'
                    'graphics card', 'graphics', 'card', 'internet', 'ipad', 'peripheral', 'windows', 'linux', 'ubuntu', 'algorithm', 'backup'
                    'browser', 'caps lock', 'caps', 'lock', 'cd', 'cloud', 'cpu', 'database', 'download', 'upload', 'performance', 'encrypt'
                    'firewall', 'firmware', 'login', 'logout', 'malware', 'media', 'moder', 'router', 'network', 'mutimedia', 'offline', 'online'
                    'username', 'password', 'web', 'website', 'camera', 'password', 'privacy', 'qwerty', 'resolution', 'screen', 'security', 'user interface',
                    'user', 'interface', 'install', 'virus', 'portability', 'buy', 'fast', 'slow', 'quality', 'design', 'problem', 'wireless', 'speed', 'machine', 'company'
                    'opinion', 'review', 'product', 'warranty', 'design', 'expensive', 'cheap', 'charger', 'purchase', 'size']
    if word.lower_ or word.lower_.lemma_ in domain_words:
        return 1
    return 0

def word_aspect_features(review_spacy, review_textblob, review_spacy_ents, i):
    # print(review_spacy)
    word = review_spacy[i]
    previous_neighbour = word
    next_neighbour = word
    if i > 0:
        previous_neighbour = review_spacy[i-1]
    if i + 1 < len(review_spacy):
        next_neighbour = review_spacy[i+1]
    # print(review_spacy)
    # print(word)
    # print(word.head)
    # print(dependency_labels_to_root(word))
    # print(word.head)
    # print(word.left_edge)
    # print(word.right_edge)
    word_ent_label = ''
    for ent in review_spacy_ents:
        if word in ent:
            word_ent_label = ent.label_

    pos = i
    features = [
        'bias',
        'word.lower=' + word.lower_,
        'word.lemma=' + word.lemma_,
        'word is out of vocabulary=%s' % word.is_oov,
        # 'word position=%s' % pos,
        # 'word.isstop=%s' % word.is_stop,
        # 'word.count=%s' % review_textblob.word_counts[word.orth_],
        'word.istitle=%s' % word.is_title,
        'word entity label=' + word_ent_label,
        'word is like_num=%s' % word.like_num,
        # 'word polarity:%s' % TextBlob(word.orth_).sentiment.polarity,
        'pos=' + word.pos_,
        'postag=' + word.tag_,
        'depend=' + word.dep_,
        # 'word parser head pos =' + word.head.pos_,
        'word previous neighbour pos=' + previous_neighbour.pos_,
        'word next neighbour pos=' + next_neighbour.pos_,
        # 'word distance to nearest opinionated word=%s' % distanceToNearestOpinionatedWord(review_spacy, word),
        # 'word distance to nearest domain word = %s' % distanceToNearestDomainWord(review_spacy, word),
        'word is domain word=%s' % wordIsDomainWord(word)
        # 'word previous neighbour dep=' + previous_neighbour.dep_,
        # 'word next neighbour dep=' + next_neighbour.dep_,
        # 'word is subject=%s' % wordIsSubjectFeature(word),
        # 'word nearest opinionated word=' + nearestOpinionatedWord(review_spacy, word)
        # 'word is adjective and preceded by verb=%s' % wordIsAdjectivePrecededByVerbFeature(word, review_spacy, i),
        # 'word is noun and direct object and preceded by adjective=%s' % wordIsNounAndDirectObjAndPrecededByAdjectiveFeature(word, review_spacy, i),
        # 'word is noun followed by verb followed by adjective=%s' %wordIsNounFollowedByVerbFollowedByAdjectiveFeature(word,review_spacy,i),
        # 'word sentence contains opinionated words=%s' % wordSentenceContainsOpinionatedWords(review_spacy),
        # 'word sentence contains noun phrases=%s' % wordSentenceContainsNounPhrases(review_textblob)
        ]

    if i > 0:
        word1 = review_spacy[i-1]
        word_ent_label = ''
        for ent in review_spacy_ents:
            if word1 in ent:
                word_ent_label = ent.label_

        previous_neighbour = word1
        next_neighbour = word1
        if i - 1 > 0:
            previous_neighbour = review_spacy[i-2]
        if i < len(review_spacy):
            next_neighbour = review_spacy[i]

        pos = i-1
        features.extend([
            '-1:word.lower=' + word1.lower_,
            '-1:word.lemma=' + word1.lemma_,
            '-1:word is out of vocabulary=%s' % word1.is_oov,
            # '-1:word position=%s' % pos,
            # '-1:word.isstop=%s' % word1.is_stop,
            # '-1:word.count=%s' % review_textblob.word_counts[word1.orth_],
            '-1:word.istitle=%s' % word1.is_title,
            '-1:word entity label' + word_ent_label,
            '-1:word is like_num=%s' % word1.like_num,
            # '-1:word polarity:%s' % TextBlob(word1.orth_).sentiment.polarity,
            '-1:pos=' + word1.pos_,
            '-1:postag=' + word1.tag_,
            '-1:depend=' + word1.dep_,
            # '-1:word parser head pos' + word1.head.pos_,
            '-1:word previous neighbour pos=' + previous_neighbour.pos_,
            '-1:word next neighbour pos=' + next_neighbour.pos_,
            # '-1:word distance to nearest opinionated word=%s' % distanceToNearestOpinionatedWord(review_spacy, word1),
            # '-1:word distance to nearest domain word = %s' % distanceToNearestDomainWord(review_spacy, word1),
            '-1:word is domain word=%s' % wordIsDomainWord(word1)
            # '-1:word previous neighbour dep=' + previous_neighbour.dep_,
            # '-1:word next neighbour dep=' + next_neighbour.dep_,
            # '-1:word is subject=%s' % wordIsSubjectFeature(word1),
            # '-1:word nearest opinionated word=' + nearestOpinionatedWord(review_spacy, word1)
            # '-1:word is adjective and preceded by verb=%s' % wordIsAdjectivePrecededByVerbFeature(word1, review_spacy, i-1),
            # '-1:word is noun and direct object and preceded by adjective=%s' % wordIsNounAndDirectObjAndPrecededByAdjectiveFeature(word1, review_spacy, i-1),
            # '-1:word is noun followed by verb followed by adjective=%s' %wordIsNounFollowedByVerbFollowedByAdjectiveFeature(word1,review_spacy,i-1),
            # '-1:word sentence contains opinionated words=%s' % wordSentenceContainsOpinionatedWords(review_spacy),
            # '-1:word sentence contains noun phrases=%s' % wordSentenceContainsNounPhrases(review_textblob)
        ])
    else:
        features.append('BOS')

    if i < len(review_spacy)-1:
        word1 = review_spacy[i+1]
        word_ent_label = ''
        for ent in review_spacy_ents:
            if word1 in ent:
                word_ent_label = ent.label_

        previous_neighbour = word1
        next_neighbour = word1
        if i + 1 > 0:
            previous_neighbour = review_spacy[i]
        if i + 2 < len(review_spacy):
            next_neighbour = review_spacy[i+2]
        pos = i+1
        features.extend([
            '+1:word.lower=' + word1.lower_,
            '+1:word.lemma=' + word1.lemma_,
            '+1:word is out of vocabulary=%s' % word1.is_oov,
            # '+1:word position=%s' % pos,
            # '+1:word.isstop=%s' % word1.is_stop,
            # '+1:word.count=%s' % review_textblob.word_counts[word1.orth_],
            '+1:word.istitle=%s' % word1.is_title,
            '+1:word entity label' + word_ent_label,
            '+1:word is like_num=%s' % word1.like_num,
            # '+1:word polarity:%s' % TextBlob(word1.orth_).sentiment.polarity,
            '+1:pos=' + word.pos_,
            '+1:postag=' + word1.tag_,
            '+1:depend=' + word1.dep_,
            # '+1:word parser head pos' + word1.head.pos_,
            '+1:word previous neighbour pos=' + previous_neighbour.pos_,
            '+1:word next neighbour pos=' + next_neighbour.pos_,
            # '+1:word distance to nearest opinionated word=%s' % distanceToNearestOpinionatedWord(review_spacy, word1),
            # '+1:word distance to nearest domain word = %s' % distanceToNearestDomainWord(review_spacy, word1),
            '+1:word is domain word=%s' % wordIsDomainWord(word1)
            # '+1:word previous neighbour dep=' + previous_neighbour.dep_,
            # '+1:word next neighbour dep=' + next_neighbour.dep_,
            # '+1:word is subject=%s' % wordIsSubjectFeature(word1),
            # '+1:word nearest opinionated word=' + nearestOpinionatedWord(review_spacy, word1)
            # '+1:word is adjective and preceded by verb=%s' % wordIsAdjectivePrecededByVerbFeature(word1, review_spacy, i+1),
            # '+1:word is noun and direct object and preceded by adjective=%s' % wordIsNounAndDirectObjAndPrecededByAdjectiveFeature(word1, review_spacy, i+1),
            # '+1:word is noun followed by verb followed by adjective=%s' %wordIsNounFollowedByVerbFollowedByAdjectiveFeature(word1,review_spacy,i+1),
            # '+1:word sentence contains opinionated words=%s' % wordSentenceContainsOpinionatedWords(review_spacy),
            # '+1:word sentence contains noun phrases=%s' % wordSentenceContainsNounPhrases(review_textblob)
        ])
    else:
        features.append('EOS')

    return features


def word_attribute_features(review_spacy, review_textblob, review_spacy_ents, i):
    # print(review_spacy)
    word = review_spacy[i]
    previous_neighbour = word
    next_neighbour = word
    if i > 0:
        previous_neighbour = review_spacy[i-1]
    if i + 1 < len(review_spacy):
        next_neighbour = review_spacy[i+1]
    # print(review_spacy)
    # print(word)
    # print(word.head)
    # print(dependency_labels_to_root(word))
    # print(word.head)
    # print(word.left_edge)
    # print(word.right_edge)
    word_ent_label = ''
    for ent in review_spacy_ents:
        if word in ent:
            word_ent_label = ent.label_

    pos = i
    features = [
        'bias',
        'word.lower=' + word.lower_,
        'word.lemma=' + word.lemma_,
        'word is out of vocabulary=%s' % word.is_oov,
        # 'word position=%s' % pos,
        # 'word.isstop=%s' % word.is_stop,
        # 'word.count=%s' % review_textblob.word_counts[word.orth_],
        'word.istitle=%s' % word.is_title,
        'word entity label=' + word_ent_label,
        'word is like_num=%s' % word.like_num,
        # 'word polarity:%s' % TextBlob(word.orth_).sentiment.polarity,
        'pos=' + word.pos_,
        'postag=' + word.tag_,
        'depend=' + word.dep_,
        # 'word parser head pos =' + word.head.pos_,
        'word previous neighbour pos=' + previous_neighbour.pos_,
        'word next neighbour pos=' + next_neighbour.pos_,
        'word is domain word=%s' % wordIsDomainWord(word),
        'word distance to nearest opinionated word=%s' % distanceToNearestOpinionatedWord(review_spacy, word),
        # 'word distance to nearest domain word = %s' % distanceToNearestDomainWord(review_spacy, word),
        # 'word is subject=%s' % wordIsSubjectFeature(word),
        # 'word nearest opinionated word=' + nearestOpinionatedWord(review_spacy, word)
        # 'word is adjective and preceded by verb=%s' % wordIsAdjectivePrecededByVerbFeature(word, review_spacy, i),
        # 'word is noun and direct object and preceded by adjective=%s' % wordIsNounAndDirectObjAndPrecededByAdjectiveFeature(word, review_spacy, i),
        # 'word is noun followed by verb followed by adjective=%s' %wordIsNounFollowedByVerbFollowedByAdjectiveFeature(word,review_spacy,i),
        # 'word sentence contains opinionated words=%s' % wordSentenceContainsOpinionatedWords(review_spacy),
        # 'word sentence contains noun phrases=%s' % wordSentenceContainsNounPhrases(review_textblob)
        ]

    if i > 0:
        word1 = review_spacy[i-1]
        word_ent_label = ''
        for ent in review_spacy_ents:
            if word1 in ent:
                word_ent_label = ent.label_

        previous_neighbour = word1
        next_neighbour = word1
        if i - 1 > 0:
            previous_neighbour = review_spacy[i-2]
        if i < len(review_spacy):
            next_neighbour = review_spacy[i]

        pos = i-1
        features.extend([
            '-1:word.lower=' + word1.lower_,
            '-1:word.lemma=' + word1.lemma_,
            '-1:word is out of vocabulary=%s' % word1.is_oov,
            # '-1:word position=%s' % pos,
            # '-1:word.isstop=%s' % word1.is_stop,
            # '-1:word.count=%s' % review_textblob.word_counts[word1.orth_],
            '-1:word.istitle=%s' % word1.is_title,
            '-1:word entity label' + word_ent_label,
            '-1:word is like_num=%s' % word1.like_num,
            # '-1:word polarity:%s' % TextBlob(word1.orth_).sentiment.polarity,
            '-1:pos=' + word1.pos_,
            '-1:postag=' + word1.tag_,
            '-1:depend=' + word1.dep_,
            # '-1:word parser head pos' + word1.head.pos_,
            '-1:word previous neighbour pos=' + previous_neighbour.pos_,
            '-1:word next neighbour pos=' + next_neighbour.pos_,
            '-1:word is domain word=%s' % wordIsDomainWord(word1),
            '-1:word distance to nearest opinionated word=%s' % distanceToNearestOpinionatedWord(review_spacy, word1),
            # '-1:word distance to nearest domain word = %s' % distanceToNearestDomainWord(review_spacy, word1),
            # '-1:word is subject=%s' % wordIsSubjectFeature(word1),
            # '-1:word nearest opinionated word=' + nearestOpinionatedWord(review_spacy, word1)
            # '-1:word is adjective and preceded by verb=%s' % wordIsAdjectivePrecededByVerbFeature(word1, review_spacy, i-1),
            # '-1:word is noun and direct object and preceded by adjective=%s' % wordIsNounAndDirectObjAndPrecededByAdjectiveFeature(word1, review_spacy, i-1),
            # '-1:word is noun followed by verb followed by adjective=%s' %wordIsNounFollowedByVerbFollowedByAdjectiveFeature(word1,review_spacy,i-1),
            # '-1:word sentence contains opinionated words=%s' % wordSentenceContainsOpinionatedWords(review_spacy),
            # '-1:word sentence contains noun phrases=%s' % wordSentenceContainsNounPhrases(review_textblob)
        ])
    else:
        features.append('BOS')

    if i < len(review_spacy)-1:
        word1 = review_spacy[i+1]
        word_ent_label = ''
        for ent in review_spacy_ents:
            if word1 in ent:
                word_ent_label = ent.label_

        previous_neighbour = word1
        next_neighbour = word1
        if i + 1 > 0:
            previous_neighbour = review_spacy[i]
        if i + 2 < len(review_spacy):
            next_neighbour = review_spacy[i+2]
        pos = i+1
        features.extend([
            '+1:word.lower=' + word1.lower_,
            '+1:word.lemma=' + word1.lemma_,
            '+1:word is out of vocabulary=%s' % word1.is_oov,
            # '+1:word position=%s' % pos,
            # '+1:word.isstop=%s' % word1.is_stop,
            # '+1:word.count=%s' % review_textblob.word_counts[word1.orth_],
            '+1:word.istitle=%s' % word1.is_title,
            '+1:word entity label' + word_ent_label,
            '+1:word is like_num=%s' % word1.like_num,
            # '+1:word polarity:%s' % TextBlob(word1.orth_).sentiment.polarity,
            '+1:pos=' + word1.pos_,
            '+1:postag=' + word1.tag_,
            '+1:depend=' + word1.dep_,
            # '+1:word parser head pos' + word1.head.pos_,
            '+1:word previous neighbour pos=' + previous_neighbour.pos_,
            '+1:word next neighbour pos=' + next_neighbour.pos_,
            '+1:word is domain word=%s' % wordIsDomainWord(word1),
            '+1:word distance to nearest opinionated word=%s' % distanceToNearestOpinionatedWord(review_spacy, word1),
            # '+1:word distance to nearest domain word = %s' % distanceToNearestDomainWord(review_spacy, word1),
            # '+1:word is subject=%s' % wordIsSubjectFeature(word1),
            # '+1:word nearest opinionated word=' + nearestOpinionatedWord(review_spacy, word1)
            # '+1:word is adjective and preceded by verb=%s' % wordIsAdjectivePrecededByVerbFeature(word1, review_spacy, i+1),
            # '+1:word is noun and direct object and preceded by adjective=%s' % wordIsNounAndDirectObjAndPrecededByAdjectiveFeature(word1, review_spacy, i+1),
            # '+1:word is noun followed by verb followed by adjective=%s' %wordIsNounFollowedByVerbFollowedByAdjectiveFeature(word1,review_spacy,i+1),
            # '+1:word sentence contains opinionated words=%s' % wordSentenceContainsOpinionatedWords(review_spacy),
            # '+1:word sentence contains noun phrases=%s' % wordSentenceContainsNounPhrases(review_textblob)
        ])
    else:
        features.append('EOS')

    return features


def word_polarity_features(review_spacy, review_textblob, review_spacy_ents, i):
    # print(review_spacy)
    word = review_spacy[i]
    previous_neighbour = word
    next_neighbour = word
    if i > 0:
        previous_neighbour = review_spacy[i-1]
    if i + 1 < len(review_spacy):
        next_neighbour = review_spacy[i+1]
    # print(review_spacy)
    # print(word)
    # print(word.head)
    # print(dependency_labels_to_root(word))
    # print(word.head)
    # print(word.left_edge)
    # print(word.right_edge)
    word_ent_label = ''
    for ent in review_spacy_ents:
        if word in ent:
            word_ent_label = ent.label_

    pos = i
    features = [
        'bias',
        'word.lower=' + word.lower_,
        'word.lemma=' + word.lemma_,
        'word is out of vocabulary=%s' % word.is_oov,
        # 'word position=%s' % pos,
        # 'word.isstop=%s' % word.is_stop,
        # 'word.count=%s' % review_textblob.word_counts[word.orth_],
        'word.ispunct=%s' % word.is_punct,
        'word.istitle=%s' % word.is_title,
        'word entity label=' + word_ent_label,
        'word is like_num=%s' % word.like_num,
        'word polarity:%s' % TextBlob(word.orth_).sentiment.polarity,
        'pos=' + word.pos_,
        'postag=' + word.tag_,
        'depend=' + word.dep_,
        'word is sentiment shifter=%s' % wordIsSentimentShifter(word),
        # 'word parser head pos =' + word.head.pos_,
        'word previous neighbour pos=' + previous_neighbour.pos_,
        'word next neighbour pos=' + next_neighbour.pos_,
        # 'word is subject=%s' % wordIsSubjectFeature(word),
        # 'word nearest opinionated word=' + nearestOpinionatedWord(review_spacy, word)
        # 'word is adjective and preceded by verb=%s' % wordIsAdjectivePrecededByVerbFeature(word, review_spacy, i),
        # 'word is noun and direct object and preceded by adjective=%s' % wordIsNounAndDirectObjAndPrecededByAdjectiveFeature(word, review_spacy, i),
        # 'word is noun followed by verb followed by adjective=%s' %wordIsNounFollowedByVerbFollowedByAdjectiveFeature(word,review_spacy,i),
        ]

    if i > 0:
        word1 = review_spacy[i-1]
        word_ent_label = ''
        for ent in review_spacy_ents:
            if word1 in ent:
                word_ent_label = ent.label_

        previous_neighbour = word1
        next_neighbour = word1
        if i - 1 > 0:
            previous_neighbour = review_spacy[i-2]
        if i < len(review_spacy):
            next_neighbour = review_spacy[i]

        pos = i-1
        features.extend([
            '-1:word.lower=' + word1.lower_,
            '-1:word.lemma=' + word1.lemma_,
            '-1:word is out of vocabulary=%s' % word1.is_oov,
            # '-1:word position=%s' % pos,
            # '-1:word.isstop=%s' % word1.is_stop,
            # '-1:word.count=%s' % review_textblob.word_counts[word1.orth_],
            '-1:word.ispunct=%s' % word1.is_punct,
            '-1:word.istitle=%s' % word1.is_title,
            '-1:word entity label' + word_ent_label,
            '-1:word is like_num=%s' % word1.like_num,
            '-1:word polarity:%s' % TextBlob(word1.orth_).sentiment.polarity,
            '-1:pos=' + word1.pos_,
            '-1:postag=' + word1.tag_,
            '-1:depend=' + word1.dep_,
            '-1:word is sentiment shifter=%s' % wordIsSentimentShifter(word1),
            # '-1:word parser head pos' + word1.head.pos_,
            '-1:word previous neighbour pos=' + previous_neighbour.pos_,
            '-1:word next neighbour pos=' + next_neighbour.pos_,
            # '-1:word is subject=%s' % wordIsSubjectFeature(word1),
            # '-1:word nearest opinionated word=' + nearestOpinionatedWord(review_spacy, word1)
            # '-1:word is adjective and preceded by verb=%s' % wordIsAdjectivePrecededByVerbFeature(word1, review_spacy, i-1),
            # '-1:word is noun and direct object and preceded by adjective=%s' % wordIsNounAndDirectObjAndPrecededByAdjectiveFeature(word1, review_spacy, i-1),
            # '-1:word is noun followed by verb followed by adjective=%s' %wordIsNounFollowedByVerbFollowedByAdjectiveFeature(word1,review_spacy,i-1),
        ])
    else:
        features.append('BOS')

    if i < len(review_spacy)-1:
        word1 = review_spacy[i+1]
        word_ent_label = ''
        for ent in review_spacy_ents:
            if word1 in ent:
                word_ent_label = ent.label_

        previous_neighbour = word1
        next_neighbour = word1
        if i + 1 > 0:
            previous_neighbour = review_spacy[i]
        if i + 2 < len(review_spacy):
            next_neighbour = review_spacy[i+2]
        pos = i+1
        features.extend([
            '+1:word.lower=' + word1.lower_,
            '+1:word.lemma=' + word1.lemma_,
            '+1:word is out of vocabulary=%s' % word1.is_oov,
            # '+1:word position=%s' % pos,
            # '+1:word.isstop=%s' % word1.is_stop,
            # '+1:word.count=%s' % review_textblob.word_counts[word1.orth_],
            '+1:word.ispunct=%s' % word1.is_punct,
            '+1:word.istitle=%s' % word1.is_title,
            '+1:word entity label' + word_ent_label,
            '+1:word is like_num=%s' % word1.like_num,
            '+1:word polarity:%s' % TextBlob(word1.orth_).sentiment.polarity,
            '+1:pos=' + word1.pos_,
            '+1:postag=' + word1.tag_,
            '+1:depend=' + word1.dep_,
            '+1:word is sentiment shifter=%s' % wordIsSentimentShifter(word1),
            # '+1:word parser head pos' + word1.head.pos_,
            '+1:word previous neighbour pos=' + previous_neighbour.pos_,
            '+1:word next neighbour pos=' + next_neighbour.pos_,
            # '+1:word is subject=%s' % wordIsSubjectFeature(word1),
            # '+1:word nearest opinionated word=' + nearestOpinionatedWord(review_spacy, word1)
            # '+1:word is adjective and preceded by verb=%s' % wordIsAdjectivePrecededByVerbFeature(word1, review_spacy, i+1),
            # '+1:word is noun and direct object and preceded by adjective=%s' % wordIsNounAndDirectObjAndPrecededByAdjectiveFeature(word1, review_spacy, i+1),
            # '+1:word is noun followed by verb followed by adjective=%s' %wordIsNounFollowedByVerbFollowedByAdjectiveFeature(word1,review_spacy,i+1),
        ])
    else:
        features.append('EOS')

    return features


def word_emotion_features(review_spacy, review_textblob, review_spacy_ents, i):
    # print(review_spacy)
    word = review_spacy[i]
    previous_neighbour = word
    next_neighbour = word
    if i > 0:
        previous_neighbour = review_spacy[i-1]
    if i + 1 < len(review_spacy):
        next_neighbour = review_spacy[i+1]
    # print(review_spacy)
    # print(word)
    # print(word.head)
    # print(dependency_labels_to_root(word))
    # print(word.head)
    # print(word.left_edge)
    # print(word.right_edge)
    word_ent_label = ''
    for ent in review_spacy_ents:
        if word in ent:
            word_ent_label = ent.label_

    pos = i
    features = [
        'bias',
        'word.lower=' + word.lower_,
        'word.lemma=' + word.lemma_,
        'word is out of vocabulary=%s' % word.is_oov,
        # 'word position=%s' % pos,
        # 'word.isstop=%s' % word.is_stop,
        # 'word.count=%s' % review_textblob.word_counts[word.orth_],
        'word.ispunct=%s' % word.is_punct,
        'word.istitle=%s' % word.is_title,
        'word entity label=' + word_ent_label,
        'word is like_num=%s' % word.like_num,
        'word polarity:%s' % TextBlob(word.orth_).sentiment.polarity,
        'pos=' + word.pos_,
        'postag=' + word.tag_,
        'depend=' + word.dep_,
        'word is sentiment shifter=%s' % wordIsSentimentShifter(word),
        # 'word parser head pos =' + word.head.pos_,
        'word previous neighbour pos=' + previous_neighbour.pos_,
        'word next neighbour pos=' + next_neighbour.pos_,
        # 'word is subject=%s' % wordIsSubjectFeature(word),
        # 'word nearest opinionated word=' + nearestOpinionatedWord(review_spacy, word)
        # 'word is adjective and preceded by verb=%s' % wordIsAdjectivePrecededByVerbFeature(word, review_spacy, i),
        # 'word is noun and direct object and preceded by adjective=%s' % wordIsNounAndDirectObjAndPrecededByAdjectiveFeature(word, review_spacy, i),
        # 'word is noun followed by verb followed by adjective=%s' %wordIsNounFollowedByVerbFollowedByAdjectiveFeature(word,review_spacy,i),
        ]

    if i > 0:
        word1 = review_spacy[i-1]
        word_ent_label = ''
        for ent in review_spacy_ents:
            if word1 in ent:
                word_ent_label = ent.label_

        previous_neighbour = word1
        next_neighbour = word1
        if i - 1 > 0:
            previous_neighbour = review_spacy[i-2]
        if i < len(review_spacy):
            next_neighbour = review_spacy[i]

        pos = i-1
        features.extend([
            '-1:word.lower=' + word1.lower_,
            '-1:word.lemma=' + word1.lemma_,
            '-1:word is out of vocabulary=%s' % word1.is_oov,
            # '-1:word position=%s' % pos,
            # '-1:word.isstop=%s' % word1.is_stop,
            # '-1:word.count=%s' % review_textblob.word_counts[word1.orth_],
            '-1:word.ispunct=%s' % word1.is_punct,
            '-1:word.istitle=%s' % word1.is_title,
            '-1:word entity label' + word_ent_label,
            '-1:word is like_num=%s' % word1.like_num,
            '-1:word polarity:%s' % TextBlob(word1.orth_).sentiment.polarity,
            '-1:pos=' + word1.pos_,
            '-1:postag=' + word1.tag_,
            '-1:depend=' + word1.dep_,
            '-1:word is sentiment shifter=%s' % wordIsSentimentShifter(word1),
            # '-1:word parser head pos' + word1.head.pos_,
            '-1:word previous neighbour pos=' + previous_neighbour.pos_,
            '-1:word next neighbour pos=' + next_neighbour.pos_,
            # '-1:word is subject=%s' % wordIsSubjectFeature(word1),
            # '-1:word nearest opinionated word=' + nearestOpinionatedWord(review_spacy, word1)
            # '-1:word is adjective and preceded by verb=%s' % wordIsAdjectivePrecededByVerbFeature(word1, review_spacy, i-1),
            # '-1:word is noun and direct object and preceded by adjective=%s' % wordIsNounAndDirectObjAndPrecededByAdjectiveFeature(word1, review_spacy, i-1),
            # '-1:word is noun followed by verb followed by adjective=%s' %wordIsNounFollowedByVerbFollowedByAdjectiveFeature(word1,review_spacy,i-1),
        ])
    else:
        features.append('BOS')

    if i < len(review_spacy)-1:
        word1 = review_spacy[i+1]
        word_ent_label = ''
        for ent in review_spacy_ents:
            if word1 in ent:
                word_ent_label = ent.label_

        previous_neighbour = word1
        next_neighbour = word1
        if i + 1 > 0:
            previous_neighbour = review_spacy[i]
        if i + 2 < len(review_spacy):
            next_neighbour = review_spacy[i+2]
        pos = i+1
        features.extend([
            '+1:word.lower=' + word1.lower_,
            '+1:word.lemma=' + word1.lemma_,
            '+1:word is out of vocabulary=%s' % word1.is_oov,
            # '+1:word position=%s' % pos,
            # '+1:word.isstop=%s' % word1.is_stop,
            # '+1:word.count=%s' % review_textblob.word_counts[word1.orth_],
            '+1:word.ispunct=%s' % word1.is_punct,
            '+1:word.istitle=%s' % word1.is_title,
            '+1:word entity label' + word_ent_label,
            '+1:word is like_num=%s' % word1.like_num,
            '+1:word polarity:%s' % TextBlob(word1.orth_).sentiment.polarity,
            '+1:pos=' + word1.pos_,
            '+1:postag=' + word1.tag_,
            '+1:depend=' + word1.dep_,
            '+1:word is sentiment shifter=%s' % wordIsSentimentShifter(word1),
            # '+1:word parser head pos' + word1.head.pos_,
            '+1:word previous neighbour pos=' + previous_neighbour.pos_,
            '+1:word next neighbour pos=' + next_neighbour.pos_,
            # '+1:word is subject=%s' % wordIsSubjectFeature(word1),
            # '+1:word nearest opinionated word=' + nearestOpinionatedWord(review_spacy, word1)
            # '+1:word is adjective and preceded by verb=%s' % wordIsAdjectivePrecededByVerbFeature(word1, review_spacy, i+1),
            # '+1:word is noun and direct object and preceded by adjective=%s' % wordIsNounAndDirectObjAndPrecededByAdjectiveFeature(word1, review_spacy, i+1),
            # '+1:word is noun followed by verb followed by adjective=%s' %wordIsNounFollowedByVerbFollowedByAdjectiveFeature(word1,review_spacy,i+1),
        ])
    else:
        features.append('EOS')

    return features


def review_features(reviewText, type):
    review_spacy = nlp(reviewText)
    review_textblob = TextBlob(reviewText)
    review_spacy_ents = review_spacy.ents
    # print(reviewText)
    #
    word_features_array = []
    for i in range(len(review_spacy)):
        word = review_spacy[i]
        # if not word.is_stop and not word.is_punct:
        if (word.pos == NOUN or (word.pos == VERB and TextBlob(word.orth_).sentiment.polarity > 0) or word.pos == ADJ or word.pos == ADV) and not word.is_punct:
        # if word.pos == NOUN:
            if type == labelType.Label.aspect:
                word_features_array.append(word_aspect_features(review_spacy, review_textblob, review_spacy_ents, i))
            elif type == labelType.Label.attribute:
                word_features_array.append(word_attribute_features(review_spacy, review_textblob, review_spacy_ents, i))
            elif type == labelType.Label.polarity:
                word_features_array.append(word_polarity_features(review_spacy, review_textblob, review_spacy_ents, i))
            elif type == labelType.Label.emotion:
                word_features_array.append(word_emotion_features(review_spacy, review_textblob, review_spacy_ents, i))
    return word_features_array


def review_features_romanian(reviewText, type):
    review_spacy = nlp(reviewText)
    review_textblob = TextBlob(reviewText)
    review_spacy_ents = review_spacy.ents
    word_features_array = []
    # print(review_textblob)
    if not review_textblob.detect_language() == 'en':
        review_textblob = review_textblob.translate(to='en')
        review_spacy = nlp(review_textblob.string)
    else:
        contains_romanian_words = 0

        for word in review_textblob.words:
            word_textblob = TextBlob(word)
            if len(word_textblob.string) >= 3 and word_textblob.detect_language() == 'ro':
                contains_romanian_words = 1
                break

        if contains_romanian_words == 1:
            new_reviewText = ''
            for word in review_spacy:
                word_textblob = TextBlob(word.orth_)
                if not word.is_title and len(word_textblob.string) >= 3:
                    if word_textblob.detect_language() != 'ro':
                        new_reviewText = new_reviewText + ' ' + word_textblob.string
                    else:
                        new_word = word_textblob.translate(to='en')
                        new_reviewText = new_reviewText + ' ' + new_word.string
                else :
                    new_reviewText = new_reviewText + ' ' + word_textblob.string
            review_textblob = TextBlob(new_reviewText)
            review_spacy = nlp(review_textblob.string)
            # print(review_spacy)w_spacy)
    for i in range(len(review_spacy)):
        word = review_spacy[i]
        # if not word.is_stop and not word.is_punct:
        if (word.pos == NOUN or (word.pos == VERB and TextBlob(word.orth_).sentiment.polarity > 0) or word.pos == ADJ or word.pos == ADV) and not word.is_punct:
        # if word.pos == NOUN:
            if type == labelType.Label.aspect:
                word_features_array.append(word_aspect_features(review_spacy, review_textblob, review_spacy_ents, i))
            elif type == labelType.Label.attribute:
                word_features_array.append(word_attribute_features(review_spacy, review_textblob, review_spacy_ents, i))
            elif type == labelType.Label.polarity:
                word_features_array.append(word_polarity_features(review_spacy, review_textblob, review_spacy_ents, i))
            elif type == labelType.Label.emotion:
                word_features_array.append(word_emotion_features(review_spacy, review_textblob, review_spacy_ents, i))
    return word_features_array