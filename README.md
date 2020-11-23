In the two #GeV_data_set.txt files,
1. The number in the 1st row is the total number of bins in this bin set.
2. There are 3 numbers in each row from row 2 to the last row of the file, which are the value of Q^2 (fm^{-2}) of this bin, GC from a certain model in this bin, and dGC the statistical uncertainty of GC in this bin.

data_points_Abbott.txt include the GC data from https://arxiv.org/pdf/nucl-ex/0002003.pdf
the three rows from left to right are the value of Q^2 (fm^{-2}) , GC, and the uncertainty of GC. 

Roofit.C is used for determining the value of the fixed parameters in the fitter Fixed Rational(1,3).
