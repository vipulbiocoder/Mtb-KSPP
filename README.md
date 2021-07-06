# Mtb-KSPP
This file details the steps to generate the phosphosite predictions using sample input data files to generate the data features and generate the predictions using the sample test data file and svm model files. Uncompress all the folders to get the files used in the following steps.

Step 1:
Run the python scripts 'aacomp_feats.py' and 'aacomp_negfeats.py' on a command line using the input files supplied in this bundle as inputs for the scripts. The output file contains the amino acid compatibility features for the peptide residues with the kinase residues. This results in 144 feature values for each heptapeptide sequence (positive or negative instance).
Step 2: Append the individual STPK features files for each STPK of eukaryotic STPKs data and Mycobacterium tuberculosis (Mtb) STPKs data by running the python scripts 'appendrows_eukSTPKs_feats.py' and 'appendrows_MtbSTPKs_feats.py'.

Step 3: Add the Intrinsic disorder (IDR) feature values of all STPKs as the 145th feature (145th column) to the output of the above file. The IDR values for each STPK substrate protein were derived using the IUPRED 1.0 tool. Further, the derivation the average IDR value was done on these files of each substrate protein sequence using the script 'avgIDR_heptapep.py'. Using the output files of the script 'avgIDR_heptapep.py', the average IDR values were retrieved for the phosphosite residues and the negative data Serine/Threonine of each STPK and compiled into a positive instances IDR files and negative instances IDR files. The positive IDR files of all STPKs were combined in the order as used for combining/appending the amino acid residues compatibility features (according to the order in 'appendrows_eukSTPKs_feats.py' and 'appendrows_MtbSTPKs_feats.py').


Step4: Scale the file using the script 'scale_features.py' and convert its output in the LibSVM format using the scripts 'libsvm_fmt_advcd_train.py' and 'libsvm_fmt_advcd_test.py'. Please note that one-thirds of the training data instances of each Mtb STPK were held-out from each STPK's file (total of 73/221 positive data instances/rows and 73/221 of the negative data instances/rows total 146 instances) for making the test data file of Mtb instances.

Step 4:
Run the file svm-predict.py available in a LibSVM environment using the sample input files 'svm_pknBpredinputs.txt' and 'kspp.model' to generate the predictions on the sample file of the kinase PknB.
