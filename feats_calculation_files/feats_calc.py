import collections, csv, os
from collections import *
dir_files = [a for a in os.listdir('.') if os.path.isfile(a)]

PpChHySz_tuples = [("A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y"),("D","E","C","N","F","Q","Y","S","M","T","I","G","V","W","L","A","P","H","K","R"),("R","K","D","Q","N","E","H","S","T","P","Y","C","G","A","M","W","L","V","F","I"),
("G","A","S","P","V","T","C","L","I","N","D","Q","K","E","M","H","F","R","Y","W")]	 # Orders of A.A. codes in comp. matrices for dict. keys assignment
AAcomp_matrices = ['btpp_ed.csv', 'charge compatibility_ed.csv', 'hydropathy compatibility_ed.csv', 'size compatibility_ed.csv']

for a in dir_files:
	if a.endswith('subsinfo.csv'):
		subsfile = a
		pepfile = open(subsfile, 'r')
		print 'a', a
		dists_files = []
		for b in dir_files:
			if b.endswith('CA.csv') and str(subsfile.split("_")[0]) == str(b.split("_")[0]):
				dists_files.append(str(b))

		for c in dir_files:
			if c.endswith('CB.csv') and subsfile.split("_")[0] == c.split("_")[0]:
				dists_files.append(str(c))


		ofile = dists_files[0].split("_")[0] + '_' + dists_files[0].split("_")[1] + '_feats' + '.txt'
		f = open(ofile, 'w')

		for peptide in pepfile.readlines():
			splitline = peptide.strip('\n').upper()
			splitline = splitline.split('\t')
			res_list = list(splitline[4])						# position of input sequence in the query protein/s' file

			aakeys = []
			pep_pp_values = []
			AAcomp_dict = collections.OrderedDict()					# Dict. with ordered keys to store A.A. pair compatibility matrix
			compMat_count = 0
			for tuple in PpChHySz_tuples:
				for j in tuple:
					AAcomp_dict[j] = {}
					for k in tuple:						# Keys assigned to dict. of dicts storing A.A. pair comp. matrix
						AAcomp_dict[j][k] = 0				# Dict. of dicts is initialized
				with open(AAcomp_matrices[compMat_count], mode='r') as infile:
					reader = csv.reader(infile, delimiter=' ')
					for rows in reader:
						for i in range(1, len(rows)):
							AAcomp_dict[rows[0]][tuple[i-1]] = rows[i]	# Values of the dict. of dicts updated
				compMat_count += 1
				count = 0
				for i in range (4,11):
					aakey = res_list[i]
					count += 1
					aakey_alphaNum = aakey + '_' + str(count)
					aakeys.append(str(aakey_alphaNum))		# list of peptide A.A. codes for dict. keys assignment
				sum_outdict = collections.OrderedDict()			# dict. with ordered keys stores avg. of A.A. pair compatibility values
				for j in aakeys:
					sum_outdict[j] = 0
				for x in range (0,2):					# list of dists_files
					kinase_dists_file = open(dists_files[x], 'r')
					cutoff = 6
					for z in range(0,3):
						aakeyid = 0				# to iterate over the keys in sum_outdict (e.g. sum_outdict[aakeys[aakeyid]])
						res_listid = 4
						for kin_dists_line in kinase_dists_file.readlines():
							dists_count = 0
							line_ed = kin_dists_line.rstrip().split(' ')
							sum_outdict[aakeys[aakeyid]] = 0
							if len(line_ed) >= 2:
								for i in range(1, len(line_ed), 2):
									if float(line_ed[i+1]) <= float(cutoff):
										dists_count += 1
										sum_outdict[aakeys[aakeyid]] += float(AAcomp_dict[res_list[res_listid]][line_ed[i]])
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

