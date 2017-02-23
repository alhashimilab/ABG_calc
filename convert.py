#!/usr/bin/python

from pdblib.base import *

mol = Mol('target.pdb')

reses = getreses(mol)
for res in reses:
   if res.name == 'ADE' or res.name == 'RA' or res.name == 'DA':
        res.name = 'A'
   elif res.name == 'THY' or res.name == 'URA' or res.name == 'DT':
        res.name = 'U'
   elif res.name == 'CYT' or res.name == 'RC' or res.name == 'DC':
        res.name = 'C'
   elif res.name == 'GUA' or res.name == 'RG' or res.name == 'DG':
        res.name = 'G'

mol.segs[0].chid = 'A'
mol.write('target.pdb')
