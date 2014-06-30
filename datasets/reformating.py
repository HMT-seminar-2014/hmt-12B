import csv
import re

sCite = '/Users/SamHill/Documents/hmt-vm/hmt-12B/datasets/scholia-citations.tsv'
sPeName = '/Users/SamHill/Documents/hmt-vm/hmt-12B/datasets/scholia-persName-index.tsv'
sPlName = '/Users/SamHill/Documents/hmt-vm/hmt-12B/datasets/scholia-placeNames.tsv'

file = open(sCite, "rU")
reader = csv.reader(file) #, delimiter='\t'
for row in reader:
	print '%s\t%s' % (row[0], row[1])
file.close()