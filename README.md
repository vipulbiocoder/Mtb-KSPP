# Mtb-KSPP
This file details the steps to generate the phosphosite predictions using sample input data files to generate the data features and generate the predictions using the sample test data file and svm model files.

Step 1:
run the script 'feats_calc.py' on a command line using the sample files supplied in this bundle (Q15759_mapk11_CA.csv, Q15759_mapk11_CB.csv, btpp_ed.csv, charge compatibility_ed.csv, hydropathy compatibility_ed.csv, size compatibility_ed.csv, Q15759_subsinfo.csv) as inputs for the script. The output file contains the amino acid compatibility features for the peptide residues with the kinase residues

Step 2:
run the file svm-predict.py available in a LibSVM environment using the sample input files 'svm_STPKs_test.txt' and 'svm_STPKs.model' to generate the predictions on the test file and/or calculate the performance metrics for the svm model file.
