from bs4 import BeautifulSoup

from constants import datasetpath


def get_parsed_xml_document(filename) -> BeautifulSoup:
    filepath = datasetpath + f'/{filename}'
    handler = open(filepath).read()
    return BeautifulSoup(handler)