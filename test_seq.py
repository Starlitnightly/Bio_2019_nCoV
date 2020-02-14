# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 19:26:31 2020

@author: FernandoZeng
"""
import Bio_2019
import os
from Bio import AlignIO
alignment = AlignIO.read(os.getcwd()+'\\testdata\\all.fas','fasta')

test=Bio_2019.ncbi_blast(alignment[0].seq,alignment[2].seq)
print(test)