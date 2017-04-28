from NCBI.pubmed import PubMed
import csv
import sys

if len(sys.argv) != 1:
    print("Usage: python CountPapers.py term-list.tsv")
    exit()

termTemplate = "(autophagy[Title/Abstract]) AND \"{}\"[Title/Abstract]"
pm = PubMed()

with open(sys.argv[1]) as fin, open(sys.argv[1]+"_count.tsv", "w") as fout:
    tsvin = csv.reader(fin, delimiter="\t")
    tsvout = csv.writer(fout, delimiter="\t")
    for row in tsvin:
        tsvout.writerow([row[0], row[1], str(pm.CountPaper(termTemplate.format(row[0])))])
        tsvout.writerow([row[0].replace("-", " "), row[1], str(pm.CountPaper(termTemplate.format(row[0].replace("-", " "))))])
