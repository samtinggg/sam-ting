from rdkit import Chem
from rdkit.Chem import Draw
smiles = 'CSNNSP'
molecule = Chem.MolFromSmiles(smiles)
image = Draw.MolToImage(molecule)
image.show()