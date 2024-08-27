from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw.MolDrawing import DrawingOptions

smiles = "csnnsp"  # 苯的SMILES表示
benzene = Chem.MolFromSmiles(smiles)
# 繪製
opts = DrawingOptions()
opts.atomLabelFontSize = 200
opts.includeAtomNumbers = True
opts.dblBondLengthFrac = 0.8
opts.dotsPerAngstrom = 1000

img = Draw.MolToImage(benzene, options=opts, size=(500, 500))
img.show()

