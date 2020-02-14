# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 18:55:52 2020

@author: FernandoZeng
"""
import requests
import urllib3
from bs4 import BeautifulSoup
import pandas as pd
import os
import os.path

urllib3.disable_warnings()


#Fasta merger
'''
parameter:
    file:The directory where sequence files are stored
'''

def merge_fas(file):
    filedir=file
    filenames=os.listdir(filedir)
    f=open(file+'\result.fasta','w')
    for filename in filenames:
        filepath=filedir+'/'+filename
        for line in open(filepath):
            f.writelines(line)
        f.write('\n')
    f.close()
    print('merge_success '+file+'\result.fasta')



#Protein structure prediction by i-tasser
'''
parameter:
    sequence:amino acid sequence
    email:your i-tasser email
    password:your i-tasser email password
    tarname:your project name
    pri:no
return:
    a:none(the result will be sent to your email)
'''
def i_tasser_post(sequence,email,password,tarname,pri="no"):
    url="https://zhanglab.ccmb.med.umich.edu/cgi-bin/itasser_submit.cgi"
    head={
          'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36"
          }
    data={
          "SEQUENCE":sequence,
          "REPLY-E-MAIL":email,
          "password":password,
          "TARGET-NAME":tarname,
          "PRI":pri,
          }
    a=requests.post(url,verify=False,headers=head,data=data)
    return(a)


#Protein structure prediction by Phyre2
'''
parameter:
    sequence:amino acid sequence
    email:your i-tasser email
    name:your project name
return:
    a:none(the result will be sent to your email)
'''
def phyre2_post(sequence,email,name):
    url="http://www.sbg.bio.ic.ac.uk/phyre2/webscripts/phyre2_submit.cgi"
    head={
          'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36"
          }
    data={
            "usr-email":email,
            "seq-desc":name,
            "sequence":sequence,
            "modelmode":"normal",
            "usertype":"NA",
            "btnS":"Phyre Search"
            }
    a=requests.post(url,verify=False,headers=head,data=data)
    return(a)


#Analyze two nucleotide sequences by blast
'''
parameter:
    se1: the first nucleotide sequence
    se2: the second nucleotide sequence
return:
    df:result(DataFrame Framework)
'''
def ncbi_blast(se1,se2):
    
    url="https://blast.ncbi.nlm.nih.gov/BlastAlign.cgi"
    head={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'                    
            }    
    data={
            'QUERY':str(se1),
'db':'nucleotide',
'QUERY_FROM':'',
'QUERY_TO':'',
'QUERYFILE':'',
'GENETIC_CODE':'1',
'JOB_TITLE':'BetaCoV/Wuhan/IVDC-HB-01/2019|EPI_ISL_402119',
'BL2SEQ':'on',
'ADV_VIEW':'on',
'SUBJECTS':str(se2),
'stype':'nucleotide',
'SUBJECTS_FROM':'',
'SUBJECTS_TO':'',
'SUBJECTFILE':'',
'DBTYPE':'gc',
'DATABASE':'',
'EQ_MENU':'',
'NUM_ORG':'1',
'EQ_TEXT':'',
'BLAST_PROGRAMS':'megaBlast',
'PHI_PATTERN':'',
'MAX_NUM_SEQ':'100',
'SHORT_QUERY_ADJUST':'on',
'EXPECT':'10',
'WORD_SIZE':'28',
'HSP_RANGE_MAX':'0',
'MATRIX_NAME':'PAM30',
'MATCH_SCORES':'1,-2',
'GAPCOSTS':'0 0',
'COMPOSITION_BASED_STATISTICS':'0',
'FILTER':'L',
'REPEATS':'repeat_9606',
'FILTER':'m',
'TEMPLATE_LENGTH':'0',
'TEMPLATE_TYPE':'0',
'PSSM':'',
'I_THRESH':'',
'DI_THRESH':'',
'PSI_PSEUDOCOUNT':'',
'SHOW_OVERVIEW':'on',
'SHOW_LINKOUT':'on',
'GET_SEQUENCE':'on',
'FORMAT_OBJECT':'Alignment',
'FORMAT_TYPE':'HTML',
'ALIGNMENT_VIEW':'Pairwise',
'MASK_CHAR':'2',
'MASK_COLOR':'1',
'DESCRIPTIONS':'100',
'ALIGNMENTS':'100',
'LINE_LENGTH':'60',
'NEW_VIEW':'',
'NCBI_GI':'',
'SHOW_CDS_FEATURE':'',
'NUM_OVERVIEW':'100',
'FORMAT_EQ_TEXT':'',
'FORMAT_ORGANISM':'',
'EXPECT_LOW':'',
'EXPECT_HIGH':'',
'PERC_IDENT_LOW':'',
'PERC_IDENT_HIGH':'',
'QUERY_INDEX':'0',
'FORMAT_NUM_ORG':'1',
'CONFIG_DESCR':'2,3,4,5,6,7,8',
'CLIENT':'web',
'SERVICE':'plain',
'CMD':'request',
'PAGE':'MegaBlast',
'PROGRAM':'blastn',
'MEGABLAST':'on',
'RUN_PSIBLAST':'',
'WWW_BLAST_TYPE':'',
'TWO_HITS':'',
'DEFAULT_PROG':'megaBlast',
'DB_DISPLAY_NAME':'',
'ORG_DBS':'',
'SHOW_ORGANISMS':'',
'DBTAXID':'',
'SAVED_PSSM':'',
'SELECTED_PROG_TYPE':'megaBlast',
'SAVED_SEARCH':'',
'BLAST_SPEC':'blast2seq',
'MIXED_DATABASE':'',
'QUERY_BELIEVE_DEFLINE':'',
'DB_DIR_PREFIX':'',
'BLAST_INIT':'',
'USER_DATABASE':'',
'USER_WORD_SIZE':'',
'USER_MATCH_SCORES':'',
'USER_FORMAT_DEFAULTS':'',
'NO_COMMON':'',
'NUM_DIFFS':'0',
'NUM_OPTS_DIFFS':'0',
'UNIQ_DEFAULTS_NAME':'',
'PAGE_TYPE':'BlastSearch',
'USER_DEFAULT_PROG_TYPE':'megaBlast',
'USER_DEFAULT_MATCH_SCORES':'0',

            }
    d=requests.post(url,verify=False,headers=head,data=data)
    
    b=BeautifulSoup(d.text, features="lxml")
    
    c=b.find_all('input')
    data1={}
    for i in c:
        data1[i.attrs['name']]=i.attrs['value']
        
    
    url="https://blast.ncbi.nlm.nih.gov/Blast.cgi"
    head={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'                    
            }
    a=requests.post(url,verify=False,headers=head,data=data1)   
    b=BeautifulSoup(a.text, features="lxml")
    c=b.find('tbody').find_all('td')
    df=pd.DataFrame(columns=['Select','Description','Max_Score','Total_Score','Query_Cover','E_value','Per,Ident','Accession'])
    df=df.append([{
            'Select':c[0].find_all('span')[1].string,
            'Description':c[1].find('a').string,
            'Max_Score':c[2].string,
            'Total_Score':c[3].string,
            'Query_Cover':c[4].string,
            'E_value':c[5].string,
            'Per,Ident':c[6].string,
            'Accession':c[7].string.replace('\n','')
            }],ignore_index=True)
    return(df)