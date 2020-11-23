#include<iostream>
#include<fstream>
#include <iomanip>
#include <string>
#include <sstream>
using namespace std;

#include "stdlib.h"
#include "TROOT.h"
#include "TApplication.h"
#include "Rtypes.h"
#include "math.h"
#include "TMath.h"
#include "TRandom.h"
#include "TRandom3.h"
#include "TFile.h"
#include "TObject.h"
#include "TKey.h"
#include "TTree.h"

#include "TChain.h"
#include "TString.h"
#include "TCut.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TH1D.h"
#include "TH2D.h"
#include "TEventList.h"

#include "data_one.h"

#include "Math/Minimizer.h"
#include "Math/Factory.h"
#include "Math/Functor.h"
#include "TError.h"

int roofit(){
    gStyle->SetOptFit(111111);
    TF1 *f1 = new TF1 ("f1","[4]*(1+[0]*x)/(1+[1]*x+[2]*x*x+[3]*x*x*x)",0.,45);//rational_1_3
    //initial values of the parameters
    f1-> SetParameter(0,-0.047);
    f1-> SetParameter(1,0.6626);
    f1-> SetParameter(2,0.4);
    f1-> SetParameter(3,0.80);
    TGraphErrors graph("DRad_models/data_points_Abbott.txt","%lg %lg %lg");
    graph.SetMarkerStyle(kCircle);
    graph.SetFillColor(0);
    graph.Print();
    graph.DrawClone("AP");
    graph.Fit("f1","B");
    double p0 = f1->GetParameter(0);
    double p1 = f1->GetParameter(1);
    double R = 6*sqrt(p1*p1-p0*p0);
    f1->Draw("same");
    f1->GetXaxis()->SetLabelSize(0.045);
    f1->GetYaxis()->SetLabelSize(0.045);
    f1->GetXaxis()->SetTitleSize(0.055);
    f1->GetYaxis()->SetTitleSize(0.055);
    f1->GetYaxis()->SetTitle("G_{C}^{d}");
    f1->GetXaxis()->SetTitle("Q^{2} (fm^{-2})");
    cout<<f1->GetChisquare()<<","<<R<<","<<f1->GetParameter(2)<<","<<f1->GetParameter(3)<<endl;
    return 0;
}
