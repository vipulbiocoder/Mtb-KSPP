# Mtb-KSPP
This file details the steps to generate the phosphosite predictions using sample input data files to generate the data features and generate the predictions using the sample test data file and svm model files.

Step 1:
Run the scripts 'aacomp_feats.py' and 'aacomp_negfeats.py' on a command line using the input files supplied in this bundle as inputs for the scripts. The output file contains the amino acid compatibility features for the peptide residues with the kinase residues.

Step 2:
Run the file svm-predict.py available in a LibSVM environment using the sample input files 'svm_pknBpredinputs.txt' and 'kspp.model' to generate the predictions on the sample file of the kinase PknB.
