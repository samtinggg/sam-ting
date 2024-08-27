from rdkit import Chem
from rdkit.Chem import Draw
smiles='CCCCC'
molecule=Chem.MolFromSmiles(smiles)
image=Draw.MolToImage(molecule)
image.show()

