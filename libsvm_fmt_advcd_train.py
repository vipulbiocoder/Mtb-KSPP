import string, collections, csv, numpy as np
from collections import *

fname = "scaled_features_trainpart.txt"
myFile = open(fname, 'r')

fname1 = "svm_features_trainpart.txt"
myFile1 = open(fname1, 'w')


linecount = 0
for line in myFile.readlines():
	splitline = line.strip('\n').split(" ")
	
	linecount += 1
	if linecount <= 2064:					 
		myFile1.write(str(int(1)))
		myFile1.write(' ')
	elif linecount >= 2065 and linecount <= 4128:
		myFile1.write(str(int(0)))
		myFile1.write(' ')

	elif linecount >= 4129 and linecount <= 4276:						 
		myFile1.write(str(int(1)))
		myFile1.write(' ')
	elif linecount >= 4277 and linecount <= 4424:
		myFile1.write(str(int(0)))
		myFile1.write(' ')


		
	for i in range(0, len(splitline)):
		myFile1.write(str(int(i+1))  + (':'))
		myFile1.write(str(float(splitline[i])))
		if i < len(splitline)-1:
			myFile1.write(' ')


	myFile1.write('\n')


myFile.close()
myFile1.close()

