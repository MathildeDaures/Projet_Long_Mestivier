#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import re
from visual import *

# Récuperation des données de parsing du fichier gml
filin = open("parsedata.dat")
res = pickle.load(filin)
filin.close() 

# Découpage du fichier
creator = res[0][1]
version = res[1][1]

node = []
edge = []
other = []
for li in res:
    if li[0] == "node":
        node.append(li)
    elif li[0] == "edge":
        edge.append(li)
    else:
        other.append(li)         


# Traitement des nodes
rule_regex = re.compile("^R+[0-9]")
rules = []
species = []
for li in node:
    if rule_regex.search(li[1][1][1]):
        rules.append(li)
    else:
        species.append(li)     
    
#print rules[0]
#print rules[0][1][2][1][0][1]

# Affichage des nodes 
for li in rules:
    rule = box(pos=(li[1][2][1][0][1],li[1][2][1][1][1]), length=30, height=30, width=30, color=color.blue)
   
for li in species:
    rule = sphere(pos=(li[1][2][1][0][1],li[1][2][1][1][1]), radius=15, color=color.green) 

# Traitement des edges
arrows_tmp = []
for li in edge:
    if len(li[1]) > 3:
        arrows_tmp.append(li) 
arrows = []
for li in arrows_tmp:
    if len(li[1][3][1]) > 3:
        arrows.append(li)    

for li in arrows:   
    pointer = arrow(pos=(li[1][3][1][0][1],li[1][3][1][1][1]), axis=(li[1][3][1][2][1],li[1][3][1][3][1]), shaftwidth=1)
    
    
    
