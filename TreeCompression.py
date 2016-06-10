import ROOT
import array
import struct

file = ROOT.TFile('treecompression.root', 'recreate')

tree = ROOT.TTree('treeCompression', 'test compression')

boolVal = array.array('f', [0.])
branch = tree.Branch('boolBranch', boolVal, 'boolBranch/f')

randVal = array.array('f', [0.])
randB = tree.Branch('randVal', randVal, 'randVal/f')

randValLossy = array.array('f', [0.])
randBLossy = tree.Branch('randValLossy', randValLossy, 'randValLossy/f')

toint = lambda f: struct.unpack('i', struct.pack('f', f))[0]
tofloat = lambda i: struct.unpack('f', struct.pack('i', i))[0]
lossy = lambda x: tofloat(toint(x) & ~(2**10-1))

for i in range(4000000) :
    randVal[0] = ROOT.gRandom.Gaus()
    randValLossy[0] = lossy(randVal[0])
    tree.Fill()

tree.Write()

tree.Print()
