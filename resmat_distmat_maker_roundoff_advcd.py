import os, glob, re, shutil, fnmatch, numpy, math, collections, operator, csv, pickle, string
from collections import * 

dir_files = [b for b in os.listdir('.') if os.path.isfile(b)]
for b in dir_files:
	if b.endswith('alnd_ed.pdb'):
		kinase = b.split("_")[0]

ofile = kinase + '_dists.txt'

d = open("res_beta.txt", "r")
f = open(ofile, "w")

for line in d:
	splitline = line.strip('\n').split('\t')
	resnum = splitline[0].split(".")[0]
	splitline = ' '.join(splitline).split()
	reslist = []
	a = collections.OrderedDict()
	for i in range(1, len(splitline), 2):
		reslist.append(splitline[i])
		if splitline[i] not in a:
   			a[splitline[i]] = splitline[i+1]

	
	res_dist = []
	for key, val in a.items():
		res_dist.append(key)
		res_dist.append(val)


	f.write(splitline[0])
	f.write(' ')

	for i in range(0, len(res_dist),2):
		rescode = res_dist[i].split("_")[0]
		print rescode

		f.write(rescode)
		f.write(' ')
		f.write(str(round(float(res_dist[i+1]),1)))			# decimal round-off
		if i < len(res_dist)-2:
			f.write(' ')
	f.write('\n')



