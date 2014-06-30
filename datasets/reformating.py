import csv
import re

sCite = '/Users/SamHill/Documents/hmt-vm/hmt-12B/datasets/scholia-citations.txt'
sPeName = '/Users/SamHill/Documents/hmt-vm/hmt-12B/datasets/scholia-persName-index.txt'
sPlName = '/Users/SamHill/Documents/hmt-vm/hmt-12B/datasets/scholia-placeNames.txt'

file = open(sCite, "rU")
reader = csv.reader(file, delimiter='\t')
for row in reader:
	print '"%s","%s"' % (row[0], row[1])
file.close()