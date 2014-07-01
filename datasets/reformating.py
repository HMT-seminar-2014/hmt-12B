import csv
import re

sCite = '/Users/SamHill/Documents/hmt-vm/hmt-12B/datasets/scholia-citations.tsv'
scholName = '/Users/SamHill/Documents/hmt-vm/hmt-12B/datasets/scholia-persName-index.tsv'
scholPlace = '/Users/SamHill/Documents/hmt-vm/hmt-12B/datasets/scholia-placeNames.tsv'

names = '/Users/SamHill/Documents/hmt-vm/hmt-authlists/data/hmtnames.csv'
places = '/Users/SamHill/Documents/hmt-vm/hmt-authlists/data/hmtplaces.csv'

desc_verb = 'citedata:description'
label_verb = 'rdf:label'
contained_verb = 'cts:containedBy'
contains_verb = 'cts:contains'
belong_verb = 'cts:belongsTo'
posses_verb = 'cts:possesses'

outfile = open('all.ttl', 'wb')
outfile.write('@prefix citedata: <http://www.homermultitext.org/hmt/citedata/> .\n@prefix cts: <http://www.homermultitext.org/cts/rdf/> .\n@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n')

file = open(scholName, "rU")
reader = csv.reader(file, delimiter='\t') #, delimiter='\t' for tsvs
for row in reader:
	outfile.write('<%s> %s <%s> .\n<%s> %s <%s> .\n' % (row[0], contains_verb, row[1], row[1], contained_verb, row[0]))
file.close()

file = open(scholPlace, "rU")
reader = csv.reader(file, delimiter='\t') #, delimiter='\t' for tsvs
for row in reader:
	outfile.write('<%s> %s <%s> .\n<%s> %s <%s> .\n' % (row[0], contains_verb, row[1], row[1], contained_verb, row[0]))
file.close()

file = open(names, "rU")
reader = csv.reader(file)
for row in reader:
	outfile.write('<%s> %s "%s" .\n<%s> %s "%s" .\n<%s> %s <urn:cite:hmt:pers> .\n<urn:cite:hmt:pers> %s <%s> .\n' % (row[0], label_verb, row[1], row[0], desc_verb, row[2], row[0], belong_verb, posses_verb, row[0]))
file.close()

file = open(places, "rU")
reader = csv.reader(file)
for row in reader:
	outfile.write('<%s> %s "%s" .\n<%s> %s "%s" .\n<%s> %s <urn:cite:hmt:place> .\n<urn:cite:hmt:place> %s <%s> .\n' % (row[0], label_verb, row[1], row[0], desc_verb, row[2], row[0], belong_verb, posses_verb, row[0]))
file.close()