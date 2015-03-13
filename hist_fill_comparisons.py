#!/usr/bin/env python
import time
import ROOT
ROOT.gROOT.SetBatch(True)

DYJetsChain = ROOT.TChain("ee/final/Ntuple")
DYJetsChain.Add("root://cmsxrootd.hep.wisc.edu//store/user/nsmith/ZHinvNtuples/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/make_ntuples_cfg-patTuple_cfg-00037C53-AAD1-E111-B1BE-003048D45F38.root")
DYJetsChain.Add("root://cmsxrootd.hep.wisc.edu//store/user/nsmith/ZHinvNtuples/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/make_ntuples_cfg-patTuple_cfg-00A0DE54-0BD4-E111-AB0D-003048D45F62.root")
DYJetsChain.Add("root://cmsxrootd.hep.wisc.edu//store/user/nsmith/ZHinvNtuples/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/make_ntuples_cfg-patTuple_cfg-00BFFB9C-72D4-E111-8885-002481E14E14.root")
DYJetsChain.Add("root://cmsxrootd.hep.wisc.edu//store/user/nsmith/ZHinvNtuples/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/make_ntuples_cfg-patTuple_cfg-00FB6563-58D2-E111-AFCB-001E67397D73.root")
DYJetsChain.Add("root://cmsxrootd.hep.wisc.edu//store/user/nsmith/ZHinvNtuples/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/make_ntuples_cfg-patTuple_cfg-02171BD7-A1D3-E111-A0CE-001E673967C5.root")
DataChain = ROOT.TChain("ee/final/Ntuple")
DataChain.Add("root://cmsxrootd.hep.wisc.edu//store/user/nsmith/ZHinvNtuples/data_DoubleElectron_Run2012A_22Jan2013_v1/make_ntuples_cfg-patTuple_cfg-003EC246-5E67-E211-B103-00259059642E.root")
DataChain.Add("root://cmsxrootd.hep.wisc.edu//store/user/nsmith/ZHinvNtuples/data_DoubleElectron_Run2012A_22Jan2013_v1/make_ntuples_cfg-patTuple_cfg-00AC7ED8-4C67-E211-A5F9-0025905964C0.root")
DataChain.Add("root://cmsxrootd.hep.wisc.edu//store/user/nsmith/ZHinvNtuples/data_DoubleElectron_Run2012A_22Jan2013_v1/make_ntuples_cfg-patTuple_cfg-02A18685-5567-E211-9D79-00248C0BE01E.root")
DataChain.Add("root://cmsxrootd.hep.wisc.edu//store/user/nsmith/ZHinvNtuples/data_DoubleElectron_Run2012A_22Jan2013_v1/make_ntuples_cfg-patTuple_cfg-02CE0229-A467-E211-ABD1-00248C55CC40.root")
DataChain.Add("root://cmsxrootd.hep.wisc.edu//store/user/nsmith/ZHinvNtuples/data_DoubleElectron_Run2012A_22Jan2013_v1/make_ntuples_cfg-patTuple_cfg-062A0C12-6167-E211-8114-002354EF3BE1.root")

def drawSeq() :
    c = ROOT.TCanvas()
    eID = [
        "Pt > 20",
        "CBID_MEDIUM==1",
        ]
    cuts = [leg+cut for leg in ("e1","e2") for cut in eID]
    cuts.append('doubleEPass')
    DYJetsChain.SetWeight(2.417583, "global")
    DYJetsChain.Draw("Mass>>hmass(100,40,250)", "&&".join(cuts), "hist")
    DataChain.Draw("Mass>>hmassdata(100,40,250)", "&&".join(cuts), "ex0 same")
    c.Print('test1.png')
    DYJetsChain.Draw("reducedMET>>hmet(100,0,500)", "&&".join(cuts), "hist")
    DataChain.Draw("reducedMET>>hmetdata(100,0,500)", "&&".join(cuts), "ex0 same")
    c.Print('test2.png')

def drawLoop() :
    c = ROOT.TCanvas()
    hmass = ROOT.TH1F('hmass2', '', 100, 40, 250)
    hmassdata = ROOT.TH1F('hmassdata2', '', 100, 40, 250)
    hmet = ROOT.TH1F('hmet2', '', 100, 0, 500)
    hmetdata = ROOT.TH1F('hmetdata2', '', 100, 0, 500)

    branches = ['e1Pt', 'e2Pt', 'e1CBID_MEDIUM', 'e2CBID_MEDIUM', 'doubleEPass', 'Mass', 'reducedMET']
    DYJetsChain.SetBranchStatus('*', 0)
    DataChain.SetBranchStatus('*', 0)
    for b in branches :
        DYJetsChain.SetBranchStatus(b, 1)
        DataChain.SetBranchStatus(b, 1)

    for i in range(DYJetsChain.GetEntries()) :
        DYJetsChain.GetEntry(i)
        if DYJetsChain.e1Pt > 20 and DYJetsChain.e2Pt > 20 and DYJetsChain.e1CBID_MEDIUM and DYJetsChain.e2CBID_MEDIUM and DYJetsChain.doubleEPass :
            hmass.Fill(DYJetsChain.Mass, 2.417583)
            hmet.Fill(DYJetsChain.reducedMET, 2.417583)
    for i in range(DataChain.GetEntries()) :
        DataChain.GetEntry(i)
        if DataChain.e1Pt > 20 and DataChain.e2Pt > 20 and DataChain.e1CBID_MEDIUM and DataChain.e2CBID_MEDIUM and DataChain.doubleEPass :
            hmassdata.Fill(DataChain.Mass)
            hmetdata.Fill(DataChain.reducedMET)
    hmass.Draw("hist")
    hmassdata.Draw("ex0 same")
    c.Print('test3.png')
    hmet.Draw("hist")
    hmetdata.Draw("ex0 same")
    c.Print('test4.png')

def drawCLoop() :
    c = ROOT.TCanvas()
    hdir = ROOT.TDirectory("hdir", "hdir")
    hdir.cd()
    hmass = ROOT.TH1F('hmass3', '', 100, 40, 250)
    hmassdata = ROOT.TH1F('hmassdata3', '', 100, 40, 250)
    hmet = ROOT.TH1F('hmet3', '', 100, 0, 500)
    hmetdata = ROOT.TH1F('hmetdata3', '', 100, 0, 500)
    ROOT.gROOT.ProcessLine(".L cfilltest.C+")
    ROOT.cfilltest(hdir, DYJetsChain, DataChain)
    hmass.Draw("hist")
    hmassdata.Draw("ex0 same")
    c.Print('test5.png')
    hmet.Draw("hist")
    hmetdata.Draw("ex0 same")
    c.Print('test6.png')

if __name__ == "__main__" :
    start = time.time()
    drawSeq()
    elapsed = time.time()-start
    print "drawSeq elapsed time: %f" % elapsed

    start = time.time()
    drawLoop()
    elapsed = time.time()-start
    print "drawLoop elapsed time: %f" % elapsed

    start = time.time()
    drawCLoop()
    elapsed = time.time()-start
    print "drawCLoop elapsed time: %f" % elapsed
