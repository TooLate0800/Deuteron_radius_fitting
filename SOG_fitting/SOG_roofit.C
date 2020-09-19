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
#include "TFormula.h"

//define global variables
//double G_0 = 1.0;//G_C(0)
//double G_0 = 1.714;//G_M(0)
double G_0 = 25.83;//G_Q(0)
double gamma = 0.8/TMath::Sqrt(3./2.);
double gamma2 = gamma*gamma;
double R_G = 0.4;//fm
double R[11]; 
double chi2_min = 100.0;
//double R[11] = {7.00828,3.16036,0.533948,3.72463,1.95537,3.34131,2.33181,2.08879,3.6881,0.0441331,3.31351};//GM
//double R[11] = {9.51058, 2.77812, 1.36345, 3.73107, 3.41977, 2.2224, 3.59642, 2.27404, 2.24954, 3.98724, 0.57017};
//double R[11] = {0.287782, 20.0013 ,0.402823, 9.02617, -21.2716, 119.419, -0.727167, 19.4608, -136.841, -8.77777, -1.04855};
//double R[11] = {6.66671, 2.91819, 1.25344, 2.52922, 2.73209, 3.83977, 0.449333, 3.96467, 3.86207, 3.19964, 2.13889};

//define the function
double SOG_fun(double *x, double *par)
{
    double sum = 0.0;
    double sumA = 0.0;
    for (int k = 0; k<11; k++){
        sumA = sumA + par[k];
    }
    double A_G = 1 - sumA;
    for (int k = 0; k<11; k++){
        sum = sum + par[k]/(1+2*R[k]*R[k]/gamma2)*(cos(x[0]*R[k])+(2*R[k]*R[k]/gamma2)*sin(x[0]*R[k])/(x[0]*R[k]));
    }
    sum = sum + A_G/(1+2*R_G*R_G/gamma2)*(cos(x[0]*R_G)+(2*R_G*R_G/gamma2)*sin(x[0]*R_G)/(x[0]*R_G));
    double f = G_0*TMath::Exp(-x[0]*x[0]*gamma2/4)*sum;
    return f;
}


int SOG_roofit(){
    gStyle->SetOptFit(111111);
    //auto c=new TCanvas();
    //c->SetLogy();
    for (int i=0; i <10000; i++){
        R[0] = gRandom->Uniform(4.0, 10.0);
        for (int j=1; j<11; j++){
            R[j] = gRandom->Uniform(0.0,4.0);
        }
 
        TF1 *f1 = new TF1 ("f1",SOG_fun, 0.,7.,11);//xmin,xmax,npar
        TGraphErrors graph("data/GQ_Data_fm.txt","%lg %lg %lg");
        graph.Fit("f1","B");

        //graph.SetMarkerStyle(kCircle);
        //graph.SetFillColor(0);
        //graph.DrawClone("AP");

        ////f1->Draw("");
        //f1->Draw("same");
        //f1->GetXaxis()->SetLabelSize(0.045);
        //f1->GetYaxis()->SetLabelSize(0.045);
        //f1->GetXaxis()->SetTitleSize(0.055);
        //f1->GetYaxis()->SetTitleSize(0.055);
        //f1->GetYaxis()->SetTitle("G_{M}^{d}");
        //f1->GetXaxis()->SetTitle("Q (fm^{-1})");


        double chi2 = f1->GetChisquare();
        double para[12];
        for (int n=0; n<11;n++){
            para[n] = f1->GetParameter(n);
        }
        double sumAA=0.0;
        for (int k = 0; k<11; k++){
            sumAA = sumAA + para[k];
        }
        double AG = 1 - sumAA;
        if (chi2_min>chi2){    
            chi2_min = chi2;
            cout<<chi2_min<<endl; 
            ofstream outFile1;
            outFile1.open("SOG_GQ_fit.txt", std::ios_base::app);
            outFile1<<chi2<<",";
            for (int m = 0; m<11; m++){
                outFile1<<para[m]<<", ";
            }
            for (int m = 0; m<11; m++){
                outFile1<<R[m]<<", ";
            }
            outFile1<<AG<<"\n";
            outFile1.close();
        }
 
    }
    return 0;

}
