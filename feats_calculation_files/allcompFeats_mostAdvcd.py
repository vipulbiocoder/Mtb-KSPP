import string, collections, csv, os, numpy as np
from collections import *
dir_files = [a for a in os.listdir('.') if os.path.isfile(a)]
for a in dir_files:
	if a.endswith('info_new.csv') or a.endswith('info_new_ed.csv'):
		pepfile = open(a, 'r')


btpp_aalist = ("A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y")     # Amino acid (A.A. codes for dict. keys assignment
btpp_compdict = collections.OrderedDict()				# Dict. with ordered keys to store A.A. pair compatibility matrix
for j in btpp_aalist:
	btpp_compdict[j] = {}
	for k in btpp_aalist:					# Keys assigned to dict. of dicts meant for storing A.A. pair compatibility matrix
		btpp_compdict[j][k] = 0				# Dict. of dicts is initialized
with open('btpp_ed.csv', mode='r') as infile:			# Specify the type of compatibility matrix
	reader = csv.reader(infile, delimiter=' ')
	for rows in reader:
		for i in range(1, len(rows)):
			btpp_compdict[rows[0]][btpp_aalist[i-1]] = rows[i]		# Values of the dict. of dicts are updated

charge_aalist = ("D","E","C","N","F","Q","Y","S","M","T","I","G","V","W","L","A","P","H","K","R")     # Amino acid (A.A. codes for dict. keys assignment
charge_compdict = collections.OrderedDict()				# Dict. with ordered keys to store A.A. pair compatibility matrix
for j in charge_aalist:
	charge_compdict[j] = {}
	for k in charge_aalist:					# Keys assigned to dict. of dicts meant for storing A.A. pair compatibility matrix
		charge_compdict[j][k] = 0			# Dict. of dicts is initialized
with open('charge compatibility_ed.csv', mode='r') as infile:
	reader = csv.reader(infile, delimiter=' ')
	for rows in reader:
		for i in range(1, len(rows)):
			charge_compdict[rows[0]][charge_aalist[i-1]] = rows[i]		# Values of the dict. of dicts are updated


hphobe_aalist = ("R","K","D","Q","N","E","H","S","T","P","Y","C","G","A","M","W","L","V","F","I")     # Amino acid (A.A. codes for dict. keys assignment
hphobe_compdict = collections.OrderedDict()				# Dict. with ordered keys created to store A.A. pair compatibility matrix
for j in hphobe_aalist:
	hphobe_compdict[j] = {}		
	for k in hphobe_aalist:					# Keys assigned to dict. of dicts meant for storing A.A. pair compatibility matrix
		hphobe_compdict[j][k] = 0				# Dict. of dicts is initialized
with open('hydropathy compatibility_ed.csv', mode='r') as infile:
	reader = csv.reader(infile, delimiter=' ')
	for rows in reader:
		for i in range(1, len(rows)):
			hphobe_compdict[rows[0]][hphobe_aalist[i-1]] = rows[i]		# Values of the dict. of dicts are updated

size_aalist = ("G","A","S","P","V","T","C","L","I","N","D","Q","K","E","M","H","F","R","Y","W")     # Amino acid (A.A. codes for dict. keys assignment
size_compdict = collections.OrderedDict()				# Dict. with ordered keys created to store A.A. pair compatibility matrix
for j in size_aalist:
	size_compdict[j] = {}		
	for k in size_aalist:					# Keys assigned to dict. of dicts meant for storing A.A. pair compatibility matrix
		size_compdict[j][k] = 0				# Dict. of dicts is initialized
with open('size compatibility_ed.csv', mode='r') as infile:			# Specify the type of compatibility matrix
	reader = csv.reader(infile, delimiter=' ')
	for rows in reader:
		for i in range(1, len(rows)):
			size_compdict[rows[0]][size_aalist[i-1]] = rows[i]		# Values of the dict. of dicts are updated

dists_files = ['2phk_resdists_alpha.txt', '2phk_resdists_beta.txt']
kinase_name = dists_files[0].split("_")[0] + '_144feats'

ofile = kinase_name + '.csv'
f = open(ofile, 'w')
for peptide in pepfile.readlines():
	splitline = peptide.strip('\n').upper()
	splitline = splitline.split(',')
	res_list = list(splitline[3])
	aakeys = []
	pep_pp_values = []
	count = 0
	for i in range (4,11):						# Modified the indices here (difference b/w subsseqs and negseqs file format)
		aakey = res_list[i]
		count += 1
		aakey2 = aakey + '_' + str(count)
		aakeys.append(str(aakey2))				# List of peptide A.A. codes to be used for dict. keys assignment is filled
	sum_outdict = collections.OrderedDict()				# Dict. with ordered keys created to store Avg. of A.A. pair compatibility values
	for j in aakeys:
		sum_outdict[j] = 0

	for x in range (0, 2):
		kinase_dists_file = open(dists_files[x], 'r')
		cutoff = 6
		for z in range(0,1):					# to verify whether this be set to (0, 3)
			aakeyid = 0
			res_listid = 4
			for kin_dists_line in kinase_dists_file.readlines():
				dists_count = 0
				line_ed = kin_dists_line.strip('\n').split(' ')
				sum_outdict[aakeys[aakeyid]] = 0
				if len(line_ed) >= 2:
					for i in range(1, len(line_ed), 2):
						if float(line_ed[i+1]) <= float(cutoff):
							dists_count += 1
							sum_outdict[aakeys[aakeyid]] += float(btpp_compdict[res_list[res_listid]][line_ed[i]])#/float(line_ed[i+1])
							#if res_listid == 6 and cutoff == 6:

					if dists_count >= 1:
						sum_outdict[aakeys[aakeyid]] = round(sum_outdict[aakeys[aakeyid]]/float(dists_count),3)
				elif len(line_ed) < 2:
					print "No kinase residues!"
				aakeyid += 1
				res_listid += 1

			position_count = 0
			for key, value in sum_outdict.items():
				position_count += 1
				if position_count != 4:
					pep_pp_values.append(value)		
			kinase_dists_file.seek(0)
			cutoff += 1

		cutoff = 6
		for z in range(0,3):
			aakeyid = 0
			res_listid = 4
			for kin_dists_line in kinase_dists_file.readlines():
				dists_count = 0
				line_ed = kin_dists_line.strip('\n').split(' ')
				sum_outdict[aakeys[aakeyid]] = 0
				if len(line_ed) >= 2:
					for i in range(1, len(line_ed), 2):
						if float(line_ed[i+1]) <= float(cutoff):
							dists_count += 1
							sum_outdict[aakeys[aakeyid]] += float(charge_compdict[res_list[res_listid]][line_ed[i]])#/float(line_ed[i+1])
					if dists_count >= 1:
						sum_outdict[aakeys[aakeyid]] = round(sum_outdict[aakeys[aakeyid]]/float(dists_count),3)
				elif len(line_ed) < 2:
					print "No kinase residues!"
				aakeyid += 1
				res_listid += 1

			position_count = 0
			for key, value in sum_outdict.items():
				position_count += 1
				if position_count != 4:
					pep_pp_values.append(value)
			kinase_dists_file.seek(0)
			cutoff += 1

		cutoff = 6
		for z in range(0,3):
			aakeyid = 0
			res_listid = 4
			for kin_dists_line in kinase_dists_file.readlines():
				dists_count = 0
				line_ed = kin_dists_line.strip('\n').split(' ')
				sum_outdict[aakeys[aakeyid]] = 0
				if len(line_ed) >= 2:
					for i in range(1, len(line_ed), 2):
						if float(line_ed[i+1]) <= float(cutoff):
							dists_count += 1
							sum_outdict[aakeys[aakeyid]] += float(hphobe_compdict[res_list[res_listid]][line_ed[i]])#/float(line_ed[i+1])

					if dists_count >= 1:
						sum_outdict[aakeys[aakeyid]] = round(sum_outdict[aakeys[aakeyid]]/float(dists_count),3)
				elif len(line_ed) < 2:
					print "No kinase residues!"
				aakeyid += 1
				res_listid += 1

			position_count = 0
			for key, value in sum_outdict.items():
				position_count += 1
				if position_count != 4:
					pep_pp_values.append(value)		
			kinase_dists_file.seek(0)
			cutoff += 1

		cutoff = 6
		for z in range(0,3):
			aakeyid = 0
			res_listid = 4
			for kin_dists_line in kinase_dists_file.readlines():
				dists_count = 0
				line_ed = kin_dists_line.strip('\n').split(' ')
				sum_outdict[aakeys[aakeyid]] = 0
				if len(line_ed) >= 2:
					for i in range(1, len(line_ed), 2):
						if float(line_ed[i+1]) <= float(cutoff):
							dists_count += 1
							sum_outdict[aakeys[aakeyid]] += float(size_compdict[res_list[res_listid]][line_ed[i]]) #/float(line_ed[i+1])

					if dists_count >= 1:
						sum_outdict[aakeys[aakeyid]] = round(sum_outdict[aakeys[aakeyid]]/float(dists_count),3)
				elif len(line_ed) < 2:
					print "No kinase residues!"
				aakeyid += 1
				res_listid += 1

			position_count = 0
			for key, value in sum_outdict.items():
				position_count += 1
				if position_count != 4:
					pep_pp_values.append(value)		
			kinase_dists_file.seek(0)
			cutoff += 1


	for i in range(0, len(pep_pp_values)):
		f.write(str(pep_pp_values[i]))
		if i != len(pep_pp_values)-1:
			f.write(' ')
	f.write('\n')
f.close()
