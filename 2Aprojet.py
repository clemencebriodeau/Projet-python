#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 16:41:45 2021

@author: natalie
"""

import numpy as np
import urllib
import bs4
import pandas as pd

from bs4 import BeautifulSoup
from urllib import request



urlpage = 'http://www.olympedia.org/editions/23'

#renvoie le html à la variable request_text
request_text = request.urlopen(urlpage).read()


#Récupération du tableau des JO de 1992 en utilisant BeautifulSoup: sert de phase d'initialisation des variables

page1 = bs4.BeautifulSoup(request_text, "lxml")
#print(page1.find("table"))

tableau_medailles = page1.find_all("table")[5]

#les balises ne suffisent pas à identifier le bon tableau
#tableau_medailles = page1.find('table',{'class':'table table-striped'})
#print(tableau_medailles)



# on recherche toutes les lignes du tableau avec la balise "tr"
rows = tableau_medailles.find_all("tr")


for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    print(cols)

dico_medailles = dict()
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    if len(cols) > 0 : 
        dico_medailles[cols[0]] = cols[1:]


data_medailles = pd.DataFrame.from_dict(dico_medailles,orient='index')


for row in rows:
    cols = row.find_all('th')
    print(cols)
    if len(cols) > 0 : 
        cols = [ele.get_text(separator=' ').strip().title() for ele in cols]
        columns_medailles = cols
        
data_medailles.columns = columns_medailles[0:]
data_medailles



#******************JO suivants*******************
#pour les premières pages, le tableau voulu est le 6e
nbre_pages=np.array([23,24,25,26,53]) 

for i in nbre_pages: 
    request_text_i = request.urlopen("http://www.olympedia.org/editions/" + str(i))
    pagei=bs4.BeautifulSoup(request_text_i,"lxml")
    tableau_medailles = pagei.find_all("table")[5]
    rows = tableau_medailles.find_all("tr")
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        #print(cols)

    dico_medailles = dict()
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if len(cols) > 0 : 
            dico_medailles[cols[0]] = cols[1:]


    data_medailles = pd.DataFrame.from_dict(dico_medailles,orient='index')
    data_medailles.columns = columns_medailles[0:]
    print(data_medailles)


    
#pour les dernières pages, le tableau voulu est le 5e

nbre_pages=np.array([54,59,61]) 

for i in nbre_pages: 
    request_text_i = request.urlopen("http://www.olympedia.org/editions/" + str(i))
    pagei=bs4.BeautifulSoup(request_text_i,"lxml")
    tableau_medailles = pagei.find_all("table")[4]
    rows = tableau_medailles.find_all("tr")
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        #print(cols)

    dico_medailles = dict()
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if len(cols) > 0 : 
            dico_medailles[cols[0]] = cols[1:]


    data_medailles = pd.DataFrame.from_dict(dico_medailles,orient='index')
    data_medailles.columns = columns_medailles[0:]
    print(data_medailles)

