import os, glob, re, shutil, fnmatch, numpy, math, collections, operator, csv
from collections import *

d = open("res_beta.txt", "w")
dir_files = [f for f in os.listdir('.') if os.path.isfile(f)]
resdict = collections.OrderedDict()
aakeys = ("ALA","CYS","ASP","GLU","PHE","GLY","HIS","ILE","LYS","LEU","MET","ASN","PRO","GLN","ARG","SER","THR","VAL","TRP","TYR","TPO") 
aacodes = ("A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y","T")     # amino acid codes for dict. values assignment


for j in range(0, len(aakeys)):
	resdict[aakeys[j]] = aacodes[j]		# Ordered dict. (keys:pdb amino-acid code; values:Single-letter A.A. code)


pepfiles_nums = []
for a in dir_files:
	a_num = a.split('.')[0]
	if len(a_num) == 1 or len(a_num) == 2:
		pepfiles_nums.append(int(a_num))


for i in range(min(pepfiles_nums), max(pepfiles_nums)+1):
	resdist_file = str(i) + '.csv'
	x_count = 0

	a = open(resdist_file, 'r')  
	a_handle = a.readlines()
	filenamecount = 0					# because resdist_file's (peptide res. no.) name has to be written only at start of the row

	for line in a_handle:
		splitline = line.strip('\n').split('\t')
		y = splitline[0].split("_")[2]					# Residue number of STPK in distances' file 

		if x_count == 0:
			x_count += 1
			x = splitline[0].split("_")[2]

			if filenamecount == 0:				# resdist_file's (peptide res. no.) name has to be written only once/row
				d.write(str(resdist_file))
				filenamecount += 1
				d.write('\t')

			if float(splitline[1]) <= 8:					# If Distance is <= 8 Angstroms
				d.write(str(resdict[splitline[0].split("_")[1]]))
				d.write('_')
				d.write(str(splitline[0].split("_")[2]))
				d.write('\t')
				d.write(splitline[1])
				d.write('\t')

		if y != x:
			x = splitline[0].split("_")[2]
	
			if filenamecount == 0:				# resdist_file's (peptide res. no.) name has to be written only once/row
				d.write(str(resdist_file))
				filenamecount += 1
				d.write('\t')	

			if float(splitline[1]) <= 8:
				d.write(str(resdict[splitline[0].split("_")[1]]))
				d.write('_')
				d.write(str(splitline[0].split("_")[2]))
				d.write('\t')
				d.write(splitline[1])
				d.write('\t')
	d.write('\n')
