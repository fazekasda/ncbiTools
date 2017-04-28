import requests
import xml.etree.ElementTree as ET

class Entrez():

    def __init__(self, email=""):
        self.eutilsURL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
        self.esearchURL = self.eutilsURL + "esearch.fcgi"
        self.efechURL = self.eutilsURL + "efetch.fcgi"
        # TODO: all eutils url from: https://www.ncbi.nlm.nih.gov/books/NBK25497/#_chapter2_The_Nine_Eutilities_in_Brief_
        self.db = ""
        self.term = ""
        # TODO: Retrieval parameters

    def esearch(self, term="", history=False):
        # TODO: Retrieval!
        requestURL = self.esearchURL
        requestPayload = {
            "db": self.db,
            "term": term,
        }
        ncbiResponse = requests.get(requestURL, params=requestPayload, stream=True)
        ncbiResponse.raise_for_status() # TODO: make useful error!
        return ET.fromstring(ncbiResponse.text)

    def QuickSearch(self, term):
        # shortcut to simple esearch
        return self.esearch(term=term)
