# 'i' equals the no. of features and 'j' equals no. of rows

import string, collections, csv, os, numpy as np
from collections import *

dir_files = [b for b in os.listdir('.') if os.path.isfile(b)]

def scale(val, src, dst):  
    #Scale the given value from the scale of src to the scale of dst.
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]

for b in dir_files:
	if b.endswith('_feats.txt'):
		print b
		feats_file = open(b, 'r')
		b_name = b.split(".")[0]
		outfile = 'scaled_' + b_name + '.txt'
		f = open(outfile, 'w')
		total_rows = 0

		flist = [[] for x in range(145)]				# n nested lists, one for each feature

		for line in feats_file.readlines():
			splitline = line.rstrip().split('\t')
			#print splitline
			total_rows += 1
			for i in range(0, 145):
				print splitline[i]
				flist[i].append(float(splitline[i]))
		#print flist

		flist_scaled = [[] for x in range(145)]
		for i in range(0, 145):
			src1 = min(flist[i])
			src2 = max(flist[i])

			for j in range(0, total_rows):
				val = flist[i][j]
				val_ed = scale(val, (src1, src2), (-1.0, +1.0))
				flist_scaled[i].append(val_ed)


		for j in range(0, total_rows):
			for i in range(0, 145):
				f.write(str(float(flist_scaled[i][j])))
				if i < 144:
					f.write(' ')
			f.write('\n')

