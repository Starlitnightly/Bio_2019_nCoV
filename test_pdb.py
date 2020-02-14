# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 19:19:14 2020

@author: FernandoZeng
"""

import Bio_2019

protein="MYSFVSEETGTLIVNSVLLFLAFVVFLLVTLAILTALRLCAYCCNIVNVSLVKPSFYVYSRVKNLNSSRVPDLLV"
email=""#i-tasser_name
password=""#i-tasser_password
name="2019_nCoV_E"

#Prediction Pdb by Phyre2
Bio_2019.phyre2_post(protein,email,name)
#Prediction PDB by i-tasser
Bio_2019.i_tasser_post(protein,email,password,name)