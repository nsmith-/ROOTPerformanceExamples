#include "TChain.h"
#include "TDirectory.h"
#include "TH1F.h"

void cfilltest (TDirectory * dir, TChain * dychain, TChain * datachain) {
  TH1F * hmass = (TH1F *) dir->Get("hmass3");
  TH1F * hmassdata = (TH1F *) dir->Get("hmassdata3");
  TH1F * hmet = (TH1F *) dir->Get("hmet3");
  TH1F * hmetdata = (TH1F *) dir->Get("hmetdata3");

  float e1CBID_MEDIUM, e2CBID_MEDIUM, doubleEPass;
  float e1Pt, e2Pt;
  float Mass, reducedMET;

  dychain->SetBranchAddress("e1Pt", &e1Pt);
  dychain->SetBranchAddress("e2Pt", &e2Pt);
  dychain->SetBranchAddress("e1CBID_MEDIUM", &e1CBID_MEDIUM);
  dychain->SetBranchAddress("e2CBID_MEDIUM", &e2CBID_MEDIUM);
  dychain->SetBranchAddress("doubleEPass", &doubleEPass);
  dychain->SetBranchAddress("Mass", &Mass);
  dychain->SetBranchAddress("reducedMET", &reducedMET);
  dychain->SetBranchStatus("*", 0);
  dychain->SetBranchStatus("e1Pt", 1);
  dychain->SetBranchStatus("e2Pt", 1);
  dychain->SetBranchStatus("e1CBID_MEDIUM", 1);
  dychain->SetBranchStatus("e2CBID_MEDIUM", 1);
  dychain->SetBranchStatus("doubleEPass", 1);
  dychain->SetBranchStatus("Mass", 1);
  dychain->SetBranchStatus("reducedMET", 1);

  for(int i=0; i<dychain->GetEntries(); ++i) {
    dychain->GetEntry(i);
    if ( e1Pt > 20 && e2Pt > 20 && e1CBID_MEDIUM == 1. && e2CBID_MEDIUM == 1. && doubleEPass == 1. ) {
      hmass->Fill(Mass, 2.417583);
      hmet->Fill(reducedMET, 2.417583);
    }
  }

  datachain->SetBranchAddress("e1Pt", &e1Pt);
  datachain->SetBranchAddress("e2Pt", &e2Pt);
  datachain->SetBranchAddress("e1CBID_MEDIUM", &e1CBID_MEDIUM);
  datachain->SetBranchAddress("e2CBID_MEDIUM", &e2CBID_MEDIUM);
  datachain->SetBranchAddress("doubleEPass", &doubleEPass);
  datachain->SetBranchAddress("Mass", &Mass);
  datachain->SetBranchAddress("reducedMET", &reducedMET);
  datachain->SetBranchStatus("*", 0);
  datachain->SetBranchStatus("e1Pt", 1);
  datachain->SetBranchStatus("e2Pt", 1);
  datachain->SetBranchStatus("e1CBID_MEDIUM", 1);
  datachain->SetBranchStatus("e2CBID_MEDIUM", 1);
  datachain->SetBranchStatus("doubleEPass", 1);
  datachain->SetBranchStatus("Mass", 1);
  datachain->SetBranchStatus("reducedMET", 1);

  for(int i=0; i<datachain->GetEntries(); ++i) {
    datachain->GetEntry(i);
    if ( e1Pt > 20 && e2Pt > 20 && e1CBID_MEDIUM == 1. && e2CBID_MEDIUM == 1. && doubleEPass == 1. ) {
      hmass->Fill(Mass);
      hmet->Fill(reducedMET);
    }
  }
}
