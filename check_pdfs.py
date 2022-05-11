import os
import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

with open('bibtex_v20220116.bib') as bibtex_file:
    db = bibtexparser.load(bibtex_file)


for entry in db.entries:
    pdf = "papers/" + entry['ID'] + ".pdf"
    if not os.path.exists(pdf):
        print(entry['ID'], entry['title'])

"""
for root, dirs, files in os.walk('papers/'):
    for f in files:
        if f.endswith(".pdf"):
            fname = f.replace('-', '')
            fname = fname[:3] + '-' + fname[3:]
            print(os.path.join(root, f), os.path.join(root, fname))
            shutil.copyfile(os.path.join(root, f), os.path.join(root, fname))
"""
