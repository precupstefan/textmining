import re
from os import listdir

from bs4 import BeautifulSoup
from nltk import PorterStemmer
from sklearn.feature_extraction import stop_words
from sklearn.feature_extraction.text import CountVectorizer

from constants import datasetpath
from util.xml_parser import get_parsed_xml_document

porter_stemmer = PorterStemmer()


def my_cool_preprocessor(text):
    text = text.lower()
    text = re.sub("\\W", " ", text)  # remove special chars
    text = re.sub("\\s+(in|the|all|for|and|on)\\s+", " _connector_ ", text)  # normalize certain words

    # stem words
    words = re.split("\\s+", text)
    stemmed_words = [porter_stemmer.stem(word=word) for word in words]
    return ' '.join(stemmed_words)


def extract_words_and_occurrences_from_title(document: BeautifulSoup) -> [str]:
    text_from_title = get_document_title(document)
    return get_words_and_counts_as_list_tuple(text_from_title)


def get_words_and_counts_as_list_tuple(text_from_title):
    vectorizer = CountVectorizer(stop_words=stop_words.ENGLISH_STOP_WORDS, preprocessor=my_cool_preprocessor)
    count_occurs = vectorizer.fit_transform([text_from_title])
    return [(count, word) for word, count in zip(count_occurs.toarray().tolist()[0], vectorizer.get_feature_names())]


def get_document_title(document):
    text_from_title: str = document.title.text
    return text_from_title


def extract_words_and_occurrences_from_text(document: BeautifulSoup) -> [str]:
    text = get_document_text(document)
    return get_words_and_counts_as_list_tuple(text)


def get_document_text(document):
    return document.findAll('text')[0].text


def get_topics_of_document(document) -> [str]:
    codes = document.find("codes", {"class": "bip:topics:1.0"}).findAll("code")
    topics = []
    for code in codes:
        topics.append(code.attrs["code"])
    return topics


def extract_words_from_document(document) -> ([str], [str]):
    words_from_text = extract_words_and_occurrences_from_text(document)
    words_from_title = extract_words_and_occurrences_from_title(document)
    return words_from_text, words_from_title


def build_dictionaries():
    wordCountForDocuments = {}
    topicsForDocuments = {}
    globalDictionary = {}

    for f in listdir(datasetpath):
        document = get_parsed_xml_document(f)

        if not wordCountForDocuments.__contains__(f):
            wordCountForDocuments[f] = {}

        dict = wordCountForDocuments[f]

        topicsForDocuments[f] = get_topics_of_document(document)
        words_from_text, words_from_title = extract_words_from_document(document)

        for word, count in words_from_text:
            if globalDictionary.__contains__(word):
                globalDictionary[word] += count
            else:
                globalDictionary[word] = count
            dict[word] = count

        for word, count in words_from_title:
            if globalDictionary.__contains__(word):
                globalDictionary[word] += count
            else:
                globalDictionary[word] = count
            if dict.__contains__(word):
                dict[word] += count
            else:
                dict[word] = count
    return wordCountForDocuments, topicsForDocuments, globalDictionary
