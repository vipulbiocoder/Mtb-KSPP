import os, glob, re, shutil, fnmatch, numpy, math, collections, operator, csv
from collections import *


dir_files = [f for f in os.listdir('.') if os.path.isfile(f)]		
for f in dir_files:	
	if f.endswith("atomsAvg_ed.pdb"):
		a = open(f, "r+")

for g in dir_files:	
	if g.endswith("alnd_ed.pdb"):
		b = open(g, "r+")


for line in a.readlines():
	splitline = line.split()
	if splitline[2] == 'CB':							# Replace 'CB' with 'CA' to fetch co-ordinates of the Carbon-alpha atoms
		# Co-ordinates of the reference atom (C-alpha or C-Beta of any residue of the peptide)
		x1 = float(splitline[6])
		y1 = float(splitline[7])
		z1 = float(splitline[8])
		distobj = collections.OrderedDict()					# Dict. with ordered keys created to store distances between atoms
		peptide_res =  splitline[5]

		for line in b.readlines():
			splitline = line.split()
			print splitline[5]
			atominfo = splitline[2] + '_' + splitline[3] + '_' + splitline[5]
			x2 = float(splitline[6])							# Co-ordinates of the target atom (atom of the STPK)
			y2 = float(splitline[7])
			z2 = float(splitline[8])

			'''Distance calculation formula'''
			d = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)		 
			d = round(d, 3)
			distobj[atominfo] = d
		b.seek(0)

		sorted_distobj = sorted(distobj.items(), key=operator.itemgetter(1))
		print 'sorted_distobj:', sorted_distobj


		outfile = peptide_res + ".csv"  
 
		with open(outfile, "wb" ) as c:
			for i in range(0, len(sorted_distobj)):
			    	c.write(str(sorted_distobj[i][0]))
				c.write('\t')

			    	c.write(str(sorted_distobj[i][1]))
				c.write('\n')
				print 'len(sorted_distobj) is:', len(sorted_distobj)



a.close()
b.close()
