from os import listdir, getcwd
from os.path import isfile, join
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import stop_words


datasetpath = f'./datasets/Reuters_34/Training'

wordCountForDocuments = {}
topicsForDocuments = {}
globalDictionary = {}


def get_parsed_xml_document(filename) -> BeautifulSoup:
    filepath = datasetpath + f'/{f}'
    handler = open(filepath).read()
    return BeautifulSoup(handler)


def extract_words_from_title(document: BeautifulSoup) -> [str]:
    text_from_title = get_document_title(document)
    vectorizer = CountVectorizer(stop_words=stop_words.ENGLISH_STOP_WORDS)
    vectorizer.fit_transform([text_from_title])
    return vectorizer.get_feature_names()


def get_words_from_string(text_from_title) -> [str]:
    return text_from_title.lower().split()


def get_document_title(document):
    text_from_title: str = document.title.text
    return text_from_title


def extract_words_from_text(document: BeautifulSoup) -> [str]:
    text = get_document_text(document)
    vectorizer = CountVectorizer(stop_words=stop_words.ENGLISH_STOP_WORDS)
    ceva = vectorizer.fit_transform([text])
    # TODO : https://towardsdatascience.com/3-basic-approaches-in-bag-of-words-which-are-better-than-word-embeddings-c2cbc7398016
    return vectorizer.get_feature_names()


def get_document_text(document):
    return document.findAll('text')[0].text


def count_word_in_title_for_document(word: str, document: BeautifulSoup) -> int:
    title = get_document_title(document)
    words_from_string = get_words_from_string(title)
    return words_from_string.count(word)


def count_word_in_text_for_document(word: str, document: BeautifulSoup) -> int:
    title = get_document_text(document)
    words_from_string = get_words_from_string(title)
    return words_from_string.count(word)


def get_topics_of_document(document) -> [str]:
    codes = document.find("codes", {"class": "bip:topics:1.0"}).findAll("code")
    topics = []
    for code in codes:
        topics.append(code.attrs["code"])
    return topics


# def generate_global_dictionary():
#     for key in wordCountForDocuments:


for f in listdir(datasetpath):
    document = get_parsed_xml_document(f)

    if not wordCountForDocuments.__contains__(f):
        wordCountForDocuments[f] = {}

    topicsForDocuments[f] = get_topics_of_document(document)

    words_from_text = extract_words_from_text(document)
    words_from_title = extract_words_from_title(document)
    words = list(set(words_from_title + words_from_text))
    for word in words:
        number_of_apparitions_in_title = count_word_in_title_for_document(word, document)
        number_of_apparitions_in_text = count_word_in_text_for_document(word, document)
        number_of_apparitions = number_of_apparitions_in_title + number_of_apparitions_in_text
        wordCountForDocuments[f][word] = number_of_apparitions
        if globalDictionary.keys().__contains__(word):
            globalDictionary[word] += number_of_apparitions
        else:
            globalDictionary[word] = 0
    1 == 1
1 == 1
