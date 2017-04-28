from .entrez import Entrez


class PubMed(Entrez):

    def __init__(self, **kwargs):
        super(PubMed, self).__init__(**kwargs)
        self.db = "pubmed"

    def CountPaper(self, term):
        # cont papers mach with the term
        PMtree = super(PubMed, self).QuickSearch(term)
        return int(PMtree.find("Count").text)
