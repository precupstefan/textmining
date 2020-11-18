import numpy
import pandas

from util.data_extraction import build_dictionaries
from util.pca import build_pca_dataset
from util.pd_util import build_dataframe_without_topics, add_topics_to_dataset


def build_datasets():
    wordCountForDocuments, topicsForDocuments, globalDictionary = build_dictionaries()
    dataset_without_topics = build_dataframe_without_topics(wordCountForDocuments, globalDictionary)
    pca_dataset_without_topics = build_pca_dataset(dataset_without_topics)
    pca_dataset_with_topics = add_topics_to_dataset(pca_dataset_without_topics, topicsForDocuments)
    pca_dataset_with_topics.to_csv("pca_dataset.csv", index=False)
    attributes = [x for x in globalDictionary.keys()]
    with open("attributes.np", "wb") as f:
        numpy.save(f, numpy.array(attributes))


def load_datasets() -> (numpy.ndarray, pandas.DataFrame):
    with open("attributes.np", "rb") as f:
        attributes = numpy.load(f)
    csv = pandas.read_csv("pca_dataset.csv")
    return attributes, csv
