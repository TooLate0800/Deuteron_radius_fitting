In the two #GeV_data_set.txt files,
1. The number in the 1st row is the total number of bins in this bin set.
2. There are 3 numbers in each row from row 2 to the last row of the file, which are the value of Q^2 (fm^{-2}) of this bin, GC from a certain model in this bin, and dGC the statistical uncertainty of GC in this bin.

data_points_Abbott.txt include the GC data from https://arxiv.org/pdf/nucl-ex/0002003.pdf
the three rows from left to right are the value of Q^2 (fm^{-2}) , GC, and the uncertainty of GC. 

Roofit.C is used for determining the value of the fixed parameters in the fitter Fixed Rational(1,3). The following is the fitting result:
Processing roofit.C...
x[0]=0.7396, y[0]=0.627, ex[0]=0, ey[0]=0.011//
x[1]=1.3225, y[1]=0.474, ex[1]=0, ey[1]=0.008//
x[2]=2.4964, y[2]=0.289, ex[2]=0, ey[2]=0.006//
x[3]=3.0276, y[3]=0.238, ex[3]=0, ey[3]=0.005//
x[4]=4.10468, y[4]=0.16, ex[4]=0, ey[4]=0.005
x[5]=4.1209, y[5]=0.163, ex[5]=0, ey[5]=0.005
x[6]=5.5319, y[6]=0.1, ex[6]=0, ey[6]=0.004
x[7]=6.2001, y[7]=0.087, ex[7]=0, ey[7]=0.004
x[8]=7.77294, y[8]=0.0371, ex[8]=0, ey[8]=0.0147
x[9]=8.5849, y[9]=0.0345, ex[9]=0, ey[9]=0.0122
x[10]=12.7164, y[10]=0.0153, ex[10]=0, ey[10]=0.0138
x[11]=14.2884, y[11]=0.0125, ex[11]=0, ey[11]=0.0055
x[12]=16.7281, y[12]=-0.00114, ex[12]=0, ey[12]=0.0016
x[13]=17.8084, y[13]=0.00163, ex[13]=0, ey[13]=0.00161
x[14]=19.8916, y[14]=-0.00239, ex[14]=0, ey[14]=0.00061
x[15]=21.3444, y[15]=-0.00163, ex[15]=0, ey[15]=0.00114
x[16]=25.9081, y[16]=-0.00387, ex[16]=0, ey[16]=0.0003
x[17]=29.9209, y[17]=-0.00348, ex[17]=0, ey[17]=0.00032
x[18]=37.8225, y[18]=-0.00319, ex[18]=0, ey[18]=0.00055
x[19]=37.8225, y[19]=-0.0042, ex[19]=0, ey[19]=0.00042
x[20]=44.0896, y[20]=-0.00189, ex[20]=0, ey[20]=0.00038
x[21]=44.0896, y[21]=-0.00313, ex[21]=0, ey[21]=0.00024
 FCN=22.5161 FROM MIGRAD    STATUS=CONVERGED     793 CALLS         794 TOTAL
                     EDM=5.68027e-07    STRATEGY= 1      ERROR MATRIX ACCURATE 
  EXT PARAMETER                                   STEP         FIRST   
  NO.   NAME      VALUE            ERROR          SIZE      DERIVATIVE 
   1  p0          -5.74179e-02   1.45246e-03   1.90999e-06  -4.72556e-01
   2  p1           6.17919e-01   1.05530e-01   2.56044e-05   8.71589e-02
   3  p2           4.16129e-02   1.51906e-02   7.52897e-06   1.99639e-01
   4  p3           4.73677e-03   8.91641e-04   5.93486e-07  -2.66104e-01
   5  p4           9.72029e-01   5.81757e-02   1.86931e-05  -1.16642e-01
   
