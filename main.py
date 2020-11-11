from util.data_extraction import build_dictionaries
from util.pd_util import build_dataframe_without_topics

wordCountForDocuments, topicsForDocuments, globalDictionary = build_dictionaries()
csv = build_dataframe_without_topics(wordCountForDocuments,globalDictionary)
1 == 1
