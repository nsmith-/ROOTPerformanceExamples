import ROOT
import array

file = ROOT.TFile('treecompression.root', 'recreate')

tree = ROOT.TTree('treeCompression', 'test compression')

boolVal = array.array('f', [0.])
branch = tree.Branch('boolBranch', boolVal, 'boolBranch/f')

for i in range(1000000) :
    tree.Fill()

tree.Write()

tree.Print()

file.Close()
